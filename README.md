# Jarvis: Assistente de Estudos e Gestão Acadêmica

Este projeto consiste em um agente inteligente desenvolvido para auxiliar estudantes na organização de tarefas, consulta de conteúdos técnicos e aprendizado ativo. O sistema combina **RAG (Retrieval-Augmented Generation)**, **Tool Calling** e um **gerenciador de tarefas persistente**, com interface web via Streamlit.

## Estrutura do Projeto

| Arquivo | Responsabilidade |
|---------|-----------------|
| `agente.py` | Loop de conversa via terminal (alternativa ao Streamlit) |
| `chat_rag.py` | Orquestração central: RAG, LLM, tool calling e active recall |
| `app.py` | Interface web Streamlit com histórico e sidebar de tarefas |
| `database.py` | Camada de persistência SQLite (CRUD de tarefas) |
| `ferramentas.py` | Wrappers das ferramentas disponíveis ao agente |
| `indexar.py` | Script de setup: processa PDFs e cria o banco vetorial |
| `data/` | 10 documentos acadêmicos em PDF (IHC e APS) |
| `chroma_db/` | Banco de dados vetorial gerado pelo `indexar.py` |

## Funcionalidades

### Trabalho 1
- **3.1 Consulta a materiais (RAG):** perguntas sobre os PDFs indexados
- **3.2 Agenda acadêmica:** consulta e adição de eventos por data
- **3.3 Lista de tarefas:** adicionar, listar, concluir e remover tarefas

### Trabalho 2 (novas funcionalidades)
- **3.4 Planejamento de estudos:** combina agenda + tarefas + material RAG para gerar um plano personalizado
- **Geração de exercícios:** cria questões práticas sobre qualquer tópico do dataset
- **Active Recall interativo:** o sistema gera uma pergunta, o aluno responde, e o sistema avalia e fornece feedback detalhado
- **Histórico de conversa:** o agente mantém o contexto das últimas trocas
- **Data atual injetada:** o agente resolve "hoje", "amanhã" e "esta semana" corretamente

## Ferramentas Disponíveis (Tool Calling)

| # | Ferramenta | Descrição |
|---|-----------|-----------|
| 1 | `adicionar_tarefa_agenda` | Adiciona tarefa com data |
| 2 | `consultar_agenda` | Consulta tarefas de uma data específica |
| 3 | `listar_tarefas` | Lista todas as tarefas pendentes |
| 4 | `concluir_tarefa` | Marca tarefa como concluída pelo ID |
| 5 | `remover_tarefa` | Remove tarefa pelo ID |
| 6 | `buscar_material_rag` | Busca semântica nos documentos |
| 7 | `planejar_estudos` | Gera plano de estudos personalizado |
| 8 | `gerar_exercicios` | Cria exercícios sobre um tópico |
| 9 | `active_recall` | Inicia sessão de active recall interativa |

## Dataset

- **10 documentos** acadêmicos sobre IHC e Análise e Projeto de Software
- Veja [DATASET.md](./DATASET.md) para documentação completa (origem, limitações, estratégia de chunking)

## Avaliação e Análise de Erros

- Veja [AVALIACAO.md](./AVALIACAO.md) para a avaliação com 10 perguntas e 3 análises de falhas

## Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| LLM | Qwen2.5-14B-Instruct-AWQ (API institucional UFMS) |
| Orquestração | LangChain |
| Banco vetorial | ChromaDB |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Persistência | SQLite |
| Interface | Streamlit |

## Como Instalar e Executar

### 1. Pré-requisitos
- Python 3.10 ou superior
- `pip` instalado

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Indexar os documentos (apenas na primeira vez)
```bash
python indexar.py
```

### 4. Iniciar a interface
**Opção 1 — Automático:** clique duas vezes em `iniciar.bat`

**Opção 2 — Manual:**
```bash
python -m streamlit run app.py
```

## IAs Utilizadas no Desenvolvimento

- **Cursor (Claude Sonnet):** geração e refatoração de código, arquitetura do sistema
- **Qwen2.5-14B-Instruct-AWQ:** LLM de produção do agente (via API institucional)
