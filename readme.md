![Alt text](https://i.imgur.com/RhRQLLN.jpg)

# 👀 AutoBooker: מערכת אוטומטית ליצירת ספרים מראיונות

Demo url = https://autobooker.streamlit.app/

AutoBooker היא מערכת המאפשרת יצירה אוטומטית של ספרים מראיונות מוקלטים. המערכת מתמללת ראיונות, מעבדת את הטקסט לפי סגנונות כתיבה מוגדרים, ומארגנת את התוכן לספר קוהרנטי.

[![Support](https://img.shields.io/badge/linktree-white?style=for-the-badge&logo=linktree&logoColor=43E55E)](https://linktr.ee/sagib?lt_utm_source=lt_share_link#373198503)
[![Support](https://img.shields.io/badge/Buy_Me_A_Coffee-white?style=for-the-badge&logo=buymeacoffee&logoColor=FFDD00)](https://buymeacoffee.com/sagibar)
[![Support](https://img.shields.io/badge/linkedin-white?style=for-the-badge&logo=linkedin&logoColor=0A66C2)](https://www.linkedin.com/in/sagi-bar-on)
[![Support](https://img.shields.io/badge/whatsapp-white?style=for-the-badge&logo=whatsapp&logoColor=25D366)](https://api.whatsapp.com/send?phone=972549995050)
[![Support](https://img.shields.io/badge/facebook-white?style=for-the-badge&logo=facebook&logoColor=0866FF)](https://www.facebook.com/sagi.baron)
[![Support](https://img.shields.io/badge/email_me-white?style=for-the-badge&logo=gmail&logoColor=EA4335)](mailto:sagi.baron76@gmail.com)

Join my [WhatsApp AI TIPS & TRICKS Channel](https://whatsapp.com/channel/0029Vaj33VkEawds11JP9o1c)

## התקנה

1. Clone את הrepository:

   ```
   git clone https://github.com/your-username/autobooker.git
   cd autobooker
   ```

2. צור סביבה וירטואלית והפעל אותה:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. התקן את הדרישות:

   ```
   pip install -r requirements.txt
   ```

4. העתק את קובץ `.env.example` ל-`.env` ועדכן את המשתנים הנדרשים:
   ```
   cp .env.example .env
   ```

## שימוש

הפעל את האפליקציה באמצעות Streamlit:

```
streamlit run main.py
```

פתח את הדפדפן בכתובת http://localhost:8501 כדי להשתמש באפליקציה.

## מבנה הפרויקט

- `main.py`: הקובץ הראשי של האפליקציה
- `file_upload.py`: טיפול בהעלאת קבצים
- `writing_style.py`: ניהול סגנונות כתיבה
- `interview_processing.py`: עיבוד ראיונות
- `book_creation.py`: יצירת הספר
- `photo_analysis.py`: ניתוח והטמעת תמונות
- `config.py`: ניהול הגדרות ומשתני סביבה

## תרומה

אנא קרא את [CONTRIBUTING.md](CONTRIBUTING.md) למידע על כיצד לתרום לפרויקט.

## רישיון

פרויקט זה מופץ תחת רישיון MIT. ראה את קובץ [LICENSE](LICENSE) לפרטים נוספים.
