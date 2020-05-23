def sortEveOd(List):
    eve = []  #even
    od = []   #odd
    for x in List:
        if (x % 2 == 0):
            eve.append(x)
        else :
            od.append(x)
    return sorted(od, reverse = True) + sorted(eve)
n = int(input("Enter the number of elements to add in list: "))
List = []
for i in range(n):
    List.append(int(input("Enter " + str(i + 1) + "st element" + " in the list: ")))
print("The list of numbers after sorting them according to given condition is", str(sortEveOd(List))[1:-1])