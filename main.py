import streamlit as st
import os
import json
import tempfile
import requests
import speech_recognition as sr
# from pydub import AudioSegment
import pandas as pd

# Import functions from other files
from utils.file_upload import upload_files
from utils.writing_style import define_writing_style, load_styles, save_styles
from utils.interview_processing import process_interviews
from utils.book_creation import create_book, create_suggested_chapters, organize_content, save_book
from utils.photo_analysis import analyze_photos

def main():
    st.title("AutoBooker: מערכת אוטומטית ליצירת ספרים מראיונות")

    # Custom CSS for RTL layout and Ctrl+Enter functionality
    st.markdown("""
    <style>
        body {
            direction: rtl;
            text-align: right;
        }
    </style>    
    """, unsafe_allow_html=True)

    menu = ["העלאת קבצים", "הגדרת סגנון כתיבה", "עיבוד ראיונות", "יצירת ספר", "ניתוח תמונות"]
    choice = st.sidebar.selectbox("בחר פעולה", menu)
    
    if choice == "העלאת קבצים":
        file_path = upload_files()
        if file_path:
            st.session_state['file_path'] = file_path
    
    elif choice == "הגדרת סגנון כתיבה":
        styles = define_writing_style()
        st.session_state['styles'] = styles
        
    elif choice == "עיבוד ראיונות":
        if 'file_path' not in st.session_state:
            st.error("נא להעלות קובץ תחילה.")
        else:
            styles = load_styles()
            if not styles:
                st.error("לא נמצאו סגנונות כתיבה. נא להגדיר סגנון כתיבה תחילה.")
            else:
                character_type = st.selectbox("בחר את סגנון הדמות המרואיינת", list(styles.keys()))
                chunk_length = st.slider("בחר אורך קטע (בשניות)", 10, 300, 60)
                if st.button("התחל עיבוד"):
                    st.write(f"מנסה לעבד קובץ: {st.session_state['file_path']}")
                    st.write(f"הקובץ קיים: {os.path.exists(st.session_state['file_path'])}")
                    edited_texts = process_interviews(
                        st.session_state['file_path'],
                        styles,
                        character_type,
                        chunk_length
                    )
                    st.session_state['edited_texts'] = edited_texts
                    st.subheader('הטקסט שתומלל הוא: ' + str(edited_texts))

    elif choice == "יצירת ספר":
        if 'edited_texts' not in st.session_state:
            st.error("נא לעבד ראיונות תחילה.")
        else:
            create_book()
    
    elif choice == "ניתוח תמונות":
        analyze_photos()


if __name__ == "__main__":
    main()