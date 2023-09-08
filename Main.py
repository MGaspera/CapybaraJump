import pygame
import os
import PublicVariables
import Debug
from PublicVariables import publicVariables

pygame.init()

pygame.display.set_caption("Capybara Jump")
win = pygame.display.set_mode((1280, 768))

# Simple while loop to add controls
run = True
while run:
    # Clear the screen only once at the beginning of each frame
    publicVariables.win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Specify controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and PublicVariables.x > 0:
        PublicVariables.x -= PublicVariables.vel
        lastMove = "L"

    if keys[pygame.K_HASH]:
        Debug.debugMode()


    if keys[pygame.K_RIGHT] and PublicVariables.x < PublicVariables.screenWidth - PublicVariables.width:
        PublicVariables.x += PublicVariables.vel
        lastMove = "R"

    if keys[pygame.K_SPACE] and not isJump:  # Only allow jumping if not already jumping
        isJump = True
        initialY = PublicVariables.y  # Record the initial y-position before jumping

    if isJump:
        if jumpCount >= -10:
            if jumpCount < 0 and not falling:
                PublicVariables.y += (jumpCount * abs(jumpCount)) * PublicVariables.jumpSpeed *2 # Adjust the jump speed here
                falling = True
            else:
                PublicVariables.y -= (jumpCount * abs(jumpCount)) * PublicVariables.jumpSpeed *2 # Adjust the jump speed here
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
            falling = False

    # Draw the (resized) background
    PublicVariables.win.blit(PublicVariables.resizedBg, (0, 0))

    # Draw the player sprite based on movement and direction
    if isJump:
        frameCount = 0  # Reset frame count when jumping
        PublicVariables.win.blit(PublicVariables.standingSprite, (PublicVariables.x, PublicVariables.y))
    elif keys[pygame.K_LEFT]:
        frameCount += 1
        if frameCount >= len(PublicVariables.leftSprites) * PublicVariables.frameDelay:
            frameCount = 0
        currentFrame = PublicVariables.leftSprites[frameCount // PublicVariables.frameDelay]
        PublicVariables.win.blit(currentFrame, (PublicVariables.x, PublicVariables.y))
    elif keys[pygame.K_RIGHT]:
        frameCount += 1
        if frameCount >= len(PublicVariables.rightSprites) * PublicVariables.frameDelay:
            frameCount = 0
        currentFrame = PublicVariables.rightSprites[frameCount // PublicVariables.frameDelay]
        # Flip the sprite horizontally to face right
        currentFrame = pygame.transform.flip(currentFrame, True, False)
        PublicVariables.win.blit(currentFrame, (PublicVariables.x, PublicVariables.y))
    else:
        frameCount = 0  # Reset frame count when standing still
        PublicVariables.win.blit(PublicVariables.standingSprite, (PublicVariables.x, PublicVariables.y))



    # Update the display
    pygame.display.update()

pygame.quit()
