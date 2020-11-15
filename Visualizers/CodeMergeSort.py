import random

def mergeSort(array):
    if len(array) > 1: 
        mid = len(array) // 2
        leftHalfArray = array[:mid]
        rightHalfArray = array[mid:]

        mergeSort(leftHalfArray)
        mergeSort(rightHalfArray)

        merge(array, leftHalfArray, rightHalfArray)

def merge(array, leftArray, rightArray): 
      
    i = j = k = 0
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        

        k += 1

    while i < len(leftArray): 
        array[k] = leftArray[i] 
        i+= 1
        k+= 1
        
    while j < len(rightArray): 
        array[k] = rightArray[j] 
        j+= 1
        k+= 1


def setup(array):
    for i in range(10):
        array.append(random.randint(1,10))


array = []
setup(array)
print(array)
mergeSort(array)
print(array)