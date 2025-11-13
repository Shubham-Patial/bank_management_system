import streamlit as st
import json
from bank import Bank

DATA_FILE = "data.json"
bank = Bank()

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

st.set_page_config(page_title="🏦 Bank Management System", layout="centered", page_icon="🏦")

st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #e8f1ff 0%, #f8fbff 100%);
            color: #333333;
        }
        div.block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .card {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin-top: 1.5rem;
        }
        h1, h2, h3 {
            color: #004aad;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton > button {
            background-color: #004aad !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 0.6rem 1.5rem !important;
            font-weight: bold !important;
            transition: 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #006aff !important;
            transform: scale(1.05);
        }
        .sidebar .sidebar-content {
            background-color: #f0f5ff;
        }
        .css-1d391kg, .css-18e3th9 {
            background: transparent;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏦 Bank Management System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Your simple, secure & smart digital banking interface.</p>", unsafe_allow_html=True)
st.markdown("---")

menu = ["🏠 Home", "🧾 Create Account", "💰 Deposit Money", "💸 Withdraw Money", "📋 View Details", "✏️ Update Details", "🗑️ Delete Account"]
choice = st.sidebar.radio("📍 Navigation Menu", menu)

if choice == "🏠 Home":
    st.markdown("""
        <div class="card">
        <h3>Welcome to Your Digital Bank 💳</h3>
        <p>Perform secure operations easily — create, update, deposit, withdraw, or delete accounts.</p>
        <ul>
            <li>🧾 Create new accounts with personalized PINs.</li>
            <li>💰 Deposit and manage balances safely.</li>
            <li>💸 Withdraw funds instantly.</li>
            <li>📋 View or update account details.</li>
            <li>🗑️ Delete accounts when no longer needed.</li>
        </ul>
        <p>➡️ Use the left sidebar to start.</p>
        </div>
    """, unsafe_allow_html=True)

elif choice == "🧾 Create Account":
    st.markdown("<div class='card'><h3>🧾 Create Account</h3>", unsafe_allow_html=True)
    name = st.text_input("👤 Full Name")
    age = st.number_input("🎂 Age", min_value=0, step=1)
    email = st.text_input("📧 Email")
    pin = st.text_input("🔢 4-digit PIN", type="password", max_chars=4)

    if st.button("✅ Create Account"):
        if not name or not email or not pin:
            st.warning("⚠️ All fields are required!")
        elif len(pin) != 4 or not pin.isdigit():
            st.error("❌ PIN must be exactly 4 digits.")
        elif age < 18:
            st.error("🚫 Must be at least 18 years old.")
        else:
            from random import choices, shuffle
            from string import ascii_letters, digits
            chars = choices(ascii_letters, k=3)
            nums = choices(digits, k=3)
            special = choices("*%$#&?", k=1)
            acc = chars + nums + special
            shuffle(acc)
            accountNO = "".join(acc)

            new_account = {
                "name": name,
                "age": int(age),
                "email": email,
                "pin": int(pin),
                "accountNO": accountNO,
                "balance": 0
            }

            data = load_data()
            data.append(new_account)
            save_data(data)
            st.success("✅ Account created successfully!")
            st.info(f"💳 Your Account Number: `{accountNO}` — save it securely.")
    st.markdown("</div>", unsafe_allow_html=True)

elif choice == "💰 Deposit Money":
    st.markdown("<div class='card'><h3>💰 Deposit Money</h3>", unsafe_allow_html=True)
    account = st.text_input("🏦 Account Number")
    pin = st.text_input("🔢 PIN", type="password", max_chars=4)
    amount = st.number_input("💵 Amount to Deposit", min_value=1, step=1)

    if st.button("💸 Deposit"):
        data = load_data()
        for user in data:
            if user['accountNO'] == account and str(user['pin']) == pin:
                if amount > 10000:
                    st.warning("⚠️ Deposit limit is $10,000.")
                else:
                    user['balance'] += amount
                    save_data(data)
                    st.success(f"✅ ${amount} deposited successfully!")
                    st.info(f"💰 New Balance: ${user['balance']}")
                break
        else:
            st.error("❌ Invalid account number or PIN.")
    st.markdown("</div>", unsafe_allow_html=True)

elif choice == "💸 Withdraw Money":
    st.markdown("<div class='card'><h3>💸 Withdraw Money</h3>", unsafe_allow_html=True)
    account = st.text_input("🏦 Account Number")
    pin = st.text_input("🔢 PIN", type="password", max_chars=4)
    amount = st.number_input("💵 Amount to Withdraw", min_value=1, step=1)

    if st.button("🏧 Withdraw"):
        data = load_data()
        for user in data:
            if user['accountNO'] == account and str(user['pin']) == pin:
                if user['balance'] < amount:
                    st.error("❌ Insufficient balance.")
                else:
                    user['balance'] -= amount
                    save_data(data)
                    st.success(f"💸 ${amount} withdrawn successfully!")
                    st.info(f"💵 Remaining Balance: ${user['balance']}")
                break
        else:
            st.error("❌ Invalid account number or PIN.")
    st.markdown("</div>", unsafe_allow_html=True)

elif choice == "📋 View Details":
    st.markdown("<div class='card'><h3>📋 View Account Details</h3>", unsafe_allow_html=True)
    account = st.text_input("🏦 Account Number")
    pin = st.text_input("🔢 PIN", type="password", max_chars=4)

    if st.button("📄 Show Details"):
        data = load_data()
        for user in data:
            if user['accountNO'] == account and str(user['pin']) == pin:
                st.success("✅ Account Found!")
                st.json(user)
                break
        else:
            st.error("❌ No account found.")
    st.markdown("</div>", unsafe_allow_html=True)

elif choice == "✏️ Update Details":
    st.markdown("<div class='card'><h3>✏️ Update Account Details</h3>", unsafe_allow_html=True)
    account = st.text_input("🏦 Account Number")
    pin = st.text_input("🔢 PIN", type="password", max_chars=4)
    new_name = st.text_input("👤 New Name (optional)")
    new_email = st.text_input("📧 New Email (optional)")
    new_pin = st.text_input("🔢 New 4-digit PIN (optional)", type="password", max_chars=4)

    if st.button("💾 Update"):
        data = load_data()
        for user in data:
            if user['accountNO'] == account and str(user['pin']) == pin:
                if new_name:
                    user['name'] = new_name
                if new_email:
                    user['email'] = new_email
                if new_pin and len(new_pin) == 4 and new_pin.isdigit():
                    user['pin'] = int(new_pin)
                save_data(data)
                st.success("✅ Details updated successfully!")
                break
        else:
            st.error("❌ Invalid account number or PIN.")
    st.markdown("</div>", unsafe_allow_html=True)

elif choice == "🗑️ Delete Account":
    st.markdown("<div class='card'><h3>🗑️ Delete Account</h3>", unsafe_allow_html=True)
    account = st.text_input("🏦 Account Number")
    pin = st.text_input("🔢 PIN", type="password", max_chars=4)

    if st.button("🚨 Delete Account"):
        data = load_data()
        for user in data:
            if user['accountNO'] == account and str(user['pin']) == pin:
                data.remove(user)
                save_data(data)
                st.success("🗑️ Account deleted successfully!")
                break
        else:
            st.error("❌ Invalid account number or PIN.")
    st.markdown("</div>", unsafe_allow_html=True)
