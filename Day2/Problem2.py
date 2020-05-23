n = int(input("Enter the number of terms "))

n1 = 0
n2 = 1
count = 0

if n <= 0:
    print("Enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto",n)
    print(n1)
else:
    print("Fibonacci sequence upto",n)
    while count < n:
        print(n1)
        new = n1 + n2
        n1 = n2
        n2 = new

        count += 1

    
