import pygame
pygame.init()
import time
from time import sleep
 
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
screenWidth = 500
screenHeight = 500

# Set the paramaters for drawing the rectangle
x = 50
y = 50
width = 50
height = 50
vel = 5

# Variables that allow the player to jump
isJump = False
jumpCount = 10

# Simple while loop to add controls to the 
run = True
while run == True:
    pygame.time.delay(100)
    
    # If the quit button is pressed, close window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Specify controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0: #this makes sure that the block will not leave the screen if a movement takes place.
        x -= vel

    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += vel
    
    if not(isJump): 
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:  # This will execute if our jump is finished, resetting the variables.
            jumpCount = 10
            isJump = False 
    #Everytime that a movement happens, the rest of the screen should fill to black.
    win.fill ((0,0,0))
    # Draw in a rectangle, then update the screen so it is visible
    pygame.draw.rect(win, (8, 193, 255) , (x,y, width, height))
    pygame.display.update()
pygame.quit