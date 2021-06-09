def searchInSorted(matrix, target):
    #Keep track of the row and the column we are operating on
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >=0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row +=1
        else:
            return [row, col]
    return [-1,-1]
                

#def searchInsorted(matrix, target):
    #Using the recursive method
    #create a helper method
    #return searchInsortedHelper(matrix, target, 0, len(matrix[0])-1)

#def searchInsortedHelper(matrix, target, row, col):
    #if row < len(matrix) and col > 0:
        #return [-1,-1]

    #if matrix[row][col] > target:
        #return searchInsortedHelper(matrix, target, row, col-1)
    #elif matrix[row][col] < target:
      #  return searchInsortedHelper(matrix,target,row+1, col)
    #else:
       # return [row,col]
    
def searchInsorted(matrix, target):
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >=0:
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -=1
        else:
            return [row,col]

    return [-1,-1]

def searchSorted(matrix,target):
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >=0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return[-1,-1]


