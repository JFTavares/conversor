# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    pandoc \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de requisitos
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY app.py .

# Criar diretório para uploads temporários
RUN mkdir -p /tmp/streamlit_uploads

# Expor porta do Streamlit
EXPOSE 8501

# Configurar variáveis de ambiente do Streamlit
ENV STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
ENV STREAMLIT_SERVER_ENABLE_CORS=false
ENV STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false

# Comando para executar a aplicação
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true"]