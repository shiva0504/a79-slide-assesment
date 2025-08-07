import streamlit as st
from dotenv import load_dotenv
import io
import generator
import builder

load_dotenv()

st.set_page_config(page_title="Slide Generator AI", layout="centered")
st.markdown("""<style>div[data-baseweb="select"] > div:first-child {background-color: #FF4B4B;color: white;}[data-baseweb="popover"] ul {background-color: #262730;border: 1px solid #FF4B4B;}li[role="option"]:hover {background-color: #FF4B4B;color: white;}</style>""", unsafe_allow_html=True)
st.title("🤖 Slide Generator AI")

with st.sidebar:
    st.header("⚙️ Configuration")
    
    topic = st.text_input("Enter a topic:", "The Wonders of Ancient Egypt")
    layout = st.selectbox("Layout preference:", ["mixed", "bullet", "two-column", "image", "titles"])
    content_source = st.radio("Choose content source:", ("Generate with AI", "Use my own custom content"))
    
    content_input = ""
    summarize = False
    if content_source == "Use my own custom content":
        label = "Paste your bullet points or titles here (one per line):"
        if layout != 'titles':
            label = "Paste your bullet points or paragraph here:"
        content_input = st.text_area(label, height=200)
        
        if layout != 'titles':
            summarize = st.checkbox("This is a paragraph, summarize it into bullets")

    slides = st.slider("Number of slides:", min_value=2, max_value=20, value=10) # Default to 10
    font = st.selectbox("Select font:", ["Arial", "Calibri", "Times New Roman", "Verdana"])
    
    col1, col2 = st.columns(2)
    with col1:
        title_color = st.color_picker("Title color", "#000000")
    with col2:
        bullet_color = st.color_picker("Bullet color", "#333333")

    uploaded_images = st.file_uploader(
        "Upload Your Own Images (Optional)",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True,
        disabled=(layout == 'titles')
    )
    
    image_streams = []
    if uploaded_images:
        for uploaded_file in uploaded_images:
            image_streams.append(io.BytesIO(uploaded_file.getvalue()))
        st.info(f"✅ {len(image_streams)} image(s) uploaded and ready to use.")

    generate_button = st.button("Generate Presentation", type="primary")

if generate_button:
    if not topic:
        st.error("Please enter a topic.")
    elif content_source == "Use my own custom content" and not content_input:
        st.error("Please paste your custom content.")
    else:
        with st.spinner("Generating your presentation... This may take a moment."):
            try:
                if layout == 'titles':
                    if content_source == 'Generate with AI':
                        content_string = generator.generate_slide_titles(topic, slides)
                    else:
                        content_string = generator.extract_titles_from_text(content_input, slides)
                elif content_source == "Generate with AI":
                    content_string = generator.generate_ai_content(topic, slides)
                else: 
                    if summarize:
                        # UPDATED: Pass the 'slides' variable to the summarizer
                        content_string = generator.summarize_paragraph_to_bullets(content_input, slides)
                    else:
                        content_string = content_input
                
                content_lines = content_string.split("\n")

                presentation_stream = builder.create_presentation(
                    topic, content_lines, slides, layout, font, title_color, bullet_color, image_streams
                )
                
                st.success("Presentation generated successfully! 🎉")
                
                st.download_button(
                    label="Download PowerPoint",
                    data=presentation_stream,
                    file_name=f"{topic.replace(' ', '_').lower()}.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.markdown("Created with Streamlit and `python-pptx`.")