# recursive bubble sort
def bubblesort(li):
    # used to determine whether the list is fully sorted
    swapped = False
    
    for idx in range(len(li)):
        if idx != len(li) - 1 and li[idx] > li[idx + 1]:
            bookmark = li[idx]
            li[idx] = li[idx + 1]
            li[idx + 1] = bookmark
            swapped = True
    # if no swaps were performed, the list is sorted (base case)
    if not swapped:
        return li
    # if the list is not sorted, recursively call bubblesort
    else:
        return bubblesort(li)
    
sorted = bubblesort(['dog', 'cat', 'house', 'zebra', 'hen'])
print(sorted)
