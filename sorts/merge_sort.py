def merge_sort(li):
    # identify the middle index
    mid_idx = len(li) // 2
    # split it in two
    left = li[:mid_idx]
    right = li[mid_idx:]
    # call merge sort on the left and right sides
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    # create iterators for each side
    i_left = 0
    i_right = 0

    # create iterator for the sorted array
    i_sorted = 0

    # merge them together in order
    while i_left < len(left) and i_right < len(right):
        if left[i_left] <= right[i_right]:
            li[i_sorted] = left[i_left]
            i_left += 1
        else:
            li[i_sorted] = right[i_right]
            i_right += 1
        i_sorted += 1

    # if one list is used up, add the rest of the other
    while i_left < len(left):
        li[i_sorted] = left[i_left]
        i_sorted += 1
        i_left += 1
    
    while i_right < len(right):
        li[i_sorted] = right[i_right]
        i_sorted += 1
        i_right += 1

    return li

test_list = [10, 1, 3, 158, 14000, 34, 24, 3, 899, 1]
print(merge_sort(test_list))
