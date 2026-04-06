#l1 = [2,6,60,80,55,13,22]

#for l1value in l1:
 #   if l1value > 50:
  #      print(f"l1value = {l1value} is gt 50")
   # else:
    #    print(f"l1value = {l1value} is lt 50")
#################################################################

l1 = list(range(1,100))

l2 = [] # even list
l3 = [] # odd list
for i in l1:
    if i%2 == 0:
        l2.append(i)
        #print(f"i = {i} is even")
    else:
        l3.append(i)
        #print(f"i = {i} is odd")
        
print(f"l2 : {l2}")
print()
print()
print( f"l3 : {l3}")



