# 🏦 Bank Management System

A simple yet functional **Bank Management System** built using **Python** and **Streamlit**.  
This project allows users to perform essential banking operations such as account creation, deposit, withdrawal, updates, and deletion — all while storing data persistently in a JSON file.

---

## ✨ Features

- 🧾 Create new bank accounts with unique account numbers.  
- 💰 Deposit money securely using PIN authentication.  
- 💸 Withdraw funds and validate balance availability.  
- 📋 View detailed account information.  
- ✏️ Update account details (Name, Email, PIN).  
- 🗑️ Delete accounts when no longer needed.  
- 🌐 User-friendly **Streamlit Web Interface** with a modern design.  
- 💾 Persistent storage in a JSON file (`data.json`).

---

## 🧩 Project Structure

```
📁 Bank_Management_System/
│
├── bank.py        # Core banking logic (CRUD operations, deposit, withdrawal)
├── main.py        # Command-line interface for interacting with the bank system
├── app.py         # Streamlit web app with a clean and modern UI
├── data.json      # Persistent storage for all user account information
└── README.md      # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Bank_Management_System.git
cd Bank_Management_System
```

### 2. Install Dependencies
Make sure you have **Python 3.8+** installed. Then install Streamlit:
```bash
pip install streamlit
```

### 3. Run the CLI Application
```bash
python main.py
```

### 4. Run the Streamlit Web App
```bash
streamlit run app.py
```

---

## 💾 Data Handling

- All data is stored in a **JSON file** (`data.json`).
- Each account record includes:
  - `name`  
  - `age`  
  - `email`  
  - `pin`  
  - `accountNO`  
  - `balance`
- The system updates the file automatically after every transaction.

---

## 🧠 Tech Stack

- **Python** — Core logic and data handling  
- **Streamlit** — Web interface  
- **JSON** — Persistent local storage  

---

## 📸 App Preview

> Example of the Streamlit interface:
- Account creation with validation  
- Deposit & withdrawal operations  
- View, update, and delete accounts with instant feedback  

## 👨‍💻 Author

**Shubam Patial**  
🎓 Computer Programming Graduate | 💡 Python & Emerging AI/ML Engineer  
📍 Based in Ontario, Canada  
🔗 [LinkedIn](www.linkedin.com/in/shubham-patial-b9023335a) 

---
+
### ⭐ If you like this project, give it a star on GitHub!
