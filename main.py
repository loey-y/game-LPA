import pygame

print('Setup Start')
pygame.init()
print('Setup End')
window = pygame.display.set_mode(size=(600, 480))

print('Loop Start')
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #end pygame
