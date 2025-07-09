import pygame 

print('Setup Start')
pygame.init()
windoww = pygame.display.set_mode(size=(600, 480))
print('Setup End') # aqui faço a criação da janela com tamanho especificado

while True:
    #chek all events
    for event in pygame.event.get(): # comando obtido na doc pygame
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            quit() #end pygame

