import pygame 
import random

pygame.init()

s_width = 700
s_length = 500
screen = pygame.display.set_mode([s_width, s_length])

black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

array_length = 100
array = []
numColor = []
highestNum = 100

def setup():
    for i in range(array_length):
        array.append(random.randint(1,highestNum))
        numColor.append(0)

def mergeSort(array):
    if len(array) > 1: 
        mid = len(array) // 2
        leftHalfArray = array[:mid]
        rightHalfArray = array[mid:]

        mergeSort(leftHalfArray)
        mergeSort(rightHalfArray)

        merge(array, leftHalfArray, rightHalfArray, mid)

def merge(array, leftArray, rightArray, mid): 
    numColor[]
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


def drawBars():   
    for x in range(len(array)):
        x_value = (s_width/array_length) * x 
        rect_width = s_width/array_length - 1 

        rect_height = (array[x]*(s_length/highestNum)) - 5
        y_value = s_length - rect_height
        
        if numColor[x] == 0:
            pygame.draw.rect(screen, white, [x_value,y_value, rect_width, rect_height]) ##normal bars
        if numColor[x] == 1:
            pygame.draw.rect(screen, green, [x_value,y_value, rect_width, rect_height]) ##boundries of array
        if numColor[x] == 2: 
            pygame.draw.rect(screen, red, [x_value,y_value, rect_width, rect_height]) ##checked/swapped numbers
        if numColor[x] == 3: 
            pygame.draw.rect(screen, blue, [x_value,y_value, rect_width, rect_height]) ##mid
        


def drawScreen():
    screen.fill(black) 
    drawBars()
    pygame.display.update()
    pygame.time.delay(10)

    


i = 1
j = i

setup()
done = False 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)
    
    mergeSort(array)

    pygame.display.flip()

pygame.quit()