

#bank prgrm


class bank:
    def create_account(self,acno,actype):
       
        self.bankname="SBT"
        self.acno=acno
        self.__balance=2000
        self.actype=actype
    def deposit(self,amount):
        self.__balance+=amount
        print(f"your {self.bankname} acc with {self.acno} has been credited {amount} balance is {self.__balance}") 
    def withdraw(self,amount):
        if amount>self.__balance: #5000>2000
            print("transaction fai;led insufficient balamce")
        else:
            self.__balance-=amount
            print(f"your {self.bankname} acc with {self.acno} has been debited {amount} balance is {self.__balance}") 
    def get_balance(self):
        print(f"available bal={self.__balance}")
# user_account=bank()
# user_account.create_account(5000,"savings") 
# user_account.withdraw(2000) 
# user_account.deposit(1000)                       
              
rifa_account=bank()
rifa_account.create_account(4646,"savings")
rifa_account.deposit(1000)
rifa_account.balance+=20000





