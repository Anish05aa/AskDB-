import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_experimental.sql import SQLDatabaseChain

from app.examples import QUERY_EXAMPLES

load_dotenv()

def get_sql_chain():
    # DB
    db = SQLDatabase.from_uri(
        "mysql+pymysql://root:root@localhost/atliq_tshirts",
        include_tables=["t_shirts"],
        sample_rows_in_table_info=3
    )

    # Groq LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )

    # Embeddings for few-shot selection
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    texts = [ex["input"] + ex["query"] for ex in QUERY_EXAMPLES]

    vectorstore = Chroma.from_texts(texts, embeddings, metadatas=QUERY_EXAMPLES)

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2
    )

    # Prompt (adapted from your original)
    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results and return the final answer.

Use the format:

Question: ...
SQLQuery: ...
SQLResult: ...
Answer: ...
"""

    example_prompt = PromptTemplate(
        input_variables=["input"],
        template="Question: {input}\nSQLQuery:"
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix="""
    Question: {input}
    SQLQuery:
    SQLResult:
    Answer (only the final answer, no SQL, no extra text):
    """,
        input_variables=["input"],
    )

    chain = SQLDatabaseChain.from_llm(
        llm,
        db,
        verbose=False,
        prompt=few_shot_prompt,
        return_intermediate_steps=False,
        output_key="result"
    )

    return chain
