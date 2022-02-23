def bubblesort(li):
    # this is used to determine whether the list needs to reset
    swapped = False
    
    for idx in range(len(li)):
        if idx != len(li) - 1 and li[idx] > li[idx + 1]:
            bookmark = li[idx]
            li[idx] = li[idx + 1]
            li[idx + 1] = bookmark
            swapped = True
    if not swapped:
        return li
    else:
        swapped = False
        return bubblesort(li)
    

import timeit

my_setup = '''
from test_lists import test_list
def bubblesort(li):
    # this is used to determine whether the list needs to reset
    swapped = False
    
    for idx in range(len(li)):
        if idx != len(li) - 1 and li[idx] > li[idx + 1]:
            bookmark = li[idx]
            li[idx] = li[idx + 1]
            li[idx + 1] = bookmark
            swapped = True
    if not swapped:
        return li
    else:
        swapped = False
        return bubblesort(li)
'''

my_code = '''
bubblesort([8,5,4,7,9,1])
'''

print(timeit.timeit(setup = my_setup, stmt = my_code, number = 1000000))