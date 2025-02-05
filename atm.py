class ATM:
    balance = 10000
    def login(self,pin):
        if pin == 456123:
            return True
        else:
            return False
    def credit(self,amount):
        self.balance += amount
    def debit(self,amount):
        self.balance -= amount
    def display(self):
        print("Total Remaining balance : ",str(self.balance))
        
obj = ATM()
flag = False
for i in range(3):
    if obj.login(int(input("enter the pin : "))):
        flag = True
        break
if flag:
    while True:
        o = int(input('''
                  enter 1 for credit
                  enter 2 for debit
                  enter 3 for balance
                  enter 4 for exit\n'''))
        if o == 1:
            obj.credit(int(input("enter the amount to be credit : ")))
            print("After the the credit")
            obj.display()
        elif o==2:
            amount = int(input("enter the amount to debit : "))
            if amount<= obj.balance:
                obj.debit(amount)
                print("After the the debit")
                obj.display()
            else:
                print("Insufficient balance")
        elif o==3:
            obj.display()
        elif o==4:
            exit(o)
else:
    print("Your pin code attempt has been completed")


                
        