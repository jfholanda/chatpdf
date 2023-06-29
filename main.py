import streamlit as st
import PyPDF2
import Langchain

from streamlit_extras.add_vertical_space import add_vertical_space

from PyPDF2 import PdfReader

from Langchain.text_splitter import RecursiveCharacterTextSplitter

with st.sidebar:
    st.title("ChatPDF")
    st.markdown(
        """
        ## Sobre
        
        O ChatPDF é uma ferramenta criada com o framework Langchain que permite fazer perguntas sobre o conteúdo de um arquivo PDF.
        
        ### Como utilizar
        
        1. Faça o upload do arquivo PDF utilizando o botão "Browse File".
        2. Faça uma pergunta sobre o PDF.
        
        A aplicação irá analisar o PDF e fornecer uma resposta à sua pergunta com base no conteúdo do arquivo.
        """
    )
    st.write("---")
    st.write("Criado por [João Felipe](https://www.linkedin.com/in/jo%C3%A3o-felipe-holanda-952b4117a/)")

def main():
    st.header("ChatPDF")

    # Importação do PDF
    file = st.file_uploader(label="Faça o upload do seu PDF")

    if file is not None:
        # Lendo o PDF
        pdf_reader = PdfReader(file)

        # Extraindo conteúdo do PDF
        conteudo = ""
        for pagina in pdf_reader.pages:
            conteudo_pagina = pagina.extract_text()

            conteudo += conteudo_pagina

        # Criando os chunks
        


if __name__ == "__main__":
    main()