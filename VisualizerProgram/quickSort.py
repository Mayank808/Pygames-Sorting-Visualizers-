import pygame
import settings as s 

def partition(array, lowestIndex, highestIndex):
    
    i = (lowestIndex - 1)
    pivotNum = array[highestIndex]

    s.numColor[highestIndex] = 1 ##pivot
    
    s.drawScreen()

    for j in range(lowestIndex, highestIndex):
        
        s.numColor[j] = 2 ##checked num

        if array[j] < pivotNum:
            i += 1 
            s.numColor[i] = 2 ##swapped num
            array[i] , array[j] = array[j] , array[i]
            s.drawScreen()
            s.numColor[i] = 0
        
        s.numColor[j] = 0

    array[i + 1] , array[highestIndex] = array[highestIndex], array[i + 1]    
    s.drawScreen()
    s.numColor[highestIndex] = 0
    s.numColor[lowestIndex] = 0


    return(i + 1)

def quickSort(array, lowestIndex, highestIndex): 

    if lowestIndex < highestIndex:
        s.drawScreen()

        piviotIndex = partition(array, lowestIndex, highestIndex)
        
        quickSort(array, lowestIndex, piviotIndex - 1)
        for x in range (0 , piviotIndex + 1): 
            s.numColor[x] = 3

        quickSort(array, piviotIndex + 1, highestIndex)