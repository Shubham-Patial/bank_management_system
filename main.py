from bank import Bank

def main():
    user = Bank()

    while True:
        print("""
🏦 Welcome to Simple Bank System

1. Create an account
2. Deposit money
3. Withdraw money
4. Show account details
5. Update account details
6. Delete account
7. Exit
""")

        try:
            choice = int(input("Please select an option (1–7): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        match choice:
            case 1:
                user.createaccount()
            case 2:
                user.depositmoney()
            case 3:
                user.withdrawmoney()
            case 4:
                user.showdetails()
            case 5:
                user.updatedetails()
            case 6:
                user.delete()
            case 7:
                print("👋 Thank you for using Simple Bank System. Goodbye!")
                break
            case _:
                print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
