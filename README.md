# 🔐 Secure Login System with Python

A robust authentication system built with **Python** that demonstrates secure password handling using **Hashing** and **Salting** techniques.

This project was developed to understand the "White Box" logic behind user authentication, input validation, and data persistence—essential skills for Quality Assurance and Backend development.

---

## 🚀 Key Features

- **Secure Password Storage:** Uses the `bcrypt` library to hash passwords with auto-generated salts. Passwords are never stored in plain text.
- **Data Persistence:** User credentials are automatically saved in a local `Users.json` file, mimicking a NoSQL database structure.
- **Robust Error Handling:** The system automatically initializes the database file if it doesn't exist, preventing crashes (`FileNotFoundError`).
- **Input Validation:** Handles data encoding (UTF-8) to ensure smooth processing between user input and the hashing algorithm.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Security Library:** `bcrypt`
- **Data Format:** JSON

## ⚙️ How to Run

1. **Clone the repository**
   ```bash
   git clone [https://github.com/enriquedelaGarza06/Python-Secure-Login-System.git](https://github.com/enriquedelaGarza06/Python-Secure-Login-System.git)
