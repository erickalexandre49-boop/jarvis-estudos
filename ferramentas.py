"""
ferramentas.py — Wrappers de ferramentas do JARVIS.

Cada função aqui representa uma ferramenta disponível para o agente.
A orquestração (decisão de qual chamar) é feita pela LLM em chat_rag.py.
"""

import database


def consultar_agenda(data: str = None) -> str:
    """Consulta a agenda para uma data específica (formato YYYY-MM-DD) ou lista tudo."""
    return database.listar_tarefas(data)


def adicionar_tarefa_agenda(tarefa: str, data: str) -> str:
    """Adiciona uma nova tarefa na agenda com uma data limite."""
    return database.adicionar_tarefa(tarefa, data)


def listar_tarefas() -> str:
    """Lista todas as tarefas pendentes."""
    return database.listar_tarefas()


def concluir_tarefa(id_tarefa: int) -> str:
    """Marca uma tarefa como concluída pelo seu ID."""
    return database.concluir_tarefa(id_tarefa)


def remover_tarefa(id_tarefa: int) -> str:
    """Remove permanentemente uma tarefa pelo seu ID."""
    return database.remover_tarefa(id_tarefa)
