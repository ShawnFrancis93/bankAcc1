class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrwal(self, amount):
        if self.account_balance-amount>=0:
            self.account_balance -= amount
        else:
            print("Dear",self.name," ,you tried to withdraw: ",amount, "but you have insufficient balance so your withdrawal has failed. Your current balance is: ",self.account_balance)
    def display_user_balance(self):
        print ("Dear ",self.name," your current balance is: ",self.account_balance)
    def transfer_money_to_other_user(self,other,amount):
        if self.account_balance - amount >=0:
            self.account_balance-=amount
            other.account_balance+=amount
            print("success.",self.name,", you have transferred an amount of: ",amount," to ",other.name,". Your current Balancec is",self.account_balance)
        else:
            print("Failed.",self.name,", you have tried to transfer an amount of: ",amount," to ",other.name,"but your balance is insufficient.Your current Balancec is",self.account_balance)


drake = User("drake", "drake@aol.com")
josh = User("josh", "josh@yahoo.com")
megan = User("megan", "megan@gmail.com")
drake.make_deposit(2000)
drake.make_deposit(200)
drake.make_deposit(200)
drake.make_withdrwal(100)
drake.display_user_balance()
josh.make_deposit(150)
josh.make_deposit(270)
josh.make_withdrwal(100)
josh.make_withdrwal(67)       
josh.display_user_balance()
megan.make_deposit(30000)
megan.make_withdrwal(230)
megan.make_withdrwal(500)
megan.make_withdrwal(999)
megan.display_user_balance()
megan.transfer_money_to_other_user(josh,700)
megan.transfer_money_to_other_user(drake,500)