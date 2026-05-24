import streamlit as st
from chat_rag import responder_pergunta
from ferramentas import listar_tarefas, adicionar_tarefa_agenda
from database import init_db, adicionar_tarefa, listar_tarefas, remover_tarefa, concluir_tarefa

init_db()

st.set_page_config(page_title="Jarvis AI", page_icon="🤖")

st.title("🤖 Jarvis - Assistente Acadêmico")

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Como posso te ajudar hoje?"):
    # Exibe a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera a resposta do Jarvis
    with st.chat_message("assistant"):
        # Chama a sua função de chat_rag que você já criou!
        response = responder_pergunta(prompt) 
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})