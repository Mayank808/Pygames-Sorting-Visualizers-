import pygame 

def init():
    print('hello')
    global array 
    global array_length
    global highestNum
    global delay
    global numColor
    global Colors
    global s_length
    global s_width 
    global screen

    s_width = 700
    s_length = 500
    screen = pygame.display.set_mode([s_width, s_length])

    array = []
    numColor = []
    array_length = 50
    highestNum = 500
    delay = 30

    # 0 Black, 1 White, 2 Red, 3 Green, 4 Blue, 5 Orange
    Colors = [(0,0,0),(255,255,255),(255,0,0),(0,255,0), (0,0,255), (255,165,0)]

def drawScreen():
    global Colors
    global delay 
    screen.fill(Colors[0]) 
    drawBars()
    pygame.display.update()
    pygame.time.delay(delay)

def drawBars():   
    global array_length
    global s_width
    global s_length
    global screen
    global Colors
    global array
    for x in range(len(array)):
        x_value = (s_width / array_length) * x 
        rect_width = (s_width / array_length) - 1 

        rect_height = (array[x] * (s_length / highestNum)) - 5
        y_value = s_length - rect_height
        
        if numColor[x] == 0:
            pygame.draw.rect(screen, Colors[1], [x_value,y_value, rect_width, rect_height]) ##normal bars
        if numColor[x] == 1:
            pygame.draw.rect(screen, Colors[3], [x_value,y_value, rect_width, rect_height]) ##boundries of array
        if numColor[x] == 2: 
            pygame.draw.rect(screen, Colors[2], [x_value,y_value, rect_width, rect_height]) ##checked/swapped numbers
        if numColor[x] == 3: 
            pygame.draw.rect(screen, Colors[4], [x_value,y_value, rect_width, rect_height]) ##mid
        
    
