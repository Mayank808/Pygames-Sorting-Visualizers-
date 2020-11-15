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

array_length = 100
array = []
highestNum = 100

def setup():
    for i in range(array_length):
        array.append(random.randint(1,highestNum))

def bubble_sort():
    if array[j] > array[j+1]:
        array[j] , array[j+1] = array[j+1], array[j]
        

j = 0
i = 0
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
        if x is j:
            pygame.draw.rect(screen, green, [x_value,y_value, rect_width, rect_height])
        else: 
            pygame.draw.rect(screen, white, [x_value,y_value, rect_width, rect_height])
        

    bubble_sort()

    if j < array_length - i - 1:
        j += 1
    elif i <= array_length: 
        i += 1
        j = 0
    if j + 1 > array_length - 1:
        print("break")
        i += 1
        j = 0

    pygame.display.flip()

    clock.tick(60)

pygame.quit()