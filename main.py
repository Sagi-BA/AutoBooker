import streamlit as st
import os
from utils.gradio_client_wrapper import GradioClientWrapper
from utils.file_upload import upload_files
from utils.writing_style import define_writing_style, load_styles
from utils.interview_processing import process_interviews
from utils.book_creation import create_book
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
        file_paths = upload_files()
        if file_paths:
            st.session_state['file_paths'] = file_paths
    
    elif choice == "הגדרת סגנון כתיבה":
        styles = define_writing_style()
        st.session_state['styles'] = styles
        
    elif choice == "עיבוד ראיונות":
        if 'file_paths' not in st.session_state:
            st.error("נא להעלות קבצים תחילה.")
        else:
            styles = load_styles()
            if not styles:
                st.error("לא נמצאו סגנונות כתיבה. נא להגדיר סגנון כתיבה תחילה.")
            else:
                character_type = st.selectbox("בחר את סגנון הדמות המרואיינת", list(styles.keys()))
                # chunk_length = st.slider("בחר אורך קטע (בדקות)", 10, 300, 25)
                if st.button("התחל עיבוד"):
                    st.write(f"מנסה לעבד קבצים: {st.session_state['file_paths']}")
                    edited_texts = process_interviews(
                        st.session_state['file_paths'],
                        styles,
                        character_type
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
