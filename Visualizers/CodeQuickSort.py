import random

def partition(array, lowestIndex, highestIndex):
    
    i = (lowestIndex - 1)
    pivotNum = array[highestIndex]

    for j in range(lowestIndex, highestIndex):
    
        if array[j] < pivotNum:
            i += 1 
            array[i] , array[j] = array[j] , array[i]
    
    array[i + 1] , array[highestIndex] = array[highestIndex], array[i + 1]
    
    return(i + 1)

def quickSort(array, lowestIndex, highestIndex): 
    if lowestIndex < highestIndex:

        piviotIndex = partition(array, lowestIndex, highestIndex)

        quickSort(array, lowestIndex, piviotIndex - 1)
        quickSort(array, piviotIndex + 1, highestIndex)
        
def setup(array):
    for i in range(10):
        array.append(random.randint(1,10))

array = []
setup(array)
print(array)

quickSort(array, 0, 9)

print(array) 
