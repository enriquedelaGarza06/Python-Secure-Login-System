# Secure Login System

Secure authentication system written in Python. It uses the `bcrypt` library for password hashing and a local JSON file for data persistence.

This project was created to understand user validation logic and secure credential handling (avoiding plain text storage).

## Features
- **Hashing:** Passwords are securely hashed (irreversible).
- **Persistence:** User data is stored in `Users.json`.
- **Error Handling:** Automatically initializes the database file if it doesn't exist.

## Installation & Usage

1. Install the security library:
   ```bash
   pip install bcrypt
