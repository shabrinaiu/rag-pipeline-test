# Preprocess Data
from typing import List
from utils.types import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pandas as pd


def load_dataset() -> List[Document]:
    df = pd.read_excel(
        "./data/raw/TheHackerNews_Dataset.xlsx"
    )  # Replace with your actual file

    documents = [
        Document(
            page_content=row["Article"],
            metadata={
                "title": row["Title"],
                "link": row["Link"],
                "label": row["Label"],
            },
        )
        for _, row in df.iterrows()
    ]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200, chunk_overlap=50, separators=["\n\n", "\n", ".", "!", "?", " "]
    )

    return text_splitter.split_documents(documents)
