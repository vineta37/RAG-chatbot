# src/scripts/env_check.py
import sys
import importlib

print("Python:", sys.version.replace("\n", " "))

packages = {
    "langchain": "langchain",
    "chromadb": "chromadb",
    "streamlit": "streamlit",
    "PyPDF2": "PyPDF2",
    "openai": "openai",
    "sentence_transformers": "sentence_transformers",
}

for name, modname in packages.items():
    try:
        m = importlib.import_module(modname)
        ver = getattr(m, "__version__", "unknown")
        print(f"{name}: OK (version {ver})")
    except Exception as e:
        print(f"{name}: FAILED to import ({e})")
