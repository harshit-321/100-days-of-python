⏰ Python Alarm Clock

This is a simple Python-based alarm clock that allows you to set a specific time, and it will alert you with a beep sound when the time matches.

---

🚀 Features

Set alarm in HH:MM format (24-hour clock).

Continuously checks the system time until the alarm rings.

Plays a beep sound when the alarm time is reached (Windows only).

Lightweight and easy to use.

---

🛠️ Tools & Libraries Used

Python 3

datetime (to fetch system time)

time (to pause execution and reduce CPU usage)

winsound (to play sound on Windows)


---

📌 How to Run

Clone this repository or download the file.

Run the script in your terminal:

python alarm.py


Enter the alarm time in HH:MM format (example: 06:45).

Wait until the alarm time — you’ll hear a beep sound!

---

⚠️ Note

winsound works only on Windows.

For Linux/Mac, you can replace winsound with other audio libraries like playsound or pygame.


