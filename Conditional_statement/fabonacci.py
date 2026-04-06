# 0, 1, (0+1) 1, (1+1) 2, (1+2) 3, (2+3) 5

list_range = list(range(0,11))


l1 = 0
l2 = 1
for i in list_range:
    if i <= 1:
      print(f"cuurentvalue = {i}")
    else:
       s1 = l1 +l2
       print(f"currentvalue = {s1}")
       l1 = l2
       l2 = s1



# #prev_no = 0
# p1 = 0
# p2 = 1
# for val in list_range:
#     #print(val)
#     if val <=1:
#         print(f"fibo = {val}")
#     else:
#        currVal = p1 + p2
#        print(f"fibo = {currVal}")
#        p1 = p2
#        p2 = currVal
       
  
    
