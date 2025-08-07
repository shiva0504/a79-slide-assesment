# 🤖 Slide Generator AI

This project is a web application built with **Streamlit** and **Python** that automatically generates PowerPoint presentations on any given topic. It uses **Large Language Models (LLMs)** for content creation and can incorporate images to create professional-looking slides quickly.

The application provides a simple, interactive web interface where users can specify a topic, choose from various layouts, customize styling, and even upload their own images.


## ✨ Features

- **AI-Powered Content**: Generates relevant bullet points or slide titles for any topic.
- **Custom Content Input**: Allows users to paste their own text (paragraphs or pre-formatted bullets) to create presentations.
- **Intelligent Text Processing**: Can summarize paragraphs into bullet points or extract key titles from a block of text.
- **Multiple Slide Layouts**: Supports various slide layouts, including single-column (`bullet`), two-column, text-with-image, and titles-only.
- **Custom Styling**: Users can customize fonts and colors for titles and body text using interactive widgets.
- **User Image Uploads**: Allows users to upload their own images to be used in the presentation. The app intelligently prioritizes these images.
- **Local File Saving**: Automatically saves a copy of every generated presentation to a `sample_presentations` folder for your records.

---

## 📂 Directory Structure

```
slide-generator-project/
├── .streamlit/
│   └── config.toml         # Streamlit theme configuration
├── .env                    # Stores secret API keys
├── builder.py              # Code to build the PowerPoint file
├── generator.py            # Code for all AI and image API calls
├── requirements.txt        # Project dependencies
└── streamlit_app.py        # The main file to run the web application
```

---

## 🚀 Setup Instructions

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

- Python 3.8+
- `pip` package manager

### 2. Get the Code

Clone the repository or download and place all the project files into a single project folder.

### 3. Create a Virtual Environment

It's highly recommended to use a virtual environment.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# Activate it (Windows)
.\venv\Scripts\activate
```

### 4. Install Dependencies

Install all required Python libraries:

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the root of your project directory. This file stores your secret API keys:

```env
OPENROUTER_API_KEY="your_openrouter_api_key_here"
PEXELS_API_KEY="your_pexels_api_key_here"
```

- **OpenRouter Key**: Obtain from [OpenRouter.ai](https://openrouter.ai/).
- **Pexels Key**: Obtain from [Pexels API](https://www.pexels.com/api/).

### 6. Run the Streamlit Application

Use the following command:

```bash
streamlit run streamlit_app.py
```

A new browser tab will open with the running application.

---

## 🖥️ How to Use

1. **Open the App**  
   Once running, it opens in your browser.

2. **Configure Slides** using the sidebar:
   - Enter a **Topic**
   - Choose a **Layout** (Bullet, Two-Column, Image, Title)
   - Select **Content Source** (AI-generated or paste your own)
   - Set the **Number of Slides**
   - Customize **Fonts** and **Colors**
   - Optionally **Upload Your Own Images**

3. **Generate Presentation**  
   Click the **Generate Presentation** button.

4. **Download the File**  
   After generation:
   - Click **Download PowerPoint**
   - A copy is also saved to the `sample_presentations` folder
