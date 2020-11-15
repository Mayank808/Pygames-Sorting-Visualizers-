import pygame
import settings as s 

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                s.numColor[j] = 2
                s.numColor[j + 1] = 2
                array[j], array[j + 1] = array[j + 1], array[j]
                s.drawScreen()
                s.numColor[j] = 0
                s.numColor[j + 1] = 0






