#bankaccount
#  i started this, but am haing trouble with the concept
#  of classes and how to manipulate them
#  i will get back to this after i go back and learn 
#  classes and objects a little better

class BankAccount:
    def __init__(self, first_name, last_name, middle_name, account_type, balance, status):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.account_type = account_type
        self.balance = 0.0
        self.status = "Closed"
    
    def account_open(self):
        print 
        
    
    def balance_check(self):
        if float(self.balance) >= 100:
            account_open(self)
            self.status = "Open"
        else:
            print("Sorry.  You need more money")

    def account_open(self):
        first = input("What is your first name?: ")
        last = input("What is your last name?: ")
        middle = input("What is your middle name?")
        account = input("What type of account would you like to open?: ")



