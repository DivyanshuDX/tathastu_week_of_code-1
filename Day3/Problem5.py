lst1 = []
lst2 = []

n = int(input("Enter the number of elements of list1 "))

for i in range(0,n):
    element1 = input()
    
    lst1.append(element1)
    
n = int(input("Enter the number of elements of list2 "))

for i in range(0,n):
    element2 = input()
    
    lst2.append(element2)    
    
print("Original list 1 : " + str(lst1))
print("Original list 2 : " + str(lst2))

add = lst1
for i in range(0,len(lst2)):
    add.append(lst2[i])
    
print("Combined list : " + str(add))

rep = []

for i in add:
    if i not in rep:
        rep.append(i)
        
print("Intersection : " + str(rep))