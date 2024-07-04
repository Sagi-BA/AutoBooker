import streamlit as st
import json
import os

DATA_DIR = 'data'
STYLES_FILE = os.path.join(DATA_DIR, 'writing_styles.json')

def load_styles():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    if os.path.exists(STYLES_FILE):
        with open(STYLES_FILE, "r", encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_styles(styles):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    with open(STYLES_FILE, "w", encoding='utf-8') as f:
        json.dump(styles, f, ensure_ascii=False, indent=2)

def define_writing_style():
    st.header("ניהול סגנונות כתיבה")
    
    styles = load_styles()
    
    # תפריט לבחירת פעולה
    action = st.radio("בחר פעולה", ["יצירת סגנון חדש", "עריכת סגנון קיים", "מחיקת סגנון"])
    
    if action == "יצירת סגנון חדש":
        create_new_style(styles)
    elif action == "עריכת סגנון קיים":
        edit_existing_style(styles)
    elif action == "מחיקת סגנון":
        delete_style(styles)
    
    # הצגת כל הסגנונות הקיימים
    st.subheader("סגנונות קיימים")
    for name, data in styles.items():
        st.write(f"**{name}**: {data['description']}")
        if data['example']:
            st.write(f"דוגמה: {data['example']}")
        st.write("---")

    return styles

def create_new_style(styles):
    st.subheader("יצירת סגנון חדש")
    style_name = st.text_input("שם הסגנון")
    style_description = st.text_area("תיאור הסגנון")
    example_text = st.text_area("דוגמה לטקסט בסגנון זה (אופציונלי)")
    
    if st.button("שמור סגנון"):
        if style_name and style_description:
            styles[style_name] = {
                "description": style_description,
                "example": example_text
            }
            save_styles(styles)
            st.success(f"הסגנון '{style_name}' נשמר בהצלחה.")
        else:
            st.warning("נא למלא את שם הסגנון ותיאורו.")

def edit_existing_style(styles):
    st.subheader("עריכת סגנון קיים")
    style_to_edit = st.selectbox("בחר סגנון לעריכה", list(styles.keys()))
    
    if style_to_edit:
        style_description = st.text_area("תיאור הסגנון", value=styles[style_to_edit]["description"])
        example_text = st.text_area("דוגמה לטקסט בסגנון זה", value=styles[style_to_edit]["example"])
        
        if st.button("עדכן סגנון"):
            styles[style_to_edit] = {
                "description": style_description,
                "example": example_text
            }
            save_styles(styles)
            st.success(f"הסגנון '{style_to_edit}' עודכן בהצלחה.")

def delete_style(styles):
    st.subheader("מחיקת סגנון")
    style_to_delete = st.selectbox("בחר סגנון למחיקה", list(styles.keys()))
    
    if style_to_delete:
        if st.button(f"מחק את הסגנון '{style_to_delete}'"):
            del styles[style_to_delete]
            save_styles(styles)
            st.success(f"הסגנון '{style_to_delete}' נמחק בהצלחה.")

if __name__ == "__main__":
    define_writing_style()