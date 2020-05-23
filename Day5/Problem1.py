def replace(a):
    x = int(str(a).replace("0","5"))
    return x

n = int(input("Enter an integer: "))

print("The number after replacing 0s with 5 :", replace(n))

