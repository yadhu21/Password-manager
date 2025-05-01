
# 🔐 Password Manager with Login System

A user-friendly desktop application that provides secure password management along with a basic login/registration system. Built using Python's `Tkinter`, the app supports **multi-user data storage**, **CRUD operations**, and **password generation**.

---

## 📁 Features

### ✅ Login System
- **Register** new users (username/password stored in plain text files — for demo only)
- **Login** validation
- Launches password manager only after successful login

### 🛠️ Password Manager
- Save new credentials (website, username, password, security Q&A)
- View saved entries in a scrollable table
- Edit or delete credentials
- Search website-specific entries
- Generate random strong passwords
- Copy password directly to clipboard
- Records are **user-specific**

---

## 🧱 Project Structure

```
password_manager_project/
├── db_operations.py          # SQLite-based database operations
├── password_manager.py       # Main password manager GUI (after login)
├── login.py           # Login and registration system
├── README.md                 # Project documentation
```

---

## ▶️ Getting Started

### Prerequisites
- Python 3.x
- Modules: `tkinter`, `sqlite3`, `pyperclip`, `random`, `subprocess`

Install `pyperclip`:
```bash
pip install pyperclip
```

### Run the App

```bash
python login_system.py
```

Upon successful login, it will launch `password_manager.py` automatically with the logged-in username.

---

## 💾 Data Storage

### User Login
- Each registered user's credentials are stored in a simple text file named after the username.

### Password Records
- Stored in a local SQLite database `password_record.db`
- Table: `password_info`

Each record contains:
- `website`, `username`, `password`, `question`, `answer`, `user`
- Auto timestamps: `created_date`, `update_date`

---

## ⚠️ Security Notice

This project is a **demo** and not suitable for production unless:
- Passwords are encrypted (currently stored in plain SQLite text fields)
- Login system avoids using text files for credential storage

---

## 🧪 Example

- Run `login.py`
- Register a user
- Login with that user
- The password manager window will open to manage credentials

---

## 👨‍💻 Author

Developed by Yadhu Krishnan C K


---
