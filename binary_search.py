import random
import time

# the linear search function
def naive_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1

# the recursive binary search function
def binary_search(my_list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(my_list) - 1

    if high < low: # when the target is not in the list
        return -1

    mid_point = (low + high) // 2

    if target == my_list[mid_point]:
        return mid_point
    elif target < my_list[mid_point]: # continue searching in left half
        return binary_search(my_list, target, low, mid_point-1)
    else: # continue searching in right half
        return binary_search(my_list, target, mid_point+1, high)



# creating a sorted list
length = 10_000

sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list))

# comparing the execution time of the two functions, where each number in the list is searched in an iterative manner using either of the functions

# with linear search
start_1 = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
duration_1 = time.time() - start_1
print(f"Naive search time: {duration_1:.4f} seconds")

# with binary search
start_2 = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
duration_2 = time.time() - start_2
print(f"Binary search time: {duration_2:.4f} seconds")

# final comparison
print(f"Difference: {duration_1 - duration_2:.2f} seconds")
