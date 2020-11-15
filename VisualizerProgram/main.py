import pygame 
import random 
import settings as s
import quickSort as quick
import bubbleSort as bubble

s.init()
pygame.init()

def setup():
    for number in range(s.array_length):
        s.array.append(random.randint(1 , s.highestNum))
        s.numColor.append(0)

def main():
    setup()
    screen = s.screen
    isStart = False
    done = False 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    s.array.clear()
                    s.numColor.clear()
                    setup()
                if event.key == pygame.K_q:
                    isStart = True
                    sortType = 0
                if event.key == pygame.K_b:
                    isStart = True
                    sortType = 1


        screen.fill(s.Colors[0])

        if not isStart:
            s.drawScreen()
        else:
            if sortType == 0:
                quick.quickSort(s.array, 0, len(s.array) - 1)
            if sortType == 1: 
                bubble.bubbleSort(s.array)
                



        pygame.display.flip()

    pygame.quit()





if __name__ == "__main__":
    main()