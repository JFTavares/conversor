# 📚 EPUB para Word Converter

Uma interface web simples e intuitiva para converter arquivos EPUB para formato Microsoft Word (.docx) usando Streamlit e Pandoc.

![Interface Preview](https://img.shields.io/badge/Interface-Streamlit-red?style=flat-square)
![Converter](https://img.shields.io/badge/Converter-Pandoc-blue?style=flat-square)
![Docker](https://img.shields.io/badge/Deploy-Docker-blue?style=flat-square)

## ✨ Características

- **Interface Intuitiva**: Área de arrastar e soltar para upload de arquivos
- **Conversão Rápida**: Powered by Pandoc para conversões de alta qualidade
- **Download Direto**: Baixe o arquivo convertido diretamente pelo navegador
- **Dockerizado**: Deploy fácil com Docker e Docker Compose
- **Responsive**: Interface adaptável para desktop e mobile

## 🚀 Execução Rápida com Docker

### Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 1. Clone ou crie os arquivos
Certifique-se de ter todos os arquivos em um diretório:
```
epub-converter/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

### 2. Execute com Docker Compose
```bash
# Navegue até o diretório do projeto
cd epub-converter

# Execute a aplicação
docker-compose up -d

# Para ver os logs
docker-compose logs -f
```

### 3. Acesse a aplicação
Abra seu navegador em: **http://localhost:8501**

## 🔧 Instalação Local

### Pré-requisitos
- Python 3.8 ou superior
- [Pandoc](https://pandoc.org/installing.html)

### Instalação do Pandoc

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install pandoc
```

**macOS:**
```bash
brew install pandoc
```

**Windows:**
- Baixe o instalador em: https://pandoc.org/installing.html

### Instalação Python
```bash
# Clone ou baixe os arquivos do projeto
cd epub-converter

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py
```

## 📖 Como Usar

1. **Carregue o arquivo EPUB**
   - Arraste e solte um arquivo .epub na área indicada
   - Ou clique para selecionar o arquivo

2. **Defina o nome de saída**
   - Digite o nome desejado para o arquivo Word
   - A extensão .docx será adicionada automaticamente

3. **Converta**
   - Clique em "Converter para Word"
   - Aguarde o processamento

4. **Baixe**
   - Clique em "Baixar arquivo Word" quando a conversão estiver completa

## 🐳 Comandos Docker Úteis

```bash
# Construir apenas a imagem
docker build -t epub-converter .

# Executar sem docker-compose
docker run -p 8501:8501 epub-converter

# Parar os serviços
docker-compose down

# Reconstruir e executar
docker-compose up --build -d

# Ver logs em tempo real
docker-compose logs -f epub-converter
```

## 🔍 Solução de Problemas

### Pandoc não encontrado
Se você ver a mensagem "❌ Pandoc não encontrado":
- **Docker**: Reconstrua a imagem com `docker-compose up --build`
- **Local**: Instale o Pandoc seguindo as instruções acima

### Erro de conversão
- Verifique se o arquivo EPUB não está corrompido
- Certifique-se de que o arquivo é um EPUB válido
- Tente com um arquivo menor para testes

### Porta já em uso
Se a porta 8501 estiver ocupada:
```yaml
# No docker-compose.yml, altere:
ports:
  - "8502:8501"  # Use outra porta local
```

## 🛠️ Personalização

### Alterar tamanho máximo de upload
No `Dockerfile`, modifique:
```dockerfile
ENV STREAMLIT_SERVER_MAX_UPLOAD_SIZE=500  # 500MB
```

### Adicionar novos formatos
Modifique o `app.py` para aceitar outros formatos de entrada:
```python
type=['epub', 'mobi', 'azw3']  # Adicione outros formatos
```

## 📁 Estrutura do Projeto

```
epub-converter/
├── app.py              # Aplicação Streamlit principal
├── requirements.txt    # Dependências Python
├── Dockerfile         # Configuração do container
├── docker-compose.yml # Orquestração Docker
├── .dockerignore      # Arquivos ignorados no build
└── README.md         # Esta documentação
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- [Streamlit](https://streamlit.io/) - Framework para aplicações web em Python
- [Pandoc](https://pandoc.org/) - Conversor universal de documentos
- [Docker](https://www.docker.com/) - Platform de containerização

---

**Desenvolvido com ❤️ usando Streamlit e Pandoc**