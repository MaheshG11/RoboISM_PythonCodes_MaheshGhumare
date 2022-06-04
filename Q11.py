def fun():
    a=input()
    c=0
    for i in range(int(len(a)//2)):
        if a[i]!=a[len(a)-i-1]:
            c=1
            print("Is not a palindrome")
            break
    if c==0:
        print("Is a palindrome")

fun()
