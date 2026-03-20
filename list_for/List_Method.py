print(2+2)

l1 = ['a','b']
print(f"l1 = {l1}, len of l1 = {len(l1)}")

l1.append('c')
print(f"l1 after append = {l1}, len og l1 = {len(l1)}")

l2 = l1

print(f"l2 = l1 and then l2 = {l2}, len l2 = {len(l2)}")

print("-"*10)

l2.clear()

print(f"l2 after clear = {l2}, len of l2 = {len(l2)}")
print(f"l1 after clear = {l1}, len of l1 = {len(l1)}")
print("-"*10)


print()
print("We initiate new value")

l1 = ['Arc','Da_25']

print(f"l1 = {l1}, len l1 = {len(l1)}")

print("-"*10)

l2 = l1.copy()

print(f"l2 = {l2}, len l2 = {len(l2)}")
print("-"*10)

l2.clear()

print(f"l2 after clear = {l2}, len of l2 = {len(l2)}")
print(f"l1 after clear = {l1}, len of l1 = {len(l1)}")

print("--"*40)

e4 = ['Bread','Butter','Milk']
e4.append('Cheeze')
print(f"Extended list : {e4}")
e5 = e4.copy()
print(f"Copied list is : {e5}")
e5.clear()
print(e4)