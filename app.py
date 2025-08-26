import streamlit as st
import subprocess
import os
import tempfile
from pathlib import Path
import shutil

def convert_epub_to_docx(epub_file, output_name):
    """
    Converte arquivo EPUB para DOCX usando pandoc
    """
    try:
        # Criar diretório temporário
        with tempfile.TemporaryDirectory() as temp_dir:
            # Salvar arquivo EPUB temporariamente
            epub_path = os.path.join(temp_dir, "input.epub")
            with open(epub_path, "wb") as f:
                f.write(epub_file.getvalue())
            
            # Definir caminho de saída
            docx_path = os.path.join(temp_dir, f"{output_name}.docx")
            
            # Executar pandoc
            cmd = [
                "pandoc",
                epub_path,
                "-o", docx_path,
                "--extract-media", os.path.join(temp_dir, "media")
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Ler arquivo convertido
                with open(docx_path, "rb") as f:
                    return f.read(), None
            else:
                return None, f"Erro na conversão: {result.stderr}"
                
    except Exception as e:
        return None, f"Erro: {str(e)}"


def main():
    st.set_page_config(
        page_title="Conversor de EPUB para Word",
        page_icon="images/icon.png",
        layout="centered"
    )

    image_path = Path(__file__).parent / "images" / "booknando.png"

    if image_path.exists():
        st.image(str(image_path), width=200)
    else:
        st.text("by Booknando")

    st.markdown(
        "<h1 style='font-size:18px;'>Conversor de EPUB para Word</h1>", unsafe_allow_html=True
    )

    # Verificar se pandoc está instalado
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
        pandoc_status = "✅ Pandoc instalado e funcionando"
        pandoc_color = "green"
    except (subprocess.CalledProcessError, FileNotFoundError):
        pandoc_status = "❌ Pandoc não encontrado - instale o pandoc para usar este conversor"
        pandoc_color = "red"

    st.markdown(f"<p style='color: {pandoc_color}; font-size: 14px;'>{pandoc_status}</p>",
                unsafe_allow_html=True)

    st.markdown("---")

    # Upload de arquivo
    uploaded_file = st.file_uploader(
        "**Arraste e solte seu arquivo EPUB aqui ou clique para selecionar:**",
        type=['epub'],
        help="Selecione um arquivo EPUB para converter para Word"
    )

    if uploaded_file is not None:
        # Mostrar informações do arquivo
        st.success(f"Arquivo carregado: **{uploaded_file.name}**")

        file_size = len(uploaded_file.getvalue())
      #  st.info(f"Tamanho do arquivo: {file_size / 1024:.2f} KB")

        # Nome do arquivo de saída
        default_name = Path(uploaded_file.name).stem
        output_name = default_name
        # output_name = st.text_input(
        #     "**Nome do arquivo de saída (sem extensão):**",
        #     value=default_name,
        #     help="O arquivo será salvo como .docx"
        # )

        # Conversão automática
        if output_name:  # Só converte se houver um nome válido
            # Mostrar progresso
            progress_bar = st.progress(0)
            status_text = st.empty()

            status_text.text("📖 Iniciando conversão automática...")
            progress_bar.progress(25)

            # Realizar conversão
            docx_data, error = convert_epub_to_docx(uploaded_file, output_name)

            if error:
                progress_bar.empty()
                status_text.empty()
                st.error(f"❌ {error}")
            else:
                status_text.text("✅ Conversão concluída!")
                progress_bar.progress(100)

                # Botão de download
                st.success("Conversão realizada com sucesso!")

                st.download_button(
                    label="Baixar arquivo Word",
                    data=docx_data,
                    file_name=f"{output_name}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )

                # Limpar barra de progresso após sucesso
                progress_bar.empty()
                status_text.empty()
        else:
            st.warning("⚠️ Insira um nome válido para o arquivo de saída.")

    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #666; font-size: 12px;'>"
        "Powered by Booknando</p>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()