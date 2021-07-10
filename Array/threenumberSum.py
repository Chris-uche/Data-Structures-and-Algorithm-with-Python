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
            elif currentSum > targetSum:
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
                
                
def ThreenumberSum(array, target):
    array.sort()
    triplets = []

    for l in range(len(array)-2):
        left = l + 1
        right= len(array)-1
        while left < right:
            currentSum = array[l] + array[left] + array[right]
            if currentSum == target:
                triplets.append([array[l],array[left],array[right]])
                left +=1
                right -=1
            elif currentSum < target:
                left +=1
            elif currentSum > target:
                right -=1
    return triplets



def ThreeNumberSum(array, targetSum):
    tripleArray=[]
    array.sort()

    for i in range(len(array)-2):
        left = 1 +1
        right = len(array)-1
        while left < right:
            currentSum = array[1] + array[left] + array[right]
            if currentSum == targetSum:
                tripleArray.append([array[i],array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left +=1
            elif currentSum > targetSum:
                right -=1

        return tripleArray
                                


                
                