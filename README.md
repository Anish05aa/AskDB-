
# 🧠 AskDB – GenAI SQL Assistant

AskDB is a **GenAI-powered SQL Assistant** that allows users to ask natural language questions and get answers directly from a MySQL database.
It uses **LLMs (Groq + Llama 3), LangChain, semantic search, and Streamlit UI** to convert questions into SQL queries and return meaningful results.

---

## 🚀 Features

* 🔹 Ask questions in plain English
* 🔹 Automatically generates SQL queries using LLM
* 🔹 Executes queries on MySQL database
* 🔹 Returns human-readable answers
* 🔹 Few-shot prompting with semantic example selection
* 🔹 Clean UI built using Streamlit
* 🔹 Secure environment variable handling

Example:

> **User:** What is the total inventory value for small size t-shirts?
> **System:** Returns calculated result directly from database

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** – Frontend UI
* **LangChain** – LLM orchestration
* **Groq (Llama 3.1)** – LLM inference
* **MySQL** – Database
* **ChromaDB** – Vector store for semantic example selection
* **HuggingFace Embeddings**
* **SQLAlchemy + PyMySQL**
* **dotenv** – Environment management

---

## 📂 Project Structure

```
askDB/
│
├── app/
│   ├── main.py            # Streamlit UI
│   ├── ai_engine.py       # LangChain + LLM + SQL logic
│   ├── examples.py        # Few-shot examples
│   ├── prompts.py         # Prompt templates
│   └── db.py              # Database helpers
│
├── database/
│   └── db_creation_atliq_tshirts.sql
│
├── .env                   # Environment variables (ignored)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Anish05aa/AskDB.git
cd AskDB
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

Create a file named `.env` in the root folder:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🗄️ Database Setup

1. Start MySQL server
2. Create database:

```sql
CREATE DATABASE atliq_tshirts;
```

3. Import schema:

```sql
SOURCE database/db_creation_atliq_tshirts.sql;
```

---

## ▶️ Run the App

```bash
streamlit run app/main.py
```

Then open:

```
http://localhost:8501
```

---

## 📸 Sample Questions You Can Ask

* What is the total inventory value for size M?
* How many black t-shirts are available?
* Which brand has the highest stock?
* Show total stock grouped by size
* What is the average price per brand?




## 👤 Author

**Anish Anand**

* GitHub: [https://github.com/Anish05aa](https://github.com/Anish05aa)
* Role: Full Stack Developer (MERN + GenAI)
* Focus: AI-integrated real-world applications

---

