def binarySearch(array,target):
    # create a helper function
    return binarySearchHelper(array,target, 0, len(array)-1)

def binarySearchHelper(array,target,left,right):
    if left > right:
        return -1

    middleValues = (left + right) // 2
    potentialMatch = array[middleValues]
    if target ==  potentialMatch:
        return middleValues
    elif target < potentialMatch:
        return binarySearchHelper(array,target, left, middleValues-1)
    else:
        return binarySearchHelper(array,target, middleValues +1, right)
        



def binarySearchCase(array, target):
    return binarySearchHelper(array, target,0, len(array)-1)
    
def binarySearchHelper(array,target, left, right):
    if left > right:
        return - 1
    middle = (left + right)//2
    #The middle value here denotes the index value
    potentialValue = array[middle]

    if target == potentialValue:
        return middle
    elif target < potentialValue:
        #This is when the target value is less than the potentialvalue
        return binarySearchHelper(array, target, left, middle -1)
    else:
        return binarySearchHelper(array, target, middle + 1,right)
        


def binarySearchCaseThree(array,target):
    return binarySearchHelper(array,target,0, len(array)-1)
    #Implement the method above on the cases

def binarySearchHelper(array, target, left, right):
        if left > right:
            return -1
        middleIndex = (left + right)//2
        potentialIndex = array[middleIndex]

        if target == potentialIndex:
            return middleIndex
        elif target < potentialIndex:
            return binarySearchHelper(array, target, left, middleIndex-1)
        else:
            return binarySearchHelper(array,target,middleIndex+1, right)



def binarySearchCaseFour(array, target):
    return binarySearchHelper(array,target,0, len(array)-1)

def binarySearchHelper(array, target,left,right):
    if left > right:
        return -1
    middle = (left + right)//2
    potentialNum = array[middle]

    if target == potentialNum:
        return middle
    elif target < potentialNum:
        return binarySearchHelper(array, target, left, middle -1)
    else:
        return binarySearchHelper(array,target, middle+1, right)
    




def binarySearchCaseFive(array,target):
    return binarySearchHelper(array, target, 0, len(array)-1)

#Implement the helper method
def binarySearchHelper(array, target, left, right):
    #check for edge cases
    if left > right:
        return -2
    
    middle = (left + right)//2
    potentialIndex = array[middle]

    if target == potentialIndex:
        return middle
    elif target < potentialIndex:
        return binarySearchHelper(array,target,left, middle-1)
    else:
        return binarySearchHelper(array, target, middle+1, right)

        


#Using the iterative method

def binarySearchCaseSix(array,target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array,target,left,right):
    while left <= right:
        middle = (left + right)//2
        potentialIndex = array[middle]
    
        if target == potentialIndex:
            return middle
        elif target < potentialIndex:
            right = middle -1
        else:
            left = middle + 1
    
    return -1



def binarySearchcaseSeven(array, target):
    return binarySearchHelper(array,target, 0, len(array)-1)

def binarySearchHelper(array, target,left, right):
    while left <= right:
        middle = (left + right)//2
        potentialIndex = array[middle]

        if target == potentialIndex:
            return middle
        elif target < potentialIndex:
            right = middle -1
        else:
            left = middle + 1
    return -1
            


