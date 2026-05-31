import streamlit as st
from googletrans import Translator


st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)


st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
}

/* Main Title */
.title {
    text-align: center;
    color: #00E5FF;
    font-size: 45px;
    font-weight: bold;
    text-shadow: 2px 2px 10px black;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: white;
    font-size: 18px;
}

/* Labels */
label {
    color: white !important;
    font-weight: bold;
}

/* Text Area */
textarea {
    background-color: #1E293B !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #00E5FF, #007BFF);
    color: white;
    border: none;
    border-radius: 12px;
    height: 50px;
    width: 220px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #007BFF, #00E5FF);
}

/* Footer */
.footer {
    text-align: center;
    color: #d1d5db;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    "<p class='title'>🌍 AI Language Translator</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Translate Text Between Multiple Languages</p>",
    unsafe_allow_html=True
)


with st.sidebar:
    st.title("📌 About Project")
    st.write("AI Language Translator")
    st.write("")
    st.write("### Technologies Used")
    st.write("✔ Python")
    st.write("✔ Streamlit")
    st.write("✔ Googletrans")
    st.write("✔ NLP")


translator = Translator()


languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}


text = st.text_area(
    "✍ Enter Text",
    height=150
)


col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "🌐 Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "🎯 Target Language",
        list(languages.keys())
    )


if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("Please enter text.")
    else:
        try:
            translated = translator.translate(
                text,
                src=languages[source_lang],
                dest=languages[target_lang]
            )

            st.success("Translation Successful ✅")

            st.text_area(
                "📄 Translated Text",
                translated.text,
                height=150
            )

        except Exception as e:
            st.error(f"Error: {e}")


st.markdown(
    "<p class='footer'>Developed for CodeAlpha AI Internship</p>",
    unsafe_allow_html=True
)