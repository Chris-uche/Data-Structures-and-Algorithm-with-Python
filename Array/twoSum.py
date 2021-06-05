def twoNumberSum(array, targetSum):
    nums ={}
    for num in array:
        potentialNumber = targetSum - num
        if potentialNumber in nums:
            return [potentialNumber, num]
            #[y,x]
        else:
            nums[num] = True
    return []


def twoNumSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1

    while left < right:
        currentMatch = array[left] + array[right]
        if currentMatch == targetSum:
            return [ array[left], array[right]]
        elif currentMatch < targetSum:
            left +=1
        elif currentMatch > targetSum:
            right -=1
    return []
            
            

