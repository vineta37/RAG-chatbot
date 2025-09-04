# src/app.py
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # set in .env

st.title("Simple RAG Chatbot - Demo")

if "index" not in st.session_state:
    st.session_state.index = None

st.sidebar.header("Indexing")
uploaded = st.sidebar.file_uploader("Upload PDF to index", type=["pdf"], accept_multiple_files=True)

if st.sidebar.button("Build / Rebuild Index"):
    from langchain.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import Chroma

    docs = []
    for f in uploaded:
        # save temporarily
        tmp_path = os.path.join("data", f.name)
        with open(tmp_path, "wb") as out:
            out.write(f.getbuffer())
        loader = PyPDFLoader(tmp_path)
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    docs = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectordb = Chroma.from_documents(docs, embeddings)  # in-memory by default
    st.session_state.index = vectordb
    st.sidebar.success("Index built!")

st.header("Ask a question")
query = st.text_input("Enter your question:")

if query and st.sidebar.button("Run Query"):
    if not st.session_state.index:
        st.warning("First build an index in the sidebar (upload PDFs and click Build).")
    else:
        from langchain.chains import RetrievalQA
        from langchain.llms import OpenAI

        retriever = st.session_state.index.as_retriever(search_kwargs={"k": 3})
        llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
        answer = qa.run(query)
        st.subheader("Answer")
        st.write(answer)
