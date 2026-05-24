# Documentação Técnica do Dataset

## 1. Origem e Composição
* **Origem dos dados:** Os 10 documentos foram selecionados a partir de [ex: bibliografia da disciplina X / artigos técnicos selecionados do repositório da disciplina na UFMS].
* **Tipo de conteúdo:** Materiais acadêmicos em formato PDF, compreendendo apostilas de aula, capítulos de livros e slides explicativos sobre Interação Humano-Computador (IHC) e Análise de Projetos.

## 2. Limitações Conhecidas
* **Qualidade da Extração:** Como alguns PDFs possuem estruturas de colunas ou diagramas (UML), o processo de extração de texto pode ter ignorado legendas de imagens ou tabelas complexas.
* **Abrangência:** O dataset é limitado ao escopo técnico da disciplina. Consultas fora deste domínio acadêmico podem resultar em respostas genéricas ou alucinações.

## 3. Estratégia de Chunking
Para viabilizar a busca vetorial (RAG), os documentos foram processados utilizando a classe `RecursiveCharacterTextSplitter` da biblioteca LangChain:

* **Chunk Size:** 1000 caracteres.
* **Chunk Overlap (Sobreposição):** 200 caracteres.
* **Metodologia:** A estratégia recursiva tenta manter a integridade de parágrafos e frases, dividindo o texto em blocos menores que respeitem a estrutura gramatical. A sobreposição (overlap) de 200 caracteres foi definida para garantir que o contexto não seja perdido em quebras de página ou parágrafos, permitindo que a busca vetorial encontre semelhança sem "cortar" o raciocínio no meio.

## 4. Impacto no RAG
A escolha dessa estratégia de *chunking* impacta diretamente a performance do JARVIS:
* **Precisão de Busca:** Fragmentos de 1000 caracteres oferecem um equilíbrio ideal: são curtos o suficiente para manter a relevância semântica (não misturando muitos tópicos diferentes em um único chunk), mas longos o suficiente para fornecer o contexto necessário para que a LLM (Gemma 12B) consiga formular uma resposta técnica precisa.
* **Eficiência de Recuperação:** Ao alimentar o ChromaDB com estes blocos, garantimos que, ao realizar uma consulta, o sistema recupere chunks altamente específicos para a pergunta, reduzindo o ruído de informações irrelevantes.