def fun():
    a=input("Enter the string")
    b=[]
    for i in a :
        b.append(i)
    b.sort()
    b=''.join(b)
    print(b)
fun()