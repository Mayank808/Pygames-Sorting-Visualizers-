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

clock = pygame.time.Clock()

array_length = 10
array = []
highestNum = 100

def setup():
    for i in range(array_length):
        array.append(random.randint(1,highestNum))

def insertionSort():
    if array[j - 1] > array[j]:
        array[j] , array[j - 1] = array[j - 1] , array[j]
        

i = 1
j = i

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
        if i == array_length - 1 and j == 0:
            pygame.draw.rect(screen, green, [x_value,y_value, rect_width, rect_height])
        elif x is j or x is j - 1 :
            pygame.draw.rect(screen, red, [x_value,y_value, rect_width, rect_height])
        elif x is i: 
            pygame.draw.rect(screen, green, [x_value,y_value, rect_width, rect_height])
        else: 
            pygame.draw.rect(screen, white, [x_value,y_value, rect_width, rect_height])
        

    if j > 0:
        insertionSort()
        j -= 1
    elif i < array_length - 1: 
        i += 1
        j = i

    pygame.display.flip()

    clock.tick(10)

pygame.quit()