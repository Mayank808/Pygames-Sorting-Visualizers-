import pygame 
import random

pygame.init()

s_width = 1500
s_length = 700
screen = pygame.display.set_mode([s_width, s_length])

black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

array_length = 500
array = []
numColor = []
highestNum = 100

def setup():
    for i in range(array_length):
        array.append(random.randint(1,highestNum))
        numColor.append(0)

def partition(array, lowestIndex, highestIndex):
    
    i = (lowestIndex - 1)
    pivotNum = array[highestIndex]

    numColor[highestIndex] = 1 ##pivot
    
    drawScreen()

    for j in range(lowestIndex, highestIndex):
        
        numColor[j] = 2 ##checked num

        if array[j] < pivotNum:
            i += 1 
            numColor[i] = 2 ##swapped num
            array[i] , array[j] = array[j] , array[i]
            drawScreen()
            numColor[i] = 0
        
        numColor[j] = 0

    array[i + 1] , array[highestIndex] = array[highestIndex], array[i + 1]    
    drawScreen()
    numColor[highestIndex] = 0
    numColor[lowestIndex] = 0


    return(i + 1)

def quickSort(array, lowestIndex, highestIndex): 

    if lowestIndex < highestIndex:
        drawScreen()

        piviotIndex = partition(array, lowestIndex, highestIndex)
        
        quickSort(array, lowestIndex, piviotIndex - 1)
        for x in range (0 , piviotIndex + 1): 
            numColor[x] = 3

        quickSort(array, piviotIndex + 1, highestIndex)


def drawBars():   
    for x in range(len(array)):
        x_value = (s_width/array_length) * x 
        rect_width = s_width/array_length - 1 

        rect_height = (array[x]*(s_length/highestNum)) - 5
        y_value = s_length - rect_height
        
        if numColor[x] == 0:
            pygame.draw.rect(screen, white, [x_value,y_value, rect_width, rect_height]) ##normal bars
        if numColor[x] == 1:
            pygame.draw.rect(screen, red, [x_value,y_value, rect_width, rect_height]) ##piviot
        if numColor[x] == 2: 
            pygame.draw.rect(screen, green, [x_value,y_value, rect_width, rect_height]) ##checked/swapped numbers
        if numColor[x] == 3: 
            pygame.draw.rect(screen, blue, [x_value,y_value, rect_width, rect_height]) ##sorted numbers


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
    
    quickSort(array, 0, array_length - 1)

    pygame.display.flip()

pygame.quit()