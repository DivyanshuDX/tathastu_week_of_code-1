lst = [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)] 
   
print("The original list is : " + str(lst)) 
  
N = 1
 
lst.sort(key = lambda x: x[N]) 
  
# printing result  
print("List after sorting tuple by Nth index sort : " + str(lst)) 