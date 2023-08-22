import random
import time


def naive_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1


def binary_search(my_list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(my_list) - 1

    if high < low:
        return -1

    mid_point = (low + high) // 2

    if target == my_list[mid_point]:
        return mid_point
    elif target < my_list[mid_point]:
        return binary_search(my_list, target, low, mid_point-1)
    else:
        return binary_search(my_list, target, mid_point+1, high)


length = 10000

sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list))

start_1 = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
duration_1 = time.time() - start_1
print(f"Naive search time: {duration_1:.4f} seconds")

start_2 = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
duration_2 = time.time() - start_2
print(f"Binary search time: {duration_2:.4f} seconds")

print(f"Difference: {duration_1 - duration_2:.2f} seconds")
