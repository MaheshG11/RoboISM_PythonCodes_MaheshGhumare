def credi():
    while True:
            ccdn=input("Enter credit card number\n")
            if (len(ccdn)==16):
                break
            else:
                print("Enter a valid input\n")
    s="************"
    for i in range(0,4):
        s=s+str(ccdn[i+12])
    print(s)
credi()
