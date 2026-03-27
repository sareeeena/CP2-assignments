class BankAccount:
    bank_name="Urgench Bank"
    total_accounts=0
    min_balance=20

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        BankAccount.total_accounts +=1
    def deposit(self,amount):
        new_balance=self.balance+amount
        self.balance=new_balance
        if amount>0:
            self.balance=new_balance
            print(f"Deposited{amount}. New balance: {new_balance}")
    def withdraw(self,amount):
        new_balance=self.balance-amount
        if new_balance < BankAccount.min_balance:

            print("Insufficient")
        else:
            self.balance=new_balance

            print(f"Owner: {self.owner}")

        account1=BankAccount("Ali",100)
        account2=BankAccount("Vali",50)
        account1.display_account_info()
        account1.deposit(5)
        account2.withdraw(80)
        account2.display_account_info()
        account2.withdraw(100)
        print(total_accounts)


