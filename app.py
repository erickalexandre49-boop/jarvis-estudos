import streamlit as st
from chat_rag import responder_pergunta, avaliar_resposta_active_recall
from database import init_db, listar_tarefas

init_db()

st.set_page_config(
    page_title="JARVIS Acadêmico",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🤖 JARVIS")
    st.caption("Assistente Acadêmico Inteligente")
    st.divider()

    st.subheader("📋 Tarefas Pendentes")
    tarefas_str = listar_tarefas()
    st.markdown(tarefas_str)

    st.divider()
    st.subheader("💡 Exemplos de uso")
    st.markdown("""
**📚 Consulta ao material:**
> "O que é RAG?"
> "Explique regressão logística"

**📅 Agenda:**
> "O que tenho hoje?"
> "Adicione prova de IA para 20/06"

**✅ Tarefas:**
> "Quais são minhas tarefas?"
> "Conclua a tarefa 3"

**🗓️ Planejamento:**
> "Monte um plano de estudos para a prova de IHC"
> "O que devo priorizar hoje?"

**🧠 Aprendizado ativo:**
> "Gere 3 exercícios sobre embeddings"
> "Quero fazer active recall sobre UML"
""")

    st.divider()
    if st.button("🔄 Atualizar tarefas"):
        st.rerun()

# ── Session State ───────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "active_recall_mode" not in st.session_state:
    st.session_state.active_recall_mode = False

if "active_recall_question" not in st.session_state:
    st.session_state.active_recall_question = None

if "active_recall_topic" not in st.session_state:
    st.session_state.active_recall_topic = None

# ── Cabeçalho principal ─────────────────────────────────────────────────────────
st.title("🤖 JARVIS — Assistente Acadêmico")

# Indicador de modo active recall
if st.session_state.active_recall_mode:
    st.warning(
        "🧠 **Modo Active Recall ativo** — Responda à pergunta acima. "
        "Digite **sair** para encerrar o exercício.",
        icon="🎯",
    )

# ── Histórico de mensagens ──────────────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Entrada do usuário ──────────────────────────────────────────────────────────
if prompt := st.chat_input("Como posso te ajudar hoje?"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):

            # ── Modo Active Recall: avalia a resposta do aluno ──────────────────
            if st.session_state.active_recall_mode:
                if prompt.strip().lower() in ("sair", "cancelar", "exit", "parar"):
                    response = (
                        "✅ Sessão de active recall encerrada. "
                        "Continue assim — a prática constante é o segredo do aprendizado!"
                    )
                    st.session_state.active_recall_mode = False
                    st.session_state.active_recall_question = None
                    st.session_state.active_recall_topic = None
                else:
                    response = avaliar_resposta_active_recall(
                        st.session_state.active_recall_question,
                        prompt,
                        st.session_state.active_recall_topic,
                    )
                    st.session_state.active_recall_mode = False
                    st.session_state.active_recall_question = None
                    st.session_state.active_recall_topic = None

            # ── Modo normal: processa via agente ────────────────────────────────
            else:
                response = responder_pergunta(
                    prompt,
                    historico=st.session_state.messages[:-1],  # exclui a mensagem atual
                )

                # Detecta se o agente gerou uma pergunta de active recall
                if "[ACTIVE_RECALL_QUESTION]" in response:
                    response = response.replace("[ACTIVE_RECALL_QUESTION]", "").strip()
                    st.session_state.active_recall_mode = True
                    st.session_state.active_recall_question = response
                    # Extrai o tópico da mensagem do usuário
                    st.session_state.active_recall_topic = prompt

        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
