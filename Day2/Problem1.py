a = int(input("Enter an Integer "))

def even(a):
    if (a%2==0):
        print("Even")
    else:
         print("Odd")

def prime(a):
    if (a>1):
        for i in range(2,a):
            if (a % i) == 0:
                print(a," is not a prime number")
                break
        else:
            print(a," is a prime number")

    else:
        print(a," is not prime number")

def palindrome(a):
    return a == a[::-1]


def armstrong(a):
    sum = 0

    temp = a
    while temp > 0:
        rem = temp%10
        sum += rem**3
        temp //=10
    
    if a == sum:
        print(a," is a armstrong number")
    else:
        print(a," is not an Armstrong number")

even(a)
prime(a)

x = palindrome(str(a))
if a:
    print(a,"is Palindrome")
else:
    print(a,"is not Palindrome ")

armstrong(a)



