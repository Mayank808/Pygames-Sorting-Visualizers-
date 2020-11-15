import random 

def setup(array):
    for i in range(10):
        array.append(random.randint(1,10))

def mergeSort(array, leftIndex, rightIndex):
    if leftIndex < rightIndex: 
        mid = leftIndex + (rightIndex - 1) // 2 
        mergeSort(array, leftIndex, mid)
        mergeSort(array, mid + 1, rightIndex)

        merge(array, leftIndex, mid, mid+1, rightIndex)

def merge(array, leftStart, mid, rightStart, rightEnd):
    
    if array[leftStart] <= array[rightStart]:
        return; 
    
    while leftStart <= mid and rightStart <= rightEnd:

        if array[leftStart] <= array[rightStart]: 
            leftStart += 1
        else: 
            value = array[rightStart]
            index = rightStart
            
            while index != leftStart: 
                array[index] = array[index - 1] 
                index -= 1
            
            array[leftStart] = value

            leftStart += 1
            mid += 1
            rightStart += 1


array = []
setup(array)
print(array)
mergeSort(array, 0, len(array) - 1)