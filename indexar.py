import os
import shutil
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Configuração de diretórios
diretorio_data = "./data"
diretorio_db = "./chroma_db"

# SEGURANÇA: Limpa o banco antigo para evitar mistura de dados ou erros de persistência
if os.path.exists(diretorio_db):
    print("Removendo banco de dados antigo...")
    shutil.rmtree(diretorio_db)

# 2. Carregamento dos documentos
documentos = []

if not os.path.exists(diretorio_data):
    print(f"ERRO: A pasta '{diretorio_data}' não existe. Crie a pasta e coloque seus PDFs lá!")
    exit()

print("Iniciando a leitura dos arquivos...")
arquivos = [f for f in os.listdir(diretorio_data) if f.endswith(".pdf")]

if not arquivos:
    print("ERRO: Nenhum arquivo PDF encontrado na pasta './data'.")
    exit()

for arquivo in arquivos:
    caminho = os.path.join(diretorio_data, arquivo)
    print(f"-> Lendo: {arquivo}")
    
    loader = PyPDFLoader(caminho)
    paginas = loader.load()
    
    if not paginas or len(paginas) == 0:
        print(f"   ALERTA: O arquivo {arquivo} não retornou texto (pode ser imagem).")
    else:
        print(f"   Sucesso: {len(paginas)} páginas extraídas.")
        documentos.extend(paginas)

# 3. Processamento e Indexação
if not documentos:
    print("ERRO: Nenhum texto foi extraído. O banco não será criado.")
    exit()

print(f"\nDividindo {len(documentos)} documentos em pedaços...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = text_splitter.split_documents(documentos)

print(f"Criando embeddings e salvando no ChromaDB ({len(chunks)} trechos)...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Criação do banco
db = Chroma.from_documents(chunks, embeddings, persist_directory=diretorio_db)

# 4. Verificação Final (O Checkpoint)
# Se o script chegou aqui e o count for > 0, o seu banco está pronto!
print(f"\nSUCESSO TOTAL!")
print(f"O banco de dados foi criado com {len(chunks)} trechos de texto.")
