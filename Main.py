import pygame, Debug
from Classes import win, playerAssets, playerInfo, screenAssets



pygame.init()
pygame.display.set_caption("Capybara Jump")

playerRootDir = "images/Colin/"
screenRootDir = "images/"

#class instances
bgAssets = screenAssets(screenRootDir)
playerMaths = playerInfo()
playerAnim = playerAssets(playerRootDir)
winSizing = win()

gameScreen = screenAssets(screenRootDir)
player = playerAssets(playerRootDir)

# Simple while loop to add controls
run = True
debugOn = False
debug_cooldown = 0  # Add a cooldown timer
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Update game state
    if keys[pygame.K_LEFT] and playerMaths.playerX > 0:
        playerMaths.playerX -= playerMaths.vel
        playerMaths.lastMove = "L"  # Update lastMove for left movement
        playerAnim.frameCount += 1
        if playerAnim.frameCount >= len(playerAnim.leftSprites) * playerAnim.frameDelay:
            playerAnim.frameCount = 0  # Reset frame count for left movement

    if keys[pygame.K_RIGHT]:
        playerMaths.playerX += playerMaths.vel
        playerMaths.lastMove = "R"  # Update lastMove for right movement
        playerAnim.frameCount += 1
        if playerAnim.frameCount >= len(playerAnim.rightSprites) * playerAnim.frameDelay:
            playerAnim.frameCount = 0  # Reset frame count for right movement



    # Handle jumping
    if keys[pygame.K_SPACE]:
        if not playerMaths.isJump:
            playerMaths.isJump = True
            playerMaths.jumpCount = 10  # Adjust as needed

    # Apply gravity
    if not playerMaths.isJump:
        if playerMaths.playerY < 313:  # Adjust the ground level as needed
            playerMaths.playerY += 1  # Adjust the gravity value as needed

    if playerMaths.isJump == True:
        playerMaths.jumping()




    # Clear the screen
    winSizing.windowSize.fill((0, 0, 0))

    # Draw the (resized) background
    winSizing.windowSize.blit(bgAssets.resizedBgImg, (0, 0))

    #jumping
    if playerMaths.isJump:
        playerAnim.frameCount = 0  # Reset frame count when jumping
        if playerMaths.lastMove == "L":  # Check the last move direction
            # Draw the jumping sprite facing left
            winSizing.windowSize.blit(pygame.transform.flip(playerAnim.standingSprites, True, False), (playerMaths.playerX, playerMaths.playerY))
        else:
            # Draw the jumping sprite facing right
            winSizing.windowSize.blit(playerAnim.standingSprites, (playerMaths.playerX, playerMaths.playerY))

    if keys[pygame.K_LEFT]:
        playerAnim.leftFrameCount += 1
        playerMaths.lastMove = "L"
        if playerAnim.leftFrameCount >= len(playerAnim.leftSprites) * playerAnim.frameDelay:
            playerAnim.leftFrameCount = 0
        winSizing.windowSize.blit(playerAnim.leftSprites[playerAnim.leftFrameCount // playerAnim.frameDelay], (playerMaths.playerX, playerMaths.playerY))
        
    elif keys[pygame.K_RIGHT]:
        playerAnim.rightFrameCount += 1
        playerMaths.lastMove = "R"
        if playerAnim.rightFrameCount >= len(playerAnim.rightSprites) * playerAnim.frameDelay:
            playerAnim.rightFrameCount = 0
        winSizing.windowSize.blit(playerAnim.rightSprites[playerAnim.rightFrameCount // playerAnim.frameDelay], (playerMaths.playerX, playerMaths.playerY))
    else:
        playerAnim.frameCount = 0  # Reset frame count when standing still
        if playerMaths.lastMove == "L":
            # Draw the standing sprite facing left
            winSizing.windowSize.blit(pygame.transform.flip(playerAnim.standingSprites, True, False), (playerMaths.playerX, playerMaths.playerY))
        else:
            # Draw the standing sprite facing right
            winSizing.windowSize.blit(playerAnim.standingSprites, (playerMaths.playerX, playerMaths.playerY))

    # Draw the debug information if debug mode is enabled
    if debugOn:
        Debug.debugMode()

    # Update the display once per frame
    pygame.display.update()

pygame.quit()
