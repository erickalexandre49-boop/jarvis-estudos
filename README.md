# Jarvis: Assistente de Estudos e Gestão Acadêmica

Este projeto consiste em um agente inteligente desenvolvido para auxiliar estudantes na organização de tarefas e consulta de conteúdos técnicos. O sistema combina um mecanismo de **RAG (Retrieval-Augmented Generation)** com um gerenciador de tarefas persistente, operando de forma modular via terminal.

## 🏗️ Estrutura do Projeto

O sistema foi arquitetado para promover a separação de responsabilidades (baixa acoplagem), facilitando a manutenção e a escalabilidade:

* `agente.py`: O "cérebro" do projeto. Gerencia o loop de conversa, o classificador de intenções e o roteamento entre as ferramentas e o RAG.
* `chat_rag.py`: Módulo especializado na lógica de consulta aos documentos (RAG) e interação com a base vetorial.
* `database.py`: Camada de persistência de dados (CRUD) usando SQLite para gestão de tarefas.
* `ferramentas.py`: Contém a lógica das funções auxiliares que o agente utiliza (ações na agenda).
* `indexar.py`: Script de preparação (setup) responsável por processar os PDFs e criar a base vetorial.
* `data/`: Pasta contendo os 10 documentos técnicos (PDFs) sobre IHC e APS.
* `chroma_db/`: Banco de dados vetorial (gerado na primeira execução).

## 📊 Dataset
Este projeto utiliza 10 documentos sobre Interação Humano-Computador e Análise e Projeto de Software Orientado a Objetos armazenados na pasta `/data`.
* [Clique aqui para ver a documentação técnica detalhada do dataset](./DATASET.md)

## ⚙️ Tecnologias Utilizadas

* **Orquestração:** LangChain (integração entre memória, ferramentas e LLM).
* **LLM:** Google Gemma 3 12B (via API institucional).
* **Base de Dados Vetorial:** ChromaDB (armazenamento semântico).
* **Embeddings:** HuggingFace `all-MiniLM-L6-v2`.
* **Persistência:** SQLite (gestão local de tarefas).

## 🚀 Como Instalar e Executar

Siga os passos abaixo para configurar o ambiente de execução:

### 1. Pré-requisitos
* Python 3.10 ou superior instalado.
* `pip` instalado.

### 2. Instalação de Dependências
No terminal, dentro da pasta raiz do projeto, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt

Configuração Inicial (Indexação)
O sistema necessita que os documentos sejam processados para o RAG funcionar. Execute o script de indexação uma única vez:

Bash
python indexar.py

## 🚀 Como Executar

Existem duas formas de iniciar o Jarvis:

**Opção 1: Execução Automática (Recomendado)**
Basta dar dois cliques no arquivo `iniciar.bat` localizado na raiz do projeto. Ele ativará o ambiente virtual e iniciará a interface automaticamente.

**Opção 2: Execução Manual (Terminal)**
Se preferir ou se precisar depurar o sistema, abra o terminal na pasta do projeto e execute:
1. Ative o ambiente: `.\venv\Scripts\activate`
2. Inicie o sistema: `python -m streamlit run app.py`