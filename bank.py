import random
import string
import json
from pathlib import Path

class Bank:
    data_fetching = 'data.json'
    data = []

    try:
        if Path(data_fetching).exists():
            with open(data_fetching) as f:
                data = json.loads(f.read())
        else:
            with open(data_fetching, 'w') as f:
                json.dump([], f)
            print("New data file created: data.json")
    except Exception as e:
        print(f"An exception occurred: {e}")

    @classmethod
    def __update(cls):
        with open(cls.data_fetching, 'w') as f:
            json.dump(cls.data, f, indent=4)

    @classmethod
    def __accountcreation(cls):
        chars = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        special_char = random.choices("*%$#&?", k=1)
        id = chars + num + special_char
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name": input("Enter your name = "),
            "age": int(input("Enter your age = ")),
            "email": input("Enter your email = "),
            "pin": int(input("Enter the 4-digit PIN you want to set = ")),
            "accountNO": Bank.__accountcreation(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry, you cannot create your account.")
        else:
            print("\n✅ Account created successfully!\n")
            for k, v in info.items():
                print(f"{k} : {v}")
            print("\nPlease save your Account Number somewhere safe.\n")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accountNO = input("Enter your account NO = ")
        pinNo = int(input("Enter your 4-digit PIN = "))

        user_data = [i for i in Bank.data if i['accountNO'] == accountNO and i['pin'] == pinNo]
        if not user_data:
            print("❌ No account found with these details.")
            return

        amount = int(input("Enter the amount to deposit = "))
        if amount > 10000 or amount <= 0:
            print("❌ Amount must be between 1 and 10000.")
        else:
            user_data[0]['balance'] += amount
            Bank.__update()
            print("💰 Amount deposited successfully!")

    def withdrawmoney(self):
        accountNO = input("Enter your account NO = ")
        pinNo = int(input("Enter your 4-digit PIN = "))

        user_data = [i for i in Bank.data if i['accountNO'] == accountNO and i['pin'] == pinNo]
        if not user_data:
            print("❌ No account found with these details.")
            return

        withdraw_amount = int(input("Enter the amount to withdraw = "))
        if user_data[0]['balance'] < withdraw_amount:
            print("❌ Insufficient balance.")
        else:
            user_data[0]['balance'] -= withdraw_amount
            Bank.__update()
            print("✅ Amount withdrawn successfully!")

    def showdetails(self):
        accountNO = input("Enter your account NO = ")
        pinNo = int(input("Enter your 4-digit PIN = "))

        user_data = [i for i in Bank.data if i['accountNO'] == accountNO and i['pin'] == pinNo]
        if not user_data:
            print("❌ No account found with these details.")
            return

        print("\n📄 Account Details:\n")
        for k, v in user_data[0].items():
            print(f"{k}: {v}")

    def updatedetails(self):
        accountNO = input("Enter your account NO = ")
        pinNo = int(input("Enter your 4-digit PIN = "))
        user_data = [i for i in Bank.data if i['accountNO'] == accountNO and i['pin'] == pinNo]

        if not user_data:
            print("❌ No account found with these details.")
            return

        print("\nEnter new details (press Enter to skip):")
        name = input("New name: ")
        email = input("New email: ")
        pin_input = input("New 4-digit PIN: ")

        if pin_input.strip() == "":
            new_pin = user_data[0]['pin']
        else:
            new_pin = int(pin_input)

        user_data[0]['name'] = name if name else user_data[0]['name']
        user_data[0]['email'] = email if email else user_data[0]['email']
        user_data[0]['pin'] = new_pin

        Bank.__update()
        print("✅ Information updated successfully!")

    def delete(self):
        accountNO = input("Enter your account NO = ")
        pinNo = int(input("Enter your 4-digit PIN = "))
        user_data = [i for i in Bank.data if i['accountNO'] == accountNO and i['pin'] == pinNo]
        if not user_data:
            print("❌ No account found with these details.")
            return

        choice = input("Are you sure you want to delete your account? (y/n): ")
        if choice.lower() == 'y':
            Bank.data.remove(user_data[0])
            Bank.__update()
            print("🗑️ Account deleted successfully.")
        else:
            print("Action cancelled.")
