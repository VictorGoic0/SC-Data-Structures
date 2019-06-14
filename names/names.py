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
#       if arrA[0] < arrB[0]:
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
#     left = arr[:midpoint]
#     right = arr[midpoint:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return merge(left, right)

# names_2_sorted = merge_sort(names_2)
        
# def binary_search(arr, target):
# 	    left = 0
# 	    right = len(arr) - 1
# 	    found = False
	
# 	    while left <= right and not found:
# 	        midpoint = (left + right) // 2
# 	        if arr[midpoint] == target:
# 	            found = True
# 	        else:
# 	            if target < arr[midpoint]:
# 	                right = midpoint-1
# 	            else:
# 	                left = midpoint+1
	
# 	    return found

# for name in names_1:
#         if binary_search(names_2, name):
#                 duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

