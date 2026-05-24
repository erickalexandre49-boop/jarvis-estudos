from chat_rag import responder_pergunta
from database import init_db

def executar_agente():
    # Inicializa o banco de dados uma única vez
    init_db()
    
    print("--- JARVIS Acadêmico Iniciado ---")
    print("Olá! Como posso ajudar nos seus estudos ou tarefas?")
    
    while True:
        try:
            pergunta = input("\nVocê: ")
            if pergunta.lower() in ["sair", "exit", "quit"]:
                print("Encerrando JARVIS...")
                break
            
            # O agente agora delega tudo para o responder_pergunta
            # Ele já sabe se deve chamar o RAG ou uma Ferramenta
            resposta = responder_pergunta(pergunta)
            
            print(f"JARVIS: {resposta}")
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    executar_agente()