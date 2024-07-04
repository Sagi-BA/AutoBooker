import streamlit as st
import json

def create_book():
    st.header("יצירת ספר")
    
    # טעינת הטקסטים המעובדים
    try:
        with open("edited_texts.json", "r") as f:
            edited_texts = json.load(f)
    except FileNotFoundError:
        st.error("לא נמצאו טקסטים מעובדים. אנא עבד ראיונות תחילה.")
        return
    
    # יצירת רשימת פרקים מוצעת
    suggested_chapters = create_suggested_chapters(edited_texts)
    
    st.subheader("רשימת פרקים מוצעת")
    chapters = []
    for i, chapter in enumerate(suggested_chapters):
        chapter_name = st.text_input(f"פרק {i+1}", value=chapter)
        chapters.append(chapter_name)
    
    if st.button("אשר רשימת פרקים"):
        organized_content = organize_content(edited_texts, chapters)
        
        st.subheader("תצוגה מקדימה של הספר")
        for chapter, content in organized_content.items():
            st.write(f"**{chapter}**")
            st.write(content)
            st.write("---")
        
        if st.button("שמור ספר"):
            save_book(organized_content)
            st.success("הספר נשמר בהצלחה!")

def create_suggested_chapters(edited_texts):
    # לוגיקה פשוטה ליצירת רשימת פרקים מוצעת
    # ניתן לשפר זאת בעתיד עם אלגוריתמים מתקדמים יותר
    return [f"פרק {i+1}" for i in range(len(edited_texts) // 5)]  # פרק לכל 5 קטעים

def organize_content(edited_texts, chapters):
    organized_content = {chapter: "" for chapter in chapters}
    texts_per_chapter = len(edited_texts) // len(chapters)
    
    for i, chapter in enumerate(chapters):
        start = i * texts_per_chapter
        end = start + texts_per_chapter if i < len(chapters) - 1 else len(edited_texts)
        chapter_texts = [text['text'] for text in edited_texts[start:end]]
        organized_content[chapter] = "\n\n".join(chapter_texts)
    
    return organized_content

def save_book(organized_content):
    with open("final_book.json", "w") as f:
        json.dump(organized_content, f, ensure_ascii=False, indent=2)
