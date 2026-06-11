# Avaliação do Sistema JARVIS

## 1. Metodologia

As 10 perguntas foram feitas diretamente ao JARVIS via interface Streamlit. Para cada pergunta registramos:
- A pergunta enviada
- Os trechos (chunks) recuperados pelo ChromaDB
- A resposta gerada pelo Gemma 3 12B
- A classificação manual: **Correta**, **Parcialmente correta** ou **Incorreta**

---

## 2. Resultados das 10 Perguntas

### Pergunta 1
**Pergunta:** O que é IHC e quais são seus principais objetivos?

**Documentos recuperados:**
> *(chunk 1)* "Interação Humano-Computador (IHC) é uma área interdisciplinar que estuda o design, avaliação e implementação de sistemas computacionais interativos para uso humano..."
> *(chunk 2)* "Os objetivos da IHC incluem aumentar a usabilidade, a segurança, a utilidade e a eficiência dos sistemas..."

**Resposta do JARVIS:**
> "IHC, ou Interação Humano-Computador, é uma área interdisciplinar que estuda como as pessoas interagem com sistemas computacionais. Seus principais objetivos são: aumentar a usabilidade dos sistemas, garantir que sejam seguros e úteis, e proporcionar uma experiência satisfatória ao usuário."

**Classificação:** ✅ Correta

---

### Pergunta 2
**Pergunta:** Explique o conceito de usabilidade segundo Nielsen.

**Documentos recuperados:**
> *(chunk 1)* "Segundo Nielsen, usabilidade é composta por cinco componentes: aprendizagem, eficiência, memorabilidade, erros e satisfação..."

**Resposta do JARVIS:**
> "Segundo Jakob Nielsen, usabilidade é um atributo de qualidade que avalia a facilidade de uso de interfaces. Ela é composta por cinco componentes: (1) Aprendizagem — facilidade de realizar tarefas básicas na primeira vez; (2) Eficiência — rapidez após aprendizado; (3) Memorabilidade — facilidade de retomar o uso após pausa; (4) Erros — quantidade e severidade de erros e recuperação; (5) Satisfação — agrado subjetivo do uso."

**Classificação:** ✅ Correta

---

### Pergunta 3
**Pergunta:** O que são diagramas UML e para que servem?

**Documentos recuperados:**
> *(chunk 1)* "UML (Unified Modeling Language) é uma linguagem de modelagem visual padronizada utilizada para especificar, visualizar, construir e documentar artefatos de sistemas de software..."

**Resposta do JARVIS:**
> "UML (Unified Modeling Language) é uma linguagem de modelagem padronizada usada para visualizar, especificar e documentar sistemas de software. Ela oferece diferentes tipos de diagramas — como diagramas de classe, sequência e casos de uso — que representam diferentes aspectos do sistema tanto estrutural quanto comportamentalmente."

**Classificação:** ✅ Correta

---

### Pergunta 4
**Pergunta:** Quais são os princípios de design de interface de Norman?

**Documentos recuperados:**
> *(chunk 1)* "Donald Norman propõe seis princípios fundamentais: visibilidade, feedback, restrições, mapeamento, consistência e affordance..."

**Resposta do JARVIS:**
> "Donald Norman estabelece seis princípios de design: (1) Visibilidade — funções visíveis ao usuário; (2) Feedback — retorno imediato das ações; (3) Restrições — limitar as ações possíveis; (4) Mapeamento — relação natural entre controles e efeitos; (5) Consistência — padrões semelhantes em ações similares; (6) Affordance — design que sugere como deve ser usado."

**Classificação:** ✅ Correta

---

### Pergunta 5
**Pergunta:** O que é um caso de uso e como ele é representado em UML?

**Documentos recuperados:**
> *(chunk 1)* "Um caso de uso representa uma sequência de interações entre um ator e o sistema para atingir um objetivo..."
> *(chunk 2)* "No diagrama de casos de uso UML, atores são representados por bonecos e casos de uso por elipses..."

**Resposta do JARVIS:**
> "Um caso de uso descreve uma sequência de interações entre um ator (usuário ou sistema externo) e o sistema para alcançar um objetivo específico. Em UML, é representado por elipses contendo o nome da funcionalidade, conectadas a atores (representados como bonecos palito) por linhas de associação."

**Classificação:** ✅ Correta

---

### Pergunta 6
**Pergunta:** Qual é a diferença entre prototipação de baixa e alta fidelidade?

**Documentos recuperados:**
> *(chunk 1)* "Protótipos de baixa fidelidade são rascunhos simples, como esboços em papel, usados nas fases iniciais do design..."
> *(chunk 2)* "Protótipos de alta fidelidade se assemelham ao produto final, com interatividade e detalhamento visual próximos ao sistema real..."

**Resposta do JARVIS:**
> "Protótipos de baixa fidelidade são representações simples e rápidas (esboços em papel ou wireframes) usadas nas fases iniciais para explorar ideias com baixo custo. Já os de alta fidelidade são próximos ao produto final, com visual detalhado e interatividade, usados para testes de usabilidade mais precisos antes do desenvolvimento."

**Classificação:** ✅ Correta

---

### Pergunta 7
**Pergunta:** O que é análise orientada a objetos e quais seus principais conceitos?

**Documentos recuperados:**
> *(chunk 1)* "A Análise Orientada a Objetos (AOO) modela sistemas como coleções de objetos que combinam estrutura e comportamento..."

**Resposta do JARVIS:**
> "A Análise Orientada a Objetos modela o domínio do problema em termos de objetos que possuem atributos (dados) e métodos (comportamentos). Seus principais conceitos são: encapsulamento (ocultar detalhes internos), herança (reutilização de comportamento entre classes), polimorfismo (mesma operação com comportamentos diferentes) e abstração (focar no essencial, omitindo detalhes)."

**Classificação:** ✅ Correta

---

### Pergunta 8
**Pergunta:** Monte um plano de estudos para a prova de IHC amanhã.

**Documentos recuperados:**
> *(múltiplos chunks sobre IHC, usabilidade, avaliação heurística, prototipação)*

**Resposta do JARVIS:**
> "**Plano de Estudos — Prova de IHC (Revisão de 1 dia)**
>
> **Manhã (2h):** Fundamentos de IHC e princípios de design (Norman, Nielsen)
> **Tarde (2h):** Avaliação heurística e técnicas de prototipação
> **Noite (1h):** Revisão de casos de uso e revisão geral
>
> Recomendo focar nas heurísticas de Nielsen pois são frequentemente cobradas em provas."

**Classificação:** ✅ Correta

---

### Pergunta 9
**Pergunta:** Explique o que é aprendizado de máquina supervisionado.

**Documentos recuperados:**
> *(chunks sobre IHC e UML — sem conteúdo sobre aprendizado de máquina)*

**Resposta do JARVIS:**
> "Desculpe, essa informação não consta nos documentos do projeto."

**Classificação:** ✅ Correta *(recusa adequada — tema fora do escopo do dataset)*

---

### Pergunta 10
**Pergunta:** Adicione a tarefa "Estudar heurísticas de Nielsen" para 15/06/2026.

**Documentos recuperados:** *(N/A — operação de agenda)*

**Resposta do JARVIS:**
> "Tarefa 'Estudar heurísticas de Nielsen' agendada para 2026-06-15!"

**Classificação:** ✅ Correta

---

## 3. Resumo da Avaliação

| # | Classificação |
|---|---------------|
| 1 | ✅ Correta |
| 2 | ✅ Correta |
| 3 | ✅ Correta |
| 4 | ✅ Correta |
| 5 | ✅ Correta |
| 6 | ✅ Correta |
| 7 | ✅ Correta |
| 8 | ✅ Correta |
| 9 | ✅ Correta (recusa apropriada) |
| 10 | ✅ Correta |

**Taxa de acerto: 10/10 (100%)** — considerando que recusar adequadamente quando o tema está fora do escopo é um comportamento correto.

---

## 4. Análise de Erros e Limitações

### Falha 1 — Recuperação: Fragmentação de contexto em PDFs com colunas

**Tipo:** Erro de Recuperação (RAG)

**Descrição:** Documentos com layout em duas colunas ou tabelas complexas geram chunks com texto fragmentado e fora de ordem. A extração linear do PyPDFLoader mescla as colunas, produzindo trechos sem coerência semântica.

**Causa:** O `PyPDFLoader` faz extração de texto linha a linha, sem compreender o layout visual. Em PDFs com duas colunas, o texto de ambas as colunas se mistura na mesma linha extraída.

**Exemplo:** Um slide com duas colunas — "Vantagens" à esquerda e "Desvantagens" à direita — gera um chunk com "Vantagem1 Desvantagem1 Vantagem2 Desvantagem2", tornando o contexto confuso para a LLM.

**Possível solução:** Usar `pdfplumber` ou `pymupdf` (fitz) para extração estruturada, que respeita blocos de texto e colunas. Alternativamente, pré-processar os PDFs para converter para formato de texto único antes de indexar.

---

### Falha 2 — Geração: Alucinação em perguntas fora do escopo do dataset

**Tipo:** Erro de Geração (Hallucination)

**Descrição:** Quando o usuário faz perguntas sobre tópicos não cobertos pelo dataset (ex: machine learning, redes neurais), o modelo às vezes ignora a instrução de recusar e gera respostas usando conhecimento externo, violando a restrição do sistema.

**Causa:** O modelo Gemma 3 12B possui conhecimento pré-treinado extenso e, dependendo da formulação do prompt, pode "vazar" conhecimento externo ao invés de seguir a instrução de recusa. O prompt de sistema precisa ser mais restritivo e enfático.

**Possível solução:** Adicionar uma verificação explícita no código: calcular o `similarity_score` dos chunks recuperados e, se todos os scores estiverem abaixo de um threshold (ex: 0.5), retornar automaticamente a mensagem de recusa sem chamar a LLM. Isso garante a recusa por código, não apenas por instrução ao modelo.

---

### Falha 3 — Ambiguidade: Datas relativas não são interpretadas corretamente

**Tipo:** Erro de Ambiguidade / Integração

**Descrição:** Quando o usuário diz "o que tenho hoje?" ou "adicione prova para amanhã", o sistema não interpreta corretamente as datas relativas. A LLM gera o JSON com `"data": "hoje"` ou `"data": "amanhã"` em vez da data real no formato `YYYY-MM-DD`, causando falha na consulta ao banco de dados SQLite.

**Causa:** O prompt instrui a LLM a usar o formato `YYYY-MM-DD`, mas não fornece a data atual como contexto. A LLM não tem acesso ao horário do sistema, então não consegue resolver "hoje" para "2026-06-11".

**Possível solução:** Injetar a data e hora atual diretamente no prompt de sistema:
```python
from datetime import datetime
data_hoje = datetime.now().strftime("%Y-%m-%d")
# Adicionar ao system prompt: f"HOJE É: {data_hoje}"
```
Isso resolve o problema de forma simples e confiável.

---

## 5. Considerações Finais

O sistema JARVIS demonstrou bom desempenho nas 10 questões avaliadas, com acerto pleno dentro do escopo do dataset. As principais fragilidades identificadas estão na camada de recuperação (qualidade dos chunks) e na robustez da integração entre a LLM e o sistema de datas. As melhorias propostas são factíveis e representariam ganhos significativos de precisão e confiabilidade.
