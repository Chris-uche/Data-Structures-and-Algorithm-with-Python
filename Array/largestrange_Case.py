def longestRange(array):
    bestRange = []
    longestRange = 0
    nums ={}
    #We traverse every number in the array,
    for num in array:
        #We set every number in the hash table to be True  by default
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False