from test_lists import test_list

# linear search for finding the first instance
def linear_search(li, target):
    for idx in range(len(li)):
        if li[idx] == target:
            return idx
    return -1

print(linear_search(test_list, 700))

def linear_dupe_search(li, target):
    results = []

    for idx in range(len(li)):
        if li[idx] == target:
            results.append(idx)
    
    if not results:
        return 'not found'
    else:
        return results

print(linear_dupe_search([1,2,3,4,5,2,1,1,1], 8))