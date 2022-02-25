from test_lists import test_list

def linear_search(li, target):
    for idx in range(len(li)):
        if li[idx] == target:
            return idx
    return -1

print(linear_search(test_list, 700))