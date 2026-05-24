# ferramentas.py

# Importe o seu módulo de banco de dados e o de RAG
import database
import chat_rag 

def adicionar_tarefa_agenda(tarefa, data):
    """Adiciona uma tarefa na agenda."""
    return database.adicionar_tarefa(tarefa, data)

def listar_tarefas():
    """Lista todas as tarefas pendentes na agenda."""
    return database.obter_todas_tarefas()

def concluir_tarefa(id_tarefa):
    """Marca uma tarefa como concluída."""
    return database.marcar_como_concluida(id_tarefa)

def remover_tarefa(id_tarefa):
    """Remove uma tarefa da agenda."""
    return database.remover_tarefa(id_tarefa)

def buscar_material_rag(pergunta):
    """Busca informações técnicas nos materiais de estudo."""
    # Chama a lógica que você já tem no chat_rag
    return chat_rag.responder_pergunta(pergunta)