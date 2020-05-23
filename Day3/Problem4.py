lst = []

n = int(input("Enter the number of elements "))

for i in range(0,n):
    element = input()
    
    lst.append(element)

print("Entered list is : "+ str(lst))

rep = []

for i in lst:
    if i not in rep:
        rep.append(i)
        
print("The list after removing duplicates: " + str(rep))