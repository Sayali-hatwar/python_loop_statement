# 0, 1, (0+1) 1, (1+1) 2, (1+2) 3, (2+3) 5

list_range = list(range(0,11))

list_range[1]

prev_no = 0

for val in list_range:
    #print(val)
    if val <=1:
        print(val)
    else:
       s = prev_no + val
       print(s)
  
    print("--"*4)
    prev_no = val


# 0 0
# 1 1
# 1 2, 2-1 = 1, 2-2 = 0
# 2 3, 3-2 = 1, 3-2 = 1 == 2
# 3 4, 4-3 = 1, 4-2 = 2 == 3
# 5 5, 
# 8 6,
# 13 7,