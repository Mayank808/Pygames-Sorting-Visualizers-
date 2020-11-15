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
orange = (255,165,0)

clock = pygame.time.Clock()

array_length = 20
array = []
highestNum = 20

def setup():
    for number in range(array_length):
        array.append(random.randint(1 , highestNum))

def selectionCheck():
    global intMinSwap
    global j
    if array[intMinSwap] > array[j]:
        intMinSwap = j

def selectionSwap(intMinSwap, i):
    array[i] , array[intMinSwap] = array[intMinSwap] , array[i] 

i = 0
j = i + 1  
intMinSwap = i

setup()
done = False 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)
    
    for x in range(len(array)):
        x_value = (s_width/array_length) * x 
        rect_width = s_width/array_length - 1 

        rect_height = (array[x]*(s_length/highestNum)) - 5
        y_value = s_length - rect_height
        if i == array_length - 2: 
            pygame.draw.rect(screen, orange, [x_value,y_value, rect_width, rect_height])
        elif x is j:
            pygame.draw.rect(screen, green, [x_value,y_value, rect_width, rect_height])
        elif x is intMinSwap: 
            pygame.draw.rect(screen, red, [x_value,y_value, rect_width, rect_height])
        elif x < i:
            pygame.draw.rect(screen, orange, [x_value,y_value, rect_width, rect_height])
        else: 
            pygame.draw.rect(screen, white, [x_value,y_value, rect_width, rect_height])

    selectionCheck()
    
    if j < array_length - 1:
        j += 1
    elif i < array_length - 2: 
        selectionSwap(intMinSwap, i)
        i += 1
        j = i + 1
        intMinSwap = i 

    pygame.display.flip()

    clock.tick(10)

pygame.quit()