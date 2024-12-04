class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,balance):
        try:
            if (balance> self.balance):
                raise Exception("\nWithdraw balance must be less than or equal to current balance\n")
            elif (balance <= 0):
                raise Exception("\nWithdraw balance must be greater than 0\n")
            self.balance -=balance
            print(f"\n Current balance after withdraw = {self.balance}\n")
                
        except Exception as e:
            print(e)
            
    def deposit(self, balance):
        try:
            
         if (balance <= 0):
             raise Exception("\nDeposit balance must be greater 0 \n")
         
         self.balance += balance
         
         print(f"\nCurrent Balance after deposit = {self.balance}\n")
        except Exception as e:
            print(e) 
            
    def showBalance(self):
        status = "LOW" if (self.balance < 500) else ''
        print(f"\nYour Current Balance {self.balance} ({status})\n")
            
            
account = BankAccount(0.0)
def conditon(temp):
     if (temp == 1):
        account.showBalance()
     elif (temp == 2):
        balance = float(input("\nEnter deposit balance "))
        account.deposit(balance)
     elif (temp == 3):
        balance = float(input("\nEnter withdraw balance "))
        account.withdraw(balance)
    
while True:
    print("\n1. Show Balance ")
    print("2. Deposit Balance ")
    print("3. Withdraw Balance ")
    print("4. exit ")
    checker = [1,2,3,4]
    try:
        
        temp = int(input("\nEnter your choice(1-4) "))
        if temp not in checker:
            raise Exception("\nEnter valid choice \n")
        if temp == 4:
            print("\nThank You! Have a nice day\n")
            break
        else:
            conditon(temp)
    except Exception as e:
        print(e)
    