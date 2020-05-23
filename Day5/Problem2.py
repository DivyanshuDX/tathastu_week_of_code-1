def replaceInteger(l):
    for i in range(n-1):
        l[i] = max(l[i+1:])
    return l
n = int(input("Enter the size of the list: "))
l = []
for i in range(n):
    l.append(int(input("Enter the element number " + str(i+1) + " in the List: ")))
print("The list after replacing element with greatest element on right side is: ", replaceInteger(l))
