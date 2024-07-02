# app.py
import gradio as gr
from loaders.document_loader import load_document
from loaders.text_splitter import split_text
from embeddings.embeddings import get_embeddings
from vectorstore.vectorstore import create_vectorstore, load_vectorstore
from chains.retrieval_chain import create_my_chain
from utils.constants import VECTOR_STORE_DB_PATH
import os
import shutil

def process_document(file):
    # Get the file content from the file object provided by Gradio to local
    file_path = os.path.join("data", os.path.basename(file))
    shutil.copyfile(file.name, file_path)
    
    documents = load_document(file_path)
    text = split_text(documents)
    embeddings = get_embeddings()
    create_vectorstore(text, embeddings)
    return "Document processed and stored in vector database."

def ask_question(question):
    chain = create_my_chain()
    response = chain.invoke({"input": question})
    return response['answer']

def clear_data():
    dirpath = VECTOR_STORE_DB_PATH
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)
        os.makedirs(dirpath)
    return "Vector database cleared."

with gr.Blocks() as demo:
    with gr.Tab("Upload Document"):
        file_input = gr.File(label="Upload your document (PDF, DOCX, TXT)")
        file_output = gr.Textbox(label="Upload Status")
        upload_button = gr.Button("Upload")
        upload_button.click(process_document, inputs=[file_input], outputs=file_output)
    
    with gr.Tab("Ask Question"):
        question_input = gr.Textbox(label="Your question")
        ask_button = gr.Button("Ask")
        answer_output = gr.Textbox(label="Answer")
        ask_button.click(ask_question, inputs=[question_input], outputs=answer_output)
    
    with gr.Tab("Clear"):
        clear_output = gr.Textbox(label="Clear Status")
        clear_button = gr.Button("Clear Data")
        clear_button.click(clear_data, outputs=clear_output)

if __name__ == "__main__":
    demo.launch()
