def fun():
    try:
        a=list(map(int,input("Enter the integer elements of the array with white spaces between them\n").split()))
    except:
        print("Enter valid input")
        fun()
    b={}
    for i in a :
        if i in b :
            b[i]=b[i]+1
        else:
            b[i]=0
    print(max(b,key=b.get))
fun()