#factorial()
# def fact(x):
#    if x == 0 or x == 1:
#       return 1
#    print('x',x)
#    return x * fact(x-1)

# print(fact(3))

##Fibonacci series with for

# def fibo(x):
#     p1 = 0
#     p2 = 1
#     for i in x:
#         if i <= 1:
#             print(f"fibo_value : {i}")
#         else:
#             current_value = p1+p2
#             print(f"Fibo_value : {current_value}")
#             p1 = p2
#             p2 = current_value
            
# fibo(range(0,10))


# def fibo(val):
#     #p1 = 0
#     #p2 = 1
#     if val <= 1 :
#         return val
#     return fibo(val-1) + fibo(val-2)
#         #print(f"fibo_value : {current_value}")
#         #fibo = p2
#         #p2 = current_value

# for i in range(10):
#     print(fibo(i))




# def fb(n):
#     if n <=1:
#         return n
#     return fb(n-1) + fb(n-2)

# for i in range(10):
#     print(fb(i))



# def fb(n,m):
#     if n >= m:
#         return 
#     print(n)
#     return fb(n-1) + fb(n-2)
#     #return fb(n-1) + fb(n-2)

# fb(0,8)

#for i in range(10):
 #   print(fb(i))


def fibonacci(n):
   if n <= 1:
      return n
   return fibonacci(n-1) + fibonacci(n-2)

for i in range(8):
    print(fibonacci(i))




