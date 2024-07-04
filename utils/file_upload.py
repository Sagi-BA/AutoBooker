import streamlit as st
import os
import requests

UPLOAD_DIR = 'uploads'

def upload_files():
    st.header("העלאת קבצי אודיו/וידאו")
    
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    upload_option = st.radio("בחר אפשרות העלאה", ["קובץ מקומי", "קישור לענן"])
    
    if upload_option == "קובץ מקומי":
        uploaded_file = st.file_uploader("בחר קובץ אודיו או וידאו", type=["mp3", "wav", "mp4"])
        if uploaded_file is not None:
            file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"הקובץ {uploaded_file.name} הועלה בהצלחה.")
            return file_path
    
    else:  # קישור לענן
        cloud_link = st.text_input("הכנס קישור לקובץ בענן")
        if cloud_link and st.button("הורד קובץ"):
            try:
                response = requests.get(cloud_link)
                if response.status_code == 200:
                    file_name = os.path.basename(cloud_link)
                    file_path = os.path.join(UPLOAD_DIR, file_name)
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    st.success("הקובץ הורד בהצלחה מהענן.")
                    return file_path
                else:
                    st.error("לא ניתן להוריד את הקובץ. אנא בדוק את הקישור.")
            except Exception as e:
                st.error(f"אירעה שגיאה: {str(e)}")
    
    return None