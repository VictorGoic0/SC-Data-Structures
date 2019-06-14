import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

names_2_values = {}

for name in names_2:
    names_2_values[name] = name
for name in names_1:
    if name in names_2_values:
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# stretch

# def merge(arrA, arrB):
#     merged_arr = []
#     while len(arrA) > 0 and len(arrB) > 0:
#       if len(arrA[0]) < len(arrB[0]):
#         merged_arr.append(arrA[0])
#         arrA.pop(0)
#       else:
#         merged_arr.append(arrB[0])
#         arrB.pop(0)
#     while len(arrA) > 0:
#       merged_arr.append(arrA[0])
#       arrA.pop(0)
#     while len(arrB) > 0:
#       merged_arr.append(arrB[0])
#       arrB.pop(0)
#     return merged_arr

# import math 
# def merge_sort(arr):
#   if (len(arr) <= 1):
#     return arr
#   else:
#     midpoint = math.floor(len(arr) / 2)
#     left = arr[0:midpoint]
#     right = arr[midpoint:len(arr)]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return merge(left, right)

# names_2_sorted = merge_sort(names_2)

# def binary_search(arr, target):
#         while len(arr) > 1:
#                 midpoint = len(arr) // 2
#                 if len(arr[midpoint]) == len(target):
#                         # if len(arr[midpoint - 1]) < len(target):
#                         #         arr = arr[midpoint:]
#                         # elif len(arr[midpoint + 1]) > len(target):
#                         #         arr = arr[:midpoint+1]
#                         for name in arr:
#                                 if name == target:
#                                         return True
#                         return False
#                 else:
#                         if len(arr[midpoint]) > len(target):
#                                 arr = arr[0:midpoint]
#                         elif len(arr[midpoint]) < len(target):
#                                 arr = arr[midpoint: len(arr)]
#         if arr[0] == target:
#                 return True
#         else:
#                 return False
        
# for name in names_1:
#         if binary_search(names_2, name):
#                 duplicates.append(name)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

