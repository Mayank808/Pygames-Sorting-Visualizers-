import pygame 
import random

pygame.init()

s_width = 700
s_length = 500
screen = pygame.display.set_mode([s_width, s_length])

black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)

clock = pygame.time.Clock()

array_length = 30
array = []
highestNum = 100

def setup():
    for i in range(array_length):
        array.append(random.randint(1 , highestNum))

def bubbleSort():
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

setup()
done = False 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)
    
    for i in range(len(array)):
        x_value = (s_width/array_length) * i 
        rect_width = s_width/array_length - 1 

        rect_height = (array[i]*(s_length/highestNum)) - 5
        y_value = s_length - rect_height
        
        pygame.draw.rect(screen, white, [x_value,y_value, rect_width, rect_height])


    bubbleSort()

    pygame.display.flip()

    clock.tick(1)

pygame.quit()