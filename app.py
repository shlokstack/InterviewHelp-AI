import streamlit as st
from langchain_groq  import ChatGroq
from langchain_core.prompts import PromptTemplate
from prompts import template
from dotenv import load_dotenv
import os
load_dotenv()

st.set_page_config(
    page_title="InterviewHelp AI"
)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0.5
)

# Prompt to be given to the model 
prompt = PromptTemplate(
    input_variables=["skills","domain","experience"],
    template=template
)
# Sidebar for better webpage format
with st.sidebar:
    st.title("🎓 InterviewHelp AI")
    skills = st.text_area("Enter your skills...", placeholder="Python, SQL, Machine Learning, Git...")
    domain = st.selectbox("Enter your domain... (Type if not listed)", options=["Gen AI", "AI/ML", "Full stack", "Cloud", "DBMS"], accept_new_options=True)
    experience = st.slider("Experience level", min_value=1, max_value=5, help="1 = Beginner, 5 = Expert")
    generate = st.button("Generate response")
if generate:
    if not skills.strip():
        st.warning("Please enter your skills.")
        st.stop()
    final_prompt = prompt.format(
        skills = skills,
        domain = domain,
        experience  = experience
        )
    with st.spinner("Thinking..."):
        response = llm.invoke(final_prompt)
        st.markdown(response.content)
    st.balloons()