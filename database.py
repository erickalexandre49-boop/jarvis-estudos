import sqlite3

def init_db():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    
    # MUDE DESTE JEITO:
    # Cria a tabela apenas SE ELA NÃO EXISTIR
    cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       descricao TEXT, 
                       data TEXT, 
                       status TEXT)''')
    
    conn.commit()
    conn.close()

def adicionar_tarefa(descricao, data_limite):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (descricao, data, status) VALUES (?, ?, ?)", 
                   (descricao, data_limite, "pendente"))
    conn.commit()
    conn.close()
    return f"Tarefa '{descricao}' agendada para {data_limite}!"

def listar_tarefas(data=None):
    # Válvula de segurança: se o agente passar "TODAS", tratamos como None
    if data == "TODAS":
        data = None

    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    
    # 1. Ajuste: Selecionar o 'id' também no SELECT
    if data:
        # Busca ID e Descrição quando há filtro de data
        cursor.execute("SELECT id, descricao FROM tarefas WHERE data=? AND status='pendente'", (data,))
    else:
        # Busca ID, Descrição e Data quando lista tudo
        cursor.execute("SELECT id, descricao, data FROM tarefas WHERE status='pendente'")
    
    tarefas = cursor.fetchall()
    conn.close()

<<<<<<< HEAD
    #Verificamos se há tarefas
=======
>>>>>>> 793fc46 (Limpeza: removendo arquivos desnecessários e ignorando pastas de cache/banco)
    if not tarefas:
        if data:
            return f"Você não tem nada pendente para o dia {data}."
        else:
            return "Você não tem nenhuma tarefa pendente no momento."

    # 2. Ajuste: Formatação da string para incluir o ID
    resultado = "Aqui estão suas tarefas pendentes (use o ID para concluir ou remover):\n"
    for t in tarefas:
        if data:
            # t[0] = id, t[1] = descricao
            resultado += f"• [ID: {t[0]}] {t[1]}\n"
        else:
            # t[0] = id, t[1] = descricao, t[2] = data
            resultado += f"• [ID: {t[0]}] {t[1]} (Data: {t[2]})\n"
            
    return resultado

def remover_tarefa(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    return f"Tarefa com ID {id_tarefa} removida com sucesso!"

def concluir_tarefa(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    # Atualiza o status da tarefa para 'concluída' baseada no ID
    cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    return f"Tarefa com ID {id_tarefa} marcada como concluída com sucesso!"


# Cria o banco de dados quando rodar o arquivo diretamente
if __name__ == "__main__":
    init_db()
    print("Banco de dados criado com sucesso!")
