a=3;b=1;n= 5
for i in range(n,0,-2):
    for j in range(1,i+1):
        if(j%2!=0):
            print(str(a),end="")
        else:
            print("*",end="")
    a-=1
    print()
for i in range(1,n+1,2):
    for j in range(1,i+1):
        if(j%2!=0):
            print(str(b),end="")
        else:
            print("*",end="")
    b+=1
    print()