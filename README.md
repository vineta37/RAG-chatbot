# RAG-chatbot
A Retrieval-Augmented Generation (RAG) powered chatbot that allows you to upload PDFs, build an index, and ask natural language questions answered from your documents. 
Built with Streamlit, LangChain, and ChromaDB.

## Project Outline
RAG-CHATBOT/
│── .venv/ # Virtual environment
│── src/
│ ├── app.py # Main Streamlit app
│ └── scripts/
│ └── env_check.py # Environment check script
│── data/ # Uploaded documents (PDFs)
│── .env # Environment variables
│── .gitignore
│── README.md

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate     

# Install dependencies
pip install langchain chromadb openai sentence-transformers streamlit PyPDF2 python-dotenv tiktoken faiss-cpu

# Check environment
python src/scripts/env_check.py

# Run the app
streamlit run src/app.py 
Local URL: http://localhost:8501
Network URL: http://192.168.1.7:8501
