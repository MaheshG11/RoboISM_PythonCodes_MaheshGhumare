def fun() :
    d=[]
    try:
        a=list(map(int,input("Enter the integer elements of the array with white spaces between them\n").split()))
        if len(a)!=2:
            s
    except:
        print("Enter valid input")
        fun()
    for i in range(a[0],a[1]):
        c = 0
        for j in range(2,int(i/2)):
            if i%j==0:
                c=1
                break
        if c==0:
            d.append(i)
    print(f"The prime numbers in the {a[0]} and {a[1]} are {d}")
fun()
