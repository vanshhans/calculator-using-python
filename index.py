def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def divide(x,y):
    if y==0:
        return "cannot divide by 0"
    return x/y

def multiply(x,y):
    return x*y

print("Available Operations")
print("1) ADD")
print("2) SUBTRACT")
print("3) MULTIPLY")
print("4) DIVIDE")

while True:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    choice=input("Enter choice: 1 2 3 4 \n")
    if(choice=="1"):
        print(add(num1,num2))
    elif(choice=="2"):
        print(subtract(num1,num2))
    elif(choice=="3"):
        print(multiply(num1,num2))
    elif(choice=="4"):
        print(divide(num1,num2))
    else:
        print("Select valid option")
