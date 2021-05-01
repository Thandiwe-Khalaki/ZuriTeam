import random as ran
from datetime import datetime

now = datetime.now()
currentDt = now.strftime("%d/%m/%Y %H:%M:%S")

database = {
    4290010047: ['Thandiwe Khalaki', 'thandi', 'thandi@hotmail', 'password', 7000],

}

current_account = False

def init():
    isValidOption = False
    print("Welcome to ATM Machine")

    while isValidOption == False:   

        print("Do you have an account with us?")
        print("\n1 - Yes \t 2 - No")
        haveAccount = int(input("\nEnter your selection: "))

        if haveAccount == 1:
            login()

        else:
            register()

def login():
    print('...Login..')
    isValid = False

    while isValid == False:
        user_account = int(input('Enter your account number \n'))
        user_password = input('Enter your password \n')
        for account_number, user_details in database.items():
            if account_number == user_account and user_details[3] == user_password:
                isValid = True
                global current_account
                current_account = user_account
                bank_operation()

        if isValid == False:
            print('Invalid account number or user_password')

def register():
    print('...Registering..')
    email = input('please enter your email address \n')
    first_name = input('Your First Name? \n')
    last_name = input('Your last name \n')
    user_password = input('create a new password \n')

    account_number = generate_account()

    database[account_number] = [ first_name, last_name, email, user_password, 0]

    print('Your account number is:', account_number)
    bank_operation()

def generate_account():
    return ran.randrange(1000000000, 9999999999)

def bank_operation():
    isValidOption = False
    while isValidOption == False:
        print("WELCOME TO ABC ATM MACHINE")
        print("PLEASE CHOOSE THE FOLLOWING OPTIONS")

        print("\n1 - Withdraw \t 2 - Deposit \t 3 - Complain \t 4 - Exit ")

        selection = int(input("\nEnter your selection: "))

        #withdrawal amount
        wamt = 0.00
        #deposite amount
        damt = 0.00
        #account balance
        net_amt = 0.00

        if selection == 1:
        #Withdraw
            wamt = float(input("\nHow much would you like to withdraw: "))
            ver_wamt = input("Is this the correct amount, Yes or No ? " + str(wamt) + " ")
            if ver_wamt == "Yes":
                print("Take your cash")
                net_amt = net_amt + wamt
            else:
                print("Please start again")

        if selection == 2:
        # Deposit
            damt = float(input("\nHow much would you like to deposit: "))
            ver_damt = input("Is this the correct amount, Yes or No ? " + str(damt) + " ")
            if ver_damt == "Yes":
                net_amt = net_amt + damt
                print("Current balance is " + str(net_amt))
            else:
                print("Please start again")

        if selection == 3:
        # complain
            issue = input("\nWhat issue would you like to report: ")
            ver_issue = input("Is this the issue correct, Yes or No ? " + issue + " ")
            if ver_issue == "Yes":
                print("Thank you for reporting this issue to us")
            else:
                print(" Please start again")

        else:
                print("Thank you")
                exit()

def logout():
    print('Thank you ')
    exit()

def contact_bank():
    print('Would you like to contact the bank?')
    print("\n1 - Yes \t 2 - No ")

    bank = int(input("\nEnter your selection: "))
    if bank == 1:
        print('Contact us on +276 025 0648 during business hours')

    else:
        print('Thank you')



init()