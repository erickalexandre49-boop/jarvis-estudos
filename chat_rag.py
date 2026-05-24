import json
import re
import logging
from openai import OpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Importando apenas o necessário do banco de dados
from database import adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa

# --- CONFIGURAÇÃO DE LOGS (Essencial para o requisito de rastreabilidade) ---
logging.basicConfig(
    filename='agente.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)

# 1. Configuração do cliente da LLM
client = OpenAI(
    base_url='https://llm.liaufms.org/v1/gemma-3-12b-it', 
    api_key='Cxt2ftLF7d3mHS2JdiFqB-eSDAQeZvFATPXPs02lV9A'
)

# 2. Configuração do Banco de Dados
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

def responder_pergunta(pergunta):
    global db
    
    # --- PASSO 1: Fazer o RAG ANTES de montar o prompt ---
    docs = db.similarity_search(pergunta, k=3)
    contexto = "\n\n".join([d.page_content for d in docs])
    
    # --- PASSO 2: Montar o prompt ---
    prompt = f"""
    Você é o JARVIS Acadêmico.
    Se precisar usar uma ferramenta, escreva o JSON exatamente assim (use apenas uma ação por vez):
    JSON_TOOL: {{"acao": "adicionar_tarefa_agenda", "tarefa": "...", "data": "..."}}
    JSON_TOOL: {{"acao": "listar_tarefas"}}
    JSON_TOOL: {{"acao": "concluir_tarefa", "id_tarefa": 1}}
    JSON_TOOL: {{"acao": "remover_tarefa", "id_tarefa": 1}}
    JSON_TOOL: {{"acao": "buscar_material_rag", "pergunta": "..."}}
    
    Contexto acadêmico:
    {contexto}
    
    Pergunta do usuário: {pergunta}
    """

    try:
        response = client.chat.completions.create(
            model='google/gemma-3-12b-it',
            messages=[{'role': 'user', 'content': prompt}]
        )
        resposta_ia = response.choices[0].message.content.strip()

        # --- PASSO 3: Processar ferramenta se detectada ---
        if "JSON_TOOL:" in resposta_ia:
            match = re.search(r'\{.*\}', resposta_ia, re.DOTALL)
            if match:
                json_str = match.group(0)
                data_json = json.loads(json_str)
                acao = data_json.get("acao")
                res = ""
                
                # Execução das ferramentas
                if acao == "adicionar_tarefa_agenda":
                    res = adicionar_tarefa(data_json['tarefa'], data_json['data'])
                elif acao == "listar_tarefas":
                    res = listar_tarefas()
                elif acao == "concluir_tarefa":
                    res = concluir_tarefa(data_json['id_tarefa'])
                elif acao == "remover_tarefa":
                    res = remover_tarefa(data_json['id_tarefa'])
                elif acao == "buscar_material_rag":
                    docs_extra = db.similarity_search(data_json['pergunta'], k=3)
                    res = "Material encontrado: " + "\n".join([d.page_content for d in docs_extra])
                else:
                    res = "Ação desconhecida."
                
                # --- REGISTRO DE LOG ---
                logging.info(f"FERRAMENTA: {acao} | ENTRADA: {data_json} | SAÍDA: {res}")
                
                # Limpa a resposta
                resposta_limpa = resposta_ia.replace(json_str, "").replace("JSON_TOOL:", "").strip()
                return f"JARVIS: {res}\n\n{resposta_limpa}"

        return resposta_ia
    except Exception as e:
        return f"Erro ao processar: {str(e)}"