import streamlit as st


st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)


st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#141E30,#243B55);
}

.title{
    text-align:center;
    color:#00E5FF;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:white;
}

.user{
    background:#007BFF;
    color:white;
    padding:10px;
    border-radius:10px;
    margin:10px 0;
}

.bot{
    background:#1E293B;
    color:white;
    padding:10px;
    border-radius:10px;
    margin:10px 0;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    "<p class='title'>🤖 AI FAQ Chatbot</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Ask Questions About AI & Technology</p>",
    unsafe_allow_html=True
)


with st.sidebar:
    st.header("📌 About")
    st.write("AI FAQ Chatbot")
    st.write("Built using:")
    st.write("✔ Python")
    st.write("✔ Streamlit")
    st.write("✔ NLP Concepts")


faq = {
    "what is ai":
        "Artificial Intelligence enables machines to simulate human intelligence.",

    "what is machine learning":
        "Machine Learning is a subset of AI that learns from data.",

    "what is deep learning":
        "Deep Learning uses neural networks with multiple layers.",

    "what is nlp":
        "NLP stands for Natural Language Processing.",

    "what is computer vision":
        "Computer Vision allows computers to understand images and videos.",

    "what is python":
        "Python is a popular programming language used in AI.",

    "what is codealpha":
        "CodeAlpha provides internship opportunities and project-based learning.",

    "what is data science":
        "Data Science extracts insights from data using statistics and AI.",

    "what is chatbot":
        "A chatbot is a software application that interacts with users through text or voice.",

    "what is neural network":
        "A neural network is a computing system inspired by the human brain."
}


question = st.text_input(
    "💬 Ask Your Question"
)


if st.button("Send 🚀"):

    query = question.lower().strip()

    st.markdown(
        f"<div class='user'>👤 {question}</div>",
        unsafe_allow_html=True
    )

    if query in faq:

        st.markdown(
            f"<div class='bot'>🤖 {faq[query]}</div>",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            "<div class='bot'>🤖 Sorry, I don't know the answer. Please try another question.</div>",
            unsafe_allow_html=True
        )


st.markdown(
    "<br><center style='color:white;'>Developed for CodeAlpha AI Internship</center>",
    unsafe_allow_html=True
)