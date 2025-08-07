import streamlit as st
import os
import requests
import io

@st.cache_data
def generate_ai_content(topic: str, slides: int):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        st.error("OpenRouter API key is not set.")
        st.stop()
    headers = {"Authorization": f"Bearer {api_key}"}
    prompt = f"Generate {slides * 5} short, informative bullet points for a presentation on the topic: {topic}."
    data = {"model": "openai/gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]}
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to generate content: {e}")
        st.stop()

@st.cache_data
def generate_slide_titles(topic: str, slides: int):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        st.error("OpenRouter API key is not set.")
        st.stop()
    headers = {"Authorization": f"Bearer {api_key}"}
    prompt = f"Generate {slides - 1} engaging, one-line slide titles for a presentation on the topic: '{topic}'. Do not number them. Each title should be on a new line."
    data = {"model": "openai/gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]}
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to generate titles: {e}")
        st.stop()

@st.cache_data
def summarize_paragraph_to_bullets(paragraph: str, slides: int):
    """
    Uses an LLM to convert a paragraph into a specific number of bullet points.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        st.error("OpenRouter API key is not set.")
        st.stop()
    
    headers = {"Authorization": f"Bearer {api_key}"}
    # UPDATED: The prompt now requests a specific number of bullet points.
    num_bullets = slides * 4 # Aim for 4 bullets per slide
    prompt = f"Summarize the following paragraph into exactly {num_bullets} short, informative bullet points. Each bullet point should start with a '-'.\n\nParagraph: \"{paragraph}\""
    
    data = {"model": "openai/gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]}
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to summarize content: {e}")
        st.stop()
@st.cache_data
def extract_titles_from_text(text: str, slides: int):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        st.error("OpenRouter API key is not set.")
        st.stop()
    headers = {"Authorization": f"Bearer {api_key}"}
    prompt = f"Read the following text and extract {slides - 1} potential, engaging, one-line slide titles from it. Each title should be on a new line. Do not number them.\n\nText: \"{text}\""
    data = {"model": "openai/gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]}
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to extract titles: {e}")
        st.stop()

@st.cache_data
def get_image_for_topic(topic: str):
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        return None, None
    headers = {"Authorization": api_key}
    query_params = {"query": topic, "per_page": 1, "orientation": "landscape"}
    try:
        response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=query_params)
        response.raise_for_status()
        data = response.json()
        if data["photos"]:
            photo = data["photos"][0]
            image_url = photo["src"]["medium"]
            photographer_credit = f"Photo by {photo['photographer']} via Pexels"
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            return io.BytesIO(image_response.content), photographer_credit
        return None, None
    except requests.exceptions.RequestException:
        return None, None