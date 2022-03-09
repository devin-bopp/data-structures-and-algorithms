def insertion_sort(li):
    # cycle through indexes in the list, excluding the first index, which we consider sorted
    for i in range(1, len(li)):
        # the key is the element being inserted
        key = li[i]
        # j is the index immediately prior to the current key
        j = i - 1

        # while statement checks: are there j values remaining AND is the current key less than is previous value?
        while j >= 0 and key < li[j]:
            # if yes
            li[j + 1] = li[j]
            j =  j - 1

        li[j+ 1] = key
list = [5,8,1,4]
insertion_sort(list)
print(list)