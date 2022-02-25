def quicksort(li):
    # pivot is the final item in the list
    pivot = li[-1]
    left = []
    right = []
    # cycle through all elements EXCEPT the pivot
    for i in range(len(li)-1):
        # if the number is larger than the pivot, put it in the right
        if li[i] > pivot:
            right.append(li[i])
        # otherwise, put it in the left
        else:
            left.append(li[i])
    # if either the left or right array has more than one value, run them through again
    if len(right) > 1:
        right = quicksort(right)
    if len(left) > 1:
        left = quicksort(left)
    
    return left + [pivot] + right

from test_lists.test_lists import test_list

import timeit

my_setup = '''
from test_lists import test_list
def quicksort(li):
    # pivot is the final item in the list
    pivot = li[-1]
    left = []
    right = []
    # cycle through all elements EXCEPT the pivot
    for i in range(len(li)-1):
        # if the number is larger than the pivot, put it in the right
        if li[i] > pivot:
            right.append(li[i])
        # otherwise, put it in the left
        else:
            left.append(li[i])
    # if either the left or right array has more than one value, run them through again
    if len(right) > 1:
        right = quicksort(right)
    if len(left) > 1:
        left = quicksort(left)
    
    return left + [pivot] + right
'''

my_code = '''
quicksort([8,5,4,7,9,1])
'''

print(timeit.timeit(setup = my_setup, stmt = my_code, number = 1000000))