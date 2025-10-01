# 📧 Email Slicer (Python)

A simple Python project that slices an email address into two parts:
- **Username / Local Part** → The text before `@`
- **Domain** → The text after `@`

This project is beginner-friendly and a great way to practice working with strings, functions, and basic input/output in Python.

---

## 🚀 Features
- Extracts **username** and **domain** from any email
- Handles user input and trims spaces
- Shows clear error message for invalid emails
- Lightweight and beginner-friendly

---

## 🛠️ Technologies Used
- Python 3.x
- Regex (for validation)

---

## 📂 Project Structure

email_slicer.py       # main script README.md             # project documentation

---

## ▶️ Usage

### Run directly
```bash
python email_slicer.py

Then enter an email:

Enter an email: harshit@example.com
Local part: harshit
Domain:     example.com


---

📸 Example Output

Enter an email: student123@gmail.com
Local part: student123
Domain:     gmail.com


---

🧑‍💻 Future Improvements

Add GUI (Tkinter / PyQt)

Support batch email slicing from a file

Export results to CSV/Excel

