import streamlit as st

from streamlit_extras.add_vertical_space import add_vertical_space

with st.sidebar:
    st.title("ChatPDF")
    st.markdown(
        """
        ## Sobre
        
        O ChatPDF é uma ferramenta criada com o framework Langchain que permite fazer perguntas sobre o conteúdo de um arquivo PDF.
        
        ### Como utilizar
        
        1. Faça o upload do arquivo PDF utilizando o botão "Selecionar arquivo".
        2. Digite sua pergunta na caixa de texto.
        
        A aplicação irá analisar o PDF e fornecer uma resposta à sua pergunta com base no conteúdo do arquivo.
        """
    )
    st.write("---")
    st.write("Criado por [João Felipe](https://www.linkedin.com/in/jo%C3%A3o-felipe-holanda-952b4117a/)")