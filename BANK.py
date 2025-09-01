print("WELCOME TO PYTHON BANK")
print("Please fill the following details carefully \nPlease fill the asked details in Capital)")
name=input("Enter your name please ")
a=int(input("enter your age please "))
pn=int(input("enter your phone number "))
add=(input("enter your address please "))
y=int(input("enter the years of experience you have with our bank "))

balance=500000

def c_emi(pri, ar, n):
    R = ar / (12 * 100)
    N = n * 12
    emi = int((pri * R * ((1 + R) ** N)) / (((1 + R) ** N) - 1))
    return emi

def loan(a, y):
    if (a>20):

        print("\nPlease enter your choice from the menu below:")
        print("1. Educational")
        print("2. Home")
        print("3. Gold")
        print("4. Personal")

        pr=int(input("\nPlease enter the purpose of which you prefer to have loan (1-4): "))
        match pr:
            case 1:
                if (y>=5):
                    print("\nloan will be assigned with the rate of 5, per month interest ")
                    ar=5
                else:
                    print("\nloan will be assigned with the rate of 7, per month interest ")
                    ar=7

            case 2:
                if (y>=5):
                    print("loan will be assigned with the rate of 8.5, per month interest ")
                    ar=8.5
                else:
                    print("\nloan will be assigned with the rate of 10, per month interest ")
                    ar=10

            case 3:
                if (y>=5):
                    print("\nloan will be assigned with the rate of 12, per month interest ")
                    ar=12
                else:
                    print("\nloan will be assigned with the rate of 14, per month interest ")
                    ar=14

            case 4:
                if (y>=5):
                    print("\nloan will be assigned with the rate of 12, per month interest ")
                    ar=12
                else:
                    print("\nloan will be assigned with the rate of 13, per month interest ")
                    ar=13

            case _:
                print("\nPlease enter a valid type of loan")

        pri=int(input("enter the loan amount you want "))
        n=int(input("enter the time period (in years) for which you want loan "))
        emi=c_emi(pri,ar,n)

        print(f"\nYour {pr} LOAN will be assigned with the rate of {ar}, per month interest ")
        print(f"\nYour monthly EMI will be: {emi}")

    else:
        print("You are not eligible for loan due to age restrictions")

def deposit():
    amt = int(input("\nEnter the amount to deposit: "))
    yrs = int(input("Enter deposit duration in years: "))
    print("The deposit will be compounded annually and at the rate of 6")
    m = amt * ((1.06) ** yrs)
    m = int(m)
    print(f"\nDeposit successful. At 6% interest,")
    print(f"Your maturity amount after {yrs} years will be: {m}\n")

def account():
    account_type = input("Enter account type (SAVINGS/CURRENT): ").upper()
    if account_type == "SAVINGS":
        print("Savings Account created successfully with min balance ₹1000\n")
    elif account_type == "CURRENT":
        print("Current Account created successfully with overdraft facility\n")
    else:
        print("Invalid account type\n")

def withdrawal():
    print("\nYou have selected withdrawal option")
    amt = int(input("Enter amount to withdraw: "))
    ac = int(input("Enter account number: "))
    pin = int(input("Enter your PIN: "))
    if amt>(balance-1000):
        print(f"Withdrawal of {amt} from account {ac} successful.")
    else:
        print(f"Insufficient balance in account {ac}.")

def transfer():
    print("\nYou have selected transfer option")
    amt = int(input("Enter amount to transfer: "))
    ac_from = int(input("Enter your account number: "))
    ac_to = int(input("Enter recipient account number: "))
    pin = int(input("Enter your PIN: "))
    if amt>(balance-1000):
        print(f"Transfer of {amt} from account {ac_from} to {ac_to} successful.")
    else:
        print(f"Insufficient balance in account {ac_from}.")

def card():
    print("\nYou have selected credit/debit card application option")
    card_type = input("Enter card type (CREDIT/DEBIT): ").upper()
    if card_type == "CREDIT":
        print("Credit Card application submitted successfully.")
    elif card_type == "DEBIT":
        print("Debit Card application submitted successfully.")
    else:
        print("Invalid card type")

def schemes():
    print("\nThe following schemes are available in our bank:")
    print("1. Fixed Deposit")
    print("2. Recurring Deposit")
    print("3. Monthly Income Scheme")
    print("4. Senior Citizen Savings Scheme")

print("Please enter your choice from the menu below:")
print("1. Apply for Loan")
print("2. Open a Deposit")
print("3. Open an Account")
print("4. Cash Withdrawal")
print("5. Cash Transfer to another account")
print("6: Apply for Credit/debit Card")
print("7: Schemes available")
print("8. Check bank balance")
print("9. Exit")

choice = input("\nEnter your purpose for visiting our bank (1-9): ")

if choice == "1":
    loan(a, y)
elif choice == "2":
    deposit()
elif choice == "3":
    account()
elif choice == "4":
    withdrawal()
elif choice == "5":
    transfer()
elif choice == "6":
    card()
elif choice == "7":
    schemes()
elif choice == "8":
    print("\nYou have selected check bank balance option")
    ac = int(input("Enter account number: "))
    pin = int(input("Enter your PIN: "))
    print(f"Your current account balance for account {ac} is: {balance}")
elif choice == "9":
    print("\nThank you for banking with us!")
else:
    print("\nInvalid choice, please try again.")



