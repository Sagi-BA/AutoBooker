from dotenv import load_dotenv
import streamlit as st
from moviepy.editor import AudioFileClip
import json
import os
from groq import Groq
from faster_whisper import WhisperModel  

from utils.groq_translation import groq_translate  

# Load environment variables
load_dotenv()

# Load whisper model
model = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=int(os.cpu_count() / 2)) 

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# Define the path for the temporary audio files
TEMP_AUDIO_DIR = os.path.join(os.getcwd(), "temp_audio")

# Ensure the temporary directory exists
if not os.path.exists(TEMP_AUDIO_DIR):
    os.makedirs(TEMP_AUDIO_DIR)

def speech_to_text(audio_chunk):    
        segments, info = model.transcribe(audio_chunk, beam_size=5) 
        speech_text = " ".join([segment.text for segment in segments]) 
        return speech_text    

def process_interviews(file_path, styles, character_type, chunk_length):
    st.header("עיבוד ראיונות")    
    st.info(f"מנסה לעבד קובץ: {file_path}")
    st.info(f"הקובץ קיים: {os.path.exists(file_path)}")
    
    if not os.path.exists(file_path):
        st.error(f"הקובץ לא נמצא: {file_path}")
        return [], []
    
    try:
        with st.spinner('Transcribing...'):          
            speech_text = speech_to_text(file_path)
            print(speech_text)
            st.info("הקובץ תומלל מקול לטקסט STT!")

        with st.spinner('Groq LLM...'):
            translation = groq_translate(speech_text, 'he', 'he') 
            print(translation)
            st.info("מעבד את הקובץ בעזרת מודל שפה LLM!")
        
        st.success("עיבוד הראיונות הושלם בהצלחה!")

        return translation
    
    except Exception as e:
        st.error(f"שגיאה בעיבוד קובץ האודיו: {str(e)}")
        return ""
    
def edit_text(text, style, character_type):
    # Here you should add logic to edit the text according to the style and character type
    # For now, we'll just add a simple description
    print(text)
    print(style)
    style_description = style.get('description', 'סגנון לא מוגדר')
    return f"{style_description}: {text} (דמות: {character_type})"

def save_results(data, filename):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":

    # This is for testing purposes. In the actual app, this function will be called from main.py
    st.write("This is a test run of the interview processing module.")
    # You would need to provide actual values for these parameters in a real run
    file_path = os.path.join("uploads", "iris bar on_small.mp3")
    process_interviews(file_path, {"some_style": {"description": "Test style"}}, "Test character", 60)
