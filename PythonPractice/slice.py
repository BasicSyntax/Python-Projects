import random

arr = []

for x in range(10):
    arr.append(random.randint(1,100))
    
# tup = ()
# for x in range(10):
#     tup.append(random.randint(1,100))

print(arr)

print(max(arr))
arr.remove(max(arr))
print(max(arr))
arr.sort()

print(arr)
print(arr[-1:-2])

print(arr[5:])

