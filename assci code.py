# cook your dish here
a = int(input())
for i in range(a):
    N,K = map(int, input().split())
    o =input()
    cap = 0
    small = 0
    x = [char for char  in o]
    for k in x:
        p = ord(k)

    if (p >= 65 and p <= 90):
         cap = cap + 1
    else:
        small = small + 1

    if(cap==small):
        if(K>=cap):
            print("both")
        elif(k<cap):
            print("none")
    elif(small>cap):
        if(k>=small):
            print("both")
        elif(k<cap):
            print("none")
        else:
            print("chef")

    elif(cap>small):
        if(k>=cap):
           print("both")
        elif(k<small):
            print("none")
        else:
            print("brother")

