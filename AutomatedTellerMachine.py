import datetime
now = datetime.datetime.now()

print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

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
# Withdraw
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