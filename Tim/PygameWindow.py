# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 09:21:56 2022

@author: timot
"""
import pygame
pygame.init()



white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

background_colour = (100,100,100)
(width, height) = (900, 600)
display_surface = pygame.display.set_mode((width, height))
pygame.display.flip()
display_surface.fill(background_colour)
pygame.display.set_caption('Skwat Simulator 2022 - GOTY edition')


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score :', True, green, blue)

textRect = text.get_rect()
 
textRect.center = (width // 2, height // 2)


imp = pygame.image.load("SquatUp.png").convert()
imp2 = pygame.image.load("SquatDown.png").convert()


done = False
running = True
score = 0

while running:
    ###Your code here
    
    
    display_surface.blit(imp2, (0,0))
    pygame.display.update()
    #Put voice generation bit here
    display_surface.blit(imp, (0,0))
    
    
    

    display_surface.blit(text, textRect)
    pygame.display.update()
    #score+=1
    text = font.render('Score :' + str(score), True, green, blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
                running = False
                break # break out of the for loop
    if done:
        break 

pygame.display.quit()
pygame.quit()
    

    

      
