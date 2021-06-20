def moveElemsToEnd(array, toMoveNum):
    #define our pointers
    i = 0
    j = len(array)-1

    #the code is to break when this condition is meet
    while i < j:
        while i < j and array[j] == toMoveNum:
            j -= 1
        if array[i] == toMoveNum:
            array[i], array[j] = array[j], array[i]
            #After we swap the values here we increment by 1
            i +=1

    return array
        



def MoveELementToTheEnd(array,toMoveValue):
    i = 0
    j = len(array)-1

    while i < j:
        while i < j and array[j] == toMoveValue:
            j -=1
        if array[i] == toMoveValue:
            array[i], array[j] == array[j], array[i]
            i += 1
    return array



def moveEleToTheEnd(array, toMoveNumber):
    i = 0
    j = len(array)-1

    while i < j:
        while i < j and array[j] == toMoveNumber:
            j -=1
        if array[i] == toMoveNumber:
            array[i], array[j] == array[j], array[i]
            i +=1
    return array