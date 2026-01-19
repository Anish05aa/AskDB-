
import streamlit as st
from app.ai_engine import get_sql_chain

st.set_page_config(page_title="GenAI SQL Assistant")

st.title("🧠 AI Database Assistant")
st.write("Ask questions directly to your MySQL database.")

question = st.text_input("Ask your business question:")

if question:
    with st.spinner("Thinking..."):
        chain = get_sql_chain()
        response = chain.invoke({"query": question})

        raw = response["result"]

        if "Answer:" in raw:
            final_answer = raw.split("Answer:")[-1].strip()
        else:
            final_answer = raw.strip()

        st.subheader("Answer")
        st.write(final_answer)









