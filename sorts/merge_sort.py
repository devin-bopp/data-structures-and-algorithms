def merge_sort(li):
    # identify the middle index
    mid_idx = len(li) // 2

    # split it in two
    left = li[:mid_idx]
    right = li[mid_idx:]

    # call merge sort on the left and right sides until the are each one item long
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    # create iterators for each side
    i = 0
    j = 0

    # create iterator for the sorted array
    k = 0

    # merge them together in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            li[k] = left[i]
            i += 1
        else:
            li[k] = right[j]
            j += 1
        k += 1

    # if one list is used up, add the rest of the other
    while i < len(left):
        li[k] = left[i]
        k += 1
        i += 1
    
    while j < len(right):
        li[k] = right[j]
        k += 1
        j += 1

    return li

test_list = [10, 1, 3, 158, 14000, 34, 24, 3, 899, 1]
print(merge_sort(test_list))
print(test_list)