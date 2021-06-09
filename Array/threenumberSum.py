def threenumberSum(array, targetSum):
    array.sort()
    triplet = []

    for i in range(len(array)-2):

        left = i + 1
        right = len(array)-1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplet.append([array[i], array[left], array[right]])
                #because the array is sorted in an orderly manner
                left +=1
                right -=1
            elif currentSum < targetSum:
                left +=1
            elif currentSum > targerSum:
                right -=1

    return triplet
                
def threeNumSum(array, targetSum):
    array.sort()
    theTriplet =[]

    for k in range(len(array)-2):
        left = k + 1
        right = len(array)-1
        while left < right:
            currentSum = array[k] + array[left] + array[right]
            if currentSum == targetSum:
                theTriplet.append([array[k], array[left], array[right]])
                left +=1
                right -=1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1

    return theTriplet
                
                
