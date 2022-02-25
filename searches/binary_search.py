def binary_search(li, target):
    # pointers are indices used to determine the range being searched on this iteration
    left = 0
    right = len(li) - 1
    mid = (right + left) // 2

    # loop until there is a return
    while True:
        # if the middle value isn't the target and there is no further division to be done
        if li[mid] != target and len(li[left:right]) <= 1:
            return 'target {0} not found'.format(target)

        # if the target is at the middle index
        if li[mid] == target:
            return 'found target {0} at {1}'.format(target, mid)

        # if the target is greater or less than, split the list
        if target > li[mid]:
            left = mid + 1
            mid = (right + left) // 2
        elif target < li[mid]:
            right = mid
            mid = (right + left) // 2
        
print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 15))
print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 1))
print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 4))


