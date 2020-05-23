from collections import Counter 
  

dit = {'Steve' : [1, 4, 5, 6], 'Bat' : [1, 8, 9], 'Watson': [10, 22, 4], 'Sherlock': [5, 11, 22]} 
  

print("The original dictionary : " + str(dit)) 
  
cnt = Counter() 
for idx in dit.values(): 
    cnt.update(idx) 
res = {idx: [key for key in j if cnt[key] == 1]  
               for idx, j in dit.items()} 
   
print("Uncommon elements records : " + str(res))