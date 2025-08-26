#!/bin/bash

# Script de inicialização para EPUB to Word Converter

echo "🚀 Iniciando EPUB para Word Converter..."

# Verificar se o Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não encontrado. Por favor, instale o Docker primeiro."
    echo "   Visite: https://docs.docker.com/get-docker/"
    exit 1
fi

# Verificar se o docker-compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose não encontrado. Por favor, instale o Docker Compose primeiro."
    echo "   Visite: https://docs.docker.com/compose/install/"
    exit 1
fi

# Verificar se os arquivos necessários existem
required_files=("app.py" "requirements.txt" "Dockerfile" "docker-compose.yml")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Arquivo $file não encontrado!"
        echo "   Certifique-se de que todos os arquivos estão no diretório atual."
        exit 1
    fi
done

echo "✅ Verificações concluídas!"

# Parar containers existentes (se houver)
echo "🛑 Parando containers existentes..."
docker-compose down 2>/dev/null

# Construir e executar
echo "🔨 Construindo e iniciando a aplicação..."
docker-compose up -d

# Verificar se o container está rodando
if [ $? -eq 0 ]; then
    echo "✅ Aplicação iniciada com sucesso!"
    echo ""
    echo "🌐 Acesse a aplicação em: http://localhost:8501"
    echo ""
    echo "📋 Comandos úteis:"
    echo "   Ver logs:          docker-compose logs -f"
    echo "   Parar aplicação:   docker-compose down"
    echo "   Reiniciar:         docker-compose restart"
    echo ""
else
    echo "❌ Erro ao iniciar a aplicação!"
    echo "   Execute 'docker-compose logs' para ver os detalhes do erro."
    exit 1
fi