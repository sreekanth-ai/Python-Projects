class calci:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mult(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
    def floordiv(self,x,y):
        return x//y
    def mod(self,x,y):
        return x%y
    def power(self,x,y):
        return x**y
    
obj = calci()
while True:
    print("1 : Add")
    print("2 : sub")
    print("3 : mult")
    print("4 : div")
    print("5 : floordiv")
    print("6 : mod")
    print("7 : power")
    ch = int(input("enter the choice : "))
    if ch in range(1,8):
        x = int(input("enter the value of num1 : "))
        y = int(input("enter the value of num2 : "))
    else:
        print("Invalid input")
        break
    if ch == 1:
        print(x,"+",y,"=",obj.add(x,y))
    elif ch == 2:
        print(x,"-",y,"=",obj.sub(x,y))
    elif ch == 3:
        print(x,"*",y,"=",obj.mult(x,y))
    elif ch == 4:
        print(x,"/",y,"=",obj.div(x,y))
    elif ch == 5:
        print(x,"//",y,"=",obj.floordiv(x,y))
    elif ch == 6:
        print(x,"%",y,"=",obj.mod(x,y))
    elif ch == 7:
        print(x,"^",y,"=",obj.power(x,y))
    
