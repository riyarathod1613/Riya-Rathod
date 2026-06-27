# Riya-Rathod
🔐 AI Password Strength Checker

📌 Project Overview

The AI Password Strength Checker is a cybersecurity-based Python project designed to evaluate the strength of user passwords and provide real-time security analysis. The system analyzes passwords based on length, character diversity, entropy score, and common password detection to determine their overall security level.

The project simulates a real-world password auditing tool by instantly evaluating passwords entered by users and generating detailed security reports in the terminal.

---

🎯 Objectives

- Analyze password strength in real time.
- Calculate password entropy scores.
- Estimate password crack time.
- Detect commonly used weak passwords.
- Provide recommendations for creating stronger passwords.
- Store password analysis reports for future review.

---

✨ Features

- Real-time password strength analysis.
- Entropy score calculation.
- Password crack time estimation.
- Common password detection.
- Security recommendations.
- Password analysis logging using CSV.
- User-controlled password checking.
- Detailed password indicators:
  - Password Length
  - Uppercase Letters
  - Lowercase Letters
  - Numbers
  - Special Characters
  - Common Password Check

---

🛠 Technologies Used

- Python
- Math Module
- String Module
- CSV File Handling
- VS Code

---

📂 Project Structure

AI-Password-Strength-Checker/
│
├── app.py
├── password_utils.py
├── common_passwords.txt
├── password_logs.csv
├── requirements.txt
└── README.md

---

💻 VS Code Terminal Setup

---

⚙️ Installation

Step 1: Download or Clone the Repository

git clone <repository-link>
cd AI-Password-Strength-Checker

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Run the Application

python app.py

---

📊 Sample Output


🔐 AI Password Strength Checker

Password: riya@1613

🟡 Medium
████████████████ 80%

Entropy Score : 54.8
Estimated Crack Time : 500 years

Suggestions:
✓ Add uppercase letters

Check another password? (y/n):

---

🧠 Password Analysis Logic

Evaluation Factors:

- Password Length
- Lowercase Letters
- Uppercase Letters
- Numbers
- Special Characters
- Common Password Detection

Output:

- Strong Password
- Medium Password
- Weak Password

---

📁 Password Logs

Password analysis reports are stored in:

password_logs.csv

Example:

Timestamp,Password Length,Score,Strength,Entropy,Crack Time
2026-06-27 10:30:15,9,100,Strong,58.9,500 years

---

🔮 Future Enhancements

- GUI using Tkinter
- Flask Web Application
- AI-Based Password Suggestions
- Password Generator
- Dark Web Password Leak Detection
- Multi-Language Support
- User Authentication Dashboard
- Password Security Analytics Dashboard

---

👨‍💻 Author

Riya Rathod

Diploma in Computer Engineering

Cybersecurity and Python Enthusiast

---

📜 License

This project is developed for educational and learning purposes only.

The password strength analysis and crack-time estimation are based on simplified calculations and do not represent actual real-world attack capabilities. The project is intended for cybersecurity learning, awareness, and academic demonstrations.
