# AutoBooker: מערכת אוטומטית ליצירת ספרים מראיונות

AutoBooker היא מערכת המאפשרת יצירה אוטומטית של ספרים מראיונות מוקלטים. המערכת מתמללת ראיונות, מעבדת את הטקסט לפי סגנונות כתיבה מוגדרים, ומארגנת את התוכן לספר קוהרנטי.

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
