import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "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"

# Function to generate text using the OpenAI API
def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Streamlit app title
st.title("OpenAI Text Generation")

# Input box for user prompt
prompt = st.text_area("Enter your prompt")

# Button to generate text
if st.button("Generate Text"):
    with st.spinner("Generating text..."):
        generated_text = generate_text(prompt)
        st.text_area("Generated Text", generated_text)
