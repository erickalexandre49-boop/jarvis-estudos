@echo off
echo Iniciando o Jarvis...
:: Ativa o ambiente virtual
call venv\Scripts\activate
:: Executa o streamlit de forma segura
python -m streamlit run app.py
pause