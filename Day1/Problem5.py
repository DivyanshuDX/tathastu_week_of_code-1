a = int(input("Enter Player1 Score "))
b = int(input("Enter Player2 Score "))
c = int(input("Enter Player3 Score "))

def strike_rate(x):
    rate = (x*100)/60

    return rate

def sixes(x):
    maxim = x/6

    return int(maxim)

print("Strike rate of Player1: " + str(strike_rate(a)))
print("Strike rate of Player1: " + str(strike_rate(b)))
print("Strike rate of Player1: " + str(strike_rate(c)))

print("maximum number of sixes each player could have hit: " + str(sixes(a)))
print("maximum number of sixes each player could have hit: " + str(sixes(b)))
print("maximum number of sixes each player could have hit: " + str(sixes(c)))