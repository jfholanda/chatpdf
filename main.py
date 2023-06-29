import streamlit as st
import PyPDF2
import langchain
import pickle
import os

from dotenv import load_dotenv 

from streamlit_extras.add_vertical_space import add_vertical_space

from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI 
from langchain.chains.question_answering import load_qa_chain

load_dotenv()

# API Key da OpenAI
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

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
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )
        chunks = text_splitter.split_text(conteudo)

        # Verificando a existência do vetor semântico
        filename = file.name[:-4]
        if os.path.exists(f"{filename}.pkl"):
            with open(file=f"{filename}.pkl", mode='rb') as pdf_file:
                vectorstore = pickle.load(pdf_file)
        else:
            embedding = OpenAIEmbeddings()
            vectorstore = FAISS.from_texts(texts=chunks, embedding=embedding)
            with open(file=f"{filename}.pkl", mode='wb') as pdf_file:
                pickle.dump(vectorstore, pdf_file)

        # Recebendo pergunta
        pergunta = st.text_input(label="Faça uma pergunta")

        if pergunta:
            paginas_semanticas = vectorstore.similarity_search(query=pergunta)

            llm = OpenAI(temperature=0, model_name = "gpt-3.5-turbo")
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            resposta = chain.run(input_documents=paginas_semanticas, 
            question=pergunta)

            st.write(resposta)

if __name__ == "__main__":
    main()