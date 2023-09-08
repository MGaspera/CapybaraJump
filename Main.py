import pygame
import os
import Classes
import Debug
from Classes import win, assets, player, fonts

pygame.init()

# Class instances
font = fonts()
myPlayer = player()
window = win()
asset = assets()

pygame.display.set_caption("Capybara Jump")

# Simple while loop to add controls
run = True
debugOn = False
debug_cooldown = 0  # Add a cooldown timer
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Specify controls
    keys = pygame.key.get_pressed()

    # Update game state
    if keys[pygame.K_LEFT] and myPlayer.x > 0:
        myPlayer.x -= myPlayer.vel
        myPlayer.lastMove = "L"  # Update lastMove for left movement
        asset.frameCount += 1
        if asset.frameCount >= len(asset.leftSprites) * asset.frameDelay:
            asset.frameCount = 0  # Reset frame count for left movement

    if keys[pygame.K_HASH]:
        # Check if debug mode cooldown is over
        if debug_cooldown == 0:
            debugOn = not debugOn
            debug_cooldown = 30  # Set cooldown to 30 frames (adjust as needed)
            print("Debug mode toggled!")

    # Decrement the cooldown timer
    if debug_cooldown > 0:
        debug_cooldown -= 1

    if keys[pygame.K_RIGHT] and myPlayer.x + myPlayer.width + myPlayer.vel < window.screenWidth:
        myPlayer.x += myPlayer.vel
        myPlayer.lastMove = "R"  # Update lastMove for right movement
        asset.frameCount += 1
        if asset.frameCount >= len(asset.rightSprites) * asset.frameDelay:
            asset.frameCount = 0  # Reset frame count for right movement

    if keys[pygame.K_SPACE] and not myPlayer.isJump:  # Only allow jumping if not already jumping
        myPlayer.isJump = True
        initialY = myPlayer.y  # Record the initial y-position before jumping

    if myPlayer.isJump:
        if myPlayer.jumpCount >= -10:
            if myPlayer.jumpCount < 0 and not myPlayer.falling:
                myPlayer.y += (myPlayer.jumpCount * abs(myPlayer.jumpCount)) * myPlayer.jumpSpeed * 3  # Adjust the jump speed here
                myPlayer.falling = True
            else:
                myPlayer.y -= (myPlayer.jumpCount * abs(myPlayer.jumpCount)) * myPlayer.jumpSpeed * 3
            myPlayer.jumpCount -= 1
        else:
            myPlayer.jumpCount = 10
            myPlayer.isJump = False
            myPlayer.falling = False

    # Clear the screen
    window.windowSize.fill((0, 0, 0))

    # Draw the (resized) background
    window.windowSize.blit(asset.resizedBgImg, (0, 0))

    #jumping
    if myPlayer.isJump:
        myPlayer.frameCount = 0  # Reset frame count when jumping
        if myPlayer.lastMove == "L":  # Check the last move direction
            # Draw the jumping sprite facing left
            window.windowSize.blit(pygame.transform.flip(myPlayer.standingSprite, True, False), (myPlayer.x, myPlayer.y))
        else:
            # Draw the jumping sprite facing right
            window.windowSize.blit(myPlayer.standingSprite, (myPlayer.x, myPlayer.y))
    elif keys[pygame.K_LEFT]:
        asset.leftFrameCount += 1
        myPlayer.lastMove = "L"
        if asset.leftFrameCount >= len(myPlayer.leftSprites) * asset.frameDelay:
            asset.leftFrameCount = 0
        window.windowSize.blit(myPlayer.leftSprites[asset.leftFrameCount // asset.frameDelay], (myPlayer.x, myPlayer.y))
    elif keys[pygame.K_RIGHT]:
        asset.rightFrameCount += 1
        myPlayer.lastMove = "R"
        if asset.rightFrameCount >= len(myPlayer.rightSprites) * asset.frameDelay:
            asset.rightFrameCount = 0
        myPlayer.currentFrame = myPlayer.rightSprites[asset.rightFrameCount // asset.frameDelay]
        myPlayer.currentFrame = pygame.transform.flip(myPlayer.currentFrame, True, False)
        window.windowSize.blit(myPlayer.currentFrame, (myPlayer.x, myPlayer.y))
    else:
        myPlayer.frameCount = 0  # Reset frame count when standing still
        if myPlayer.lastMove == "L":  # Check the last move direction
            # Draw the standing sprite facing left
            window.windowSize.blit(pygame.transform.flip(myPlayer.standingSprite, True, False), (myPlayer.x, myPlayer.y))
        else:
            # Draw the standing sprite facing right
            window.windowSize.blit(myPlayer.standingSprite, (myPlayer.x, myPlayer.y))
    # Draw the debug information if debug mode is enabled
    if debugOn:
        Debug.debugMode()

    # Update the display once per frame
    pygame.display.update()

pygame.quit()
