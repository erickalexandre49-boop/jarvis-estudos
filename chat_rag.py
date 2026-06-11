import json
import re
import logging
from datetime import datetime
from openai import OpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from database import adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa

logging.basicConfig(
    filename='agente.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)

client = OpenAI(
    base_url='https://llm.liaufms.org/v1/qwen2-5-14b-instruct-awq',
    api_key='REIkURcI7rTTqsTwlJi8MrgnKFwOiqky7Ezh7hH-l-k'
)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

SYSTEM_BASE = """Você é o JARVIS, um assistente acadêmico inteligente, prestativo e motivador.

FERRAMENTAS DISPONÍVEIS — use JSON_TOOL quando a ação for necessária:
1.  Adicionar tarefa   : JSON_TOOL: {"acao": "adicionar_tarefa_agenda", "tarefa": "descrição", "data": "YYYY-MM-DD"}
2.  Consultar agenda  : JSON_TOOL: {"acao": "consultar_agenda", "data": "YYYY-MM-DD"}
3.  Listar tarefas    : JSON_TOOL: {"acao": "listar_tarefas"}
4.  Concluir tarefa   : JSON_TOOL: {"acao": "concluir_tarefa", "id_tarefa": ID}
5.  Remover tarefa    : JSON_TOOL: {"acao": "remover_tarefa", "id_tarefa": ID}
6.  Buscar material   : JSON_TOOL: {"acao": "buscar_material_rag", "pergunta": "consulta"}
7.  Plano de estudos  : JSON_TOOL: {"acao": "planejar_estudos", "topico": "tema", "data_prova": "YYYY-MM-DD"}
8.  Gerar exercícios  : JSON_TOOL: {"acao": "gerar_exercicios", "topico": "tema", "quantidade": 3}
9.  Active recall     : JSON_TOOL: {"acao": "active_recall", "topico": "tema"}

REGRAS OBRIGATÓRIAS:
- Use ferramentas para qualquer ação de agenda ou tarefas.
- Para consultas sobre materiais, use exclusivamente o CONTEXTO ACADÊMICO fornecido.
- Se a informação não estiver no contexto, responda: "Desculpe, essa informação não consta nos documentos do projeto."
- Nunca invente dados ou use conhecimento externo não fornecido.
- Responda sempre em português do Brasil."""


def _chamar_llm(mensagens: list) -> str:
    response = client.chat.completions.create(
        model='Qwen/Qwen2.5-14B-Instruct-AWQ',
        messages=mensagens
    )
    return response.choices[0].message.content.strip()


def _executar_ferramenta(data_json: dict) -> tuple[str, object]:
    acao = data_json.get("acao", "")

    if acao == "adicionar_tarefa_agenda":
        resultado = adicionar_tarefa(data_json['tarefa'], data_json['data'])

    elif acao == "consultar_agenda":
        resultado = listar_tarefas(data_json.get('data'))

    elif acao == "listar_tarefas":
        resultado = listar_tarefas()

    elif acao == "concluir_tarefa":
        resultado = concluir_tarefa(data_json['id_tarefa'])

    elif acao == "remover_tarefa":
        resultado = remover_tarefa(data_json['id_tarefa'])

    elif acao == "buscar_material_rag":
        docs = db.similarity_search(data_json['pergunta'], k=3)
        resultado = "\n\n".join([d.page_content for d in docs])

    elif acao == "planejar_estudos":
        topico = data_json.get('topico', '')
        data_prova = data_json.get('data_prova')
        tarefas_str = listar_tarefas()
        agenda_str = listar_tarefas(data_prova) if data_prova else "Nenhuma data de prova especificada."
        docs = db.similarity_search(topico, k=5)
        material = "\n\n".join([d.page_content for d in docs])
        resultado = {
            "tarefas_pendentes": tarefas_str,
            "agenda": agenda_str,
            "material": material[:2500],
        }

    elif acao == "gerar_exercicios":
        topico = data_json.get('topico', '')
        quantidade = int(data_json.get('quantidade', 3))
        docs = db.similarity_search(topico, k=4)
        material = "\n\n".join([d.page_content for d in docs])
        resultado = {"topico": topico, "quantidade": quantidade, "material": material[:2500]}

    elif acao == "active_recall":
        topico = data_json.get('topico', '')
        docs = db.similarity_search(topico, k=3)
        material = "\n\n".join([d.page_content for d in docs])
        resultado = {"topico": topico, "material": material[:2000]}

    else:
        resultado = f"Ação desconhecida: '{acao}'."

    logging.info(f"FERRAMENTA: {acao} | ENTRADA: {data_json} | SAÍDA: {str(resultado)[:300]}")
    return acao, resultado


def _sintetizar_ferramenta(acao: str, resultado: object, pergunta_original: str) -> str:
    """Faz uma segunda chamada à LLM para gerar resposta a partir do resultado da ferramenta."""

    if acao == "planejar_estudos":
        r = resultado
        prompt_sintese = f"""Com base nos dados abaixo, crie um plano de estudos detalhado e personalizado.

TAREFAS PENDENTES:
{r.get('tarefas_pendentes', 'Nenhuma')}

AGENDA / PRÓXIMA PROVA:
{r.get('agenda', 'Sem data especificada')}

MATERIAL DE ESTUDO DISPONÍVEL:
{r.get('material', '')}

SOLICITAÇÃO DO USUÁRIO: {pergunta_original}

Monte um plano organizado com tópicos prioritários, sugestões de tempo por tema e orientações práticas de estudo."""

    elif acao == "gerar_exercicios":
        r = resultado
        prompt_sintese = f"""Com base no material abaixo, gere exatamente {r.get('quantidade', 3)} exercícios práticos sobre "{r.get('topico', '')}".

MATERIAL DE REFERÊNCIA:
{r.get('material', '')}

Para cada exercício:
- Número e enunciado claro
- Nível de dificuldade: (Fácil / Médio / Difícil)
- Resposta esperada (ao final, em seção separada "Gabarito")"""

    elif acao == "active_recall":
        r = resultado
        prompt_sintese = f"""Com base no material abaixo sobre "{r.get('topico', '')}", formule UMA única pergunta desafiadora de active recall para testar o conhecimento do usuário.

MATERIAL DE REFERÊNCIA:
{r.get('material', '')}

Regras:
- Faça apenas a pergunta, sem revelar a resposta.
- A pergunta deve exigir raciocínio, não apenas memorização.
- Termine com a tag exata: [ACTIVE_RECALL_QUESTION]"""

    else:
        return str(resultado)

    mensagens = [
        {"role": "system", "content": "Você é o JARVIS, assistente acadêmico. Responda de forma clara, estruturada e em português do Brasil."},
        {"role": "user", "content": prompt_sintese},
    ]
    return _chamar_llm(mensagens)


def responder_pergunta(pergunta: str, historico: list = None) -> str:
    if historico is None:
        historico = []

    # RAG — busca contexto relevante
    docs = db.similarity_search(pergunta, k=3)
    contexto = "\n\n".join([d.page_content for d in docs])

    # Histórico das últimas 3 trocas (6 mensagens)
    historico_str = ""
    for msg in historico[-6:]:
        papel = "Usuário" if msg["role"] == "user" else "JARVIS"
        historico_str += f"{papel}: {msg['content']}\n"

    data_hoje = datetime.now().strftime("%Y-%m-%d")
    dia_semana = datetime.now().strftime("%A")
    nomes_dias = {
        "Monday": "segunda-feira", "Tuesday": "terça-feira", "Wednesday": "quarta-feira",
        "Thursday": "quinta-feira", "Friday": "sexta-feira", "Saturday": "sábado", "Sunday": "domingo"
    }
    dia_semana_pt = nomes_dias.get(dia_semana, dia_semana)

    system_content = f"""{SYSTEM_BASE}

DATA E HORA ATUAL: {data_hoje} ({dia_semana_pt}) — use esta data para resolver "hoje", "amanhã", "esta semana" etc.

CONTEXTO ACADÊMICO (trechos recuperados para esta pergunta):
{contexto}

HISTÓRICO RECENTE DA CONVERSA:
{historico_str if historico_str else "(início da conversa)"}"""

    mensagens = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": pergunta},
    ]

    try:
        resposta_ia = _chamar_llm(mensagens)

        # Detecta chamada de ferramenta
        if "JSON_TOOL:" in resposta_ia:
            match = re.search(r'\{.*?\}', resposta_ia, re.DOTALL)
            if match:
                json_str = match.group(0)
                data_json = json.loads(json_str)
                acao, resultado = _executar_ferramenta(data_json)

                # Ferramentas que precisam de síntese pela LLM
                if acao in ("planejar_estudos", "gerar_exercicios", "active_recall"):
                    return _sintetizar_ferramenta(acao, resultado, pergunta)

                # Ferramentas simples — retorna apenas o resultado da ferramenta
                return str(resultado)

        return resposta_ia

    except Exception as e:
        logging.error(f"ERRO em responder_pergunta: {e}")
        return f"Ocorreu um erro ao processar sua mensagem: {str(e)}"


def avaliar_resposta_active_recall(pergunta_gerada: str, resposta_usuario: str, topico: str) -> str:
    """Avalia a resposta do usuário em uma sessão de active recall."""
    docs = db.similarity_search(topico, k=3)
    contexto = "\n\n".join([d.page_content for d in docs])

    prompt = f"""Você é um professor avaliando a resposta de um aluno em um exercício de active recall.

PERGUNTA FEITA AO ALUNO:
{pergunta_gerada}

RESPOSTA DO ALUNO:
{resposta_usuario}

MATERIAL DE REFERÊNCIA:
{contexto}

Avalie seguindo este formato:
**Classificação:** ✅ Correta | ⚠️ Parcialmente correta | ❌ Incorreta

**O que acertou:**
(explique os pontos corretos)

**O que pode melhorar:**
(corrija ou complemente o que estava errado/incompleto)

**Dica de reforço:**
(sugira como aprofundar o estudo neste ponto)"""

    try:
        mensagens = [
            {"role": "system", "content": "Você é um professor avaliador construtivo. Responda em português do Brasil."},
            {"role": "user", "content": prompt},
        ]
        resposta = _chamar_llm(mensagens)
        logging.info(f"ACTIVE_RECALL_EVAL | PERGUNTA: {pergunta_gerada[:80]} | RESPOSTA_ALUNO: {resposta_usuario[:80]}")
        return resposta
    except Exception as e:
        logging.error(f"ERRO em avaliar_resposta_active_recall: {e}")
        return f"Erro ao avaliar resposta: {str(e)}"
