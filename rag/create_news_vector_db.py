from tools.save_news import write_news_file
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
import shutil
from langsmith import traceable
import logging

logger=logging.getLogger(__name__)
load_dotenv()

@traceable
def create_vector_db(file_path : str):

    if file_path is None:
        return None

    current_path=os.path.dirname(__file__)
    persistent_db_path=os.path.join(current_path,"db")
    archive_path=os.path.join(current_path,"documents","archive")

    try:

        loader=TextLoader(file_path)
        documents=loader.load()

        text_splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=50)
        docs=text_splitter.split_documents(documents)
        embeddings=OpenAIEmbeddings(model="text-embedding-3-small")
        if os.path.exists(persistent_db_path):
            db = Chroma(
                persist_directory=persistent_db_path,
                embedding_function=embeddings
            )
            db.add_documents(docs)   # append new docs
        else:
            db = Chroma.from_documents(
                docs,
                embeddings,
                persist_directory=persistent_db_path
            )
        
        dest_path = os.path.join(archive_path, os.path.basename(file_path))
        shutil.move(file_path, dest_path)
    except Exception as e:
        logger.error(f"Exception occured..{e}")
    return db