'''
Nepal Bank Management System 2.0
'''

import json

try: 
  with open("accounts.json","r") as file:
   accounts=json.load(file)
except FileNotFoundError:
   accounts={ 
   "Nikita":50000,
   "Ram":10000,
   "Sita":90000
   }

   with open("accoumts.json","w") as file:
     json.dump(accounts,file,indent=4) #for redable format
class BankAccount:
    bank_name="Nepal Bank"
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def __str__(self):
        return f"{self.owner} has Rs.{self.balance} in their account."

    def deposit_amount(self):
        try:
            amount=int(input("Enter your deposit amount:"))
        except ValueError:
            print("Please enter a valid amount")
        else:
            if amount<=0:
                print("Amount must be greater than 0.")
            else:
                self.balance+=amount
                print("Successfully deposited.")
                print("Balance:",self.balance)

    def withdraw_amount(self):
        try:
           amount=int(input("Enter withdrawal amount:"))
          
        except ValueError:
            print("Please enter a valid amount")
        else:
             if amount<=0:
                print("Amount must be greater than 0.")
             elif amount>self.balance:
                print("Insufficient balance")
             else:
              self.balance-=amount
              print("withdrawal sucessful,Thank you")
              print("Remaining balance:",self.balance)

    def show_balance(self):
        print("Account owner:",self.owner)
        print("Current balance:",self.balance)

account1=BankAccount("Nikita",accounts["Nikita"])
account2=BankAccount("Ram",accounts["Ram"])
account3=BankAccount("Sita",accounts["Sita"])

while True:
    print("Welcome to Nepal Bank")
    print("1.Nikita")
    print("2.Ram")
    print("3.Sita")
    print("4.Exit")

    choice=input("Please select your account:")

    if choice=="1":
        selected_account=account1
    elif choice=="2":
        selected_account=account2
    elif choice=="3":
        selected_account=account3
    elif choice=="4":
        print("Thank you for using our service")
        break
    else:
        print("Invalid option")

    while True:

       print("Welcome,",selected_account.owner)
       print(f"---{selected_account.owner}---")
       print("1.Show balance")
       print("2.Deposit amount")
       print("3.Withdraw amount")
       print("4.Account Selection")

       choice=input("Choose an option:")
       if choice=="1":
        selected_account.show_balance()

       elif choice=="2":
        selected_account.deposit_amount()

       elif choice=="3":
        selected_account.withdraw_amount()

       elif choice=="4":
        print("Choose your account")
        break
       else:
        print("Invalid option")




            
            

        