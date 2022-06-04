def calc():
    a=int(input("Enter first number:"))
    b=input("enter an operator:")
    c=int(input("enter second number:"))
    if b=='.':
        print(a*c)
    elif b=='/':
        print(a/c)
    elif b == '+':
        print(a + c)
    elif b == '-':
        print(a - c)
    else:
        print("enter a valid inputs\n")
        calc()
while True:
    try:
        calc()
        break
    except:print ("enter valid inputs\n")
