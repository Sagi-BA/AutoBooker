import streamlit as st
import pandas as pd
import json

def analyze_photos():
    st.header("ניתוח תמונות")
    
    uploaded_file = st.file_uploader("העלה קובץ CSV עם פרטי התמונות", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        
        try:
            with open("final_book.json", "r") as f:
                book_content = json.load(f)
        except FileNotFoundError:
            st.error("לא נמצא ספר מאורגן. אנא צור ספר תחילה.")
            return
        
        analyzed_photos = analyze_and_match_photos(df, book_content)
        
        st.subheader("תוצאות ניתוח התמונות")
        st.write(analyzed_photos)
        
        if st.button("שמור תוצאות ניתוח"):
            save_photo_analysis(analyzed_photos)
            st.success("תוצאות הניתוח נשמרו בהצלחה!")

def analyze_and_match_photos(photos_df, book_content):
    analyzed_photos = []
    for _, photo in photos_df.iterrows():
        best_match = find_best_match(photo, book_content)
        analyzed_photos.append({
            "image_number": photo["מספר תמונה"],
            "who": photo["מי"],
            "when": photo["מתי"],
            "what": photo["מה"],
            "where": photo["איפה"],
            "suggested_chapter": best_match["chapter"],
            "suggested_context": best_match["context"]
        })
    return pd.DataFrame(analyzed_photos)

def find_best_match(photo, book_content):
    best_match = {"chapter": "", "context": "", "score": 0}
    for chapter, content in book_content.items():
        score = sum(word.lower() in content.lower() for word in str(photo["מי"]).split() + 
                    str(photo["מה"]).split() + str(photo["איפה"]).split())
        if score > best_match["score"]:
            best_match = {
                "chapter": chapter,
                "context": content[:100] + "...",  # רק 100 תווים ראשונים להקשר
                "score": score
            }
    return best_match

def save_photo_analysis(analyzed_photos):
    analyzed_photos.to_csv("analyzed_photos.csv", index=False)