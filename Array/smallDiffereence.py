def smallestNumDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    indxOne = 0
    indxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallerPair = []
    while indxOne < len(arrayOne) and indxTwo < len(arrayTwo):
        firstNum = arrayOne[indxOne]
        secondNum = arrayTwo[indxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            indxOne +=1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            indxTwo +=1
        else:
            return[firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallerPair= [firstNum, secondNum]
    return smallerPair

        


def SmallestNumDiff(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    indxOne= 0
    indxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallerNum = []

    while indxOne < len(arrayOne) and indxTwo < len(arrayTwo):
        firstNum = arrayOne[indxOne]
        secondNum = arrayTwo[indxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            indxOne +=1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            indxTwo +=1
        else:
            return[firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallerNum = [firstNum, secondNum]

    return smallerNum