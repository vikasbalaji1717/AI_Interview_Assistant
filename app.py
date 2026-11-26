import streamlit as st
from groq import Groq
st.set_page_config(page_title='AI Interview Assistant', layout='centered')
st.title(' AI Interview Assistant')
st.caption('Practice interviews with AI-generated questions and constructive feedback.')
st.caption(' lanchued by VIKAS')
st.write('department of AI&DS')
try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection successful")
except (keyError, FileNotFoundError):
  st.error('GROQ_API_KEY is missing. Add it to Streamlit Cloud - App setting')
  st.stop() 
import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Interview Assistant")

role = st.selectbox(
    "Select Job Role",
    [
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Machine Learning Engineer",
        "Software Engineer",
        "HR Executive",
    ],
)
diff = st.selectbox("Select Difficulty level", [
  "Beginner",
  "Advance",
  "pro"
])
if st.button("Generate Interview Questions"):
    prompt = f"Generate 5 interview questions for the role of {role}."

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are an expert technical interviewer.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    output = response.choices[0].message.content
    st.write(output)
