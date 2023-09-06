import pygame
import os

pygame.init()

win = pygame.display.set_mode((1280, 768))
pygame.display.set_caption("Capybara Platformer")
screenWidth = 1280
screenHeight = 768

x = 69
y = 313
width = 50
height = 50
vel = 3


# Remembers the last horizontal direction travelled.
lastMove = "L"

# Variables that allow the player to jump
isJump = False
jumpCount = 10
falling = False
initialY = y  # Record the initial y-position before jumping

# Define jumpSpeed (smaller value = slower jump)
jumpSpeed = 0.1

# Load background and sprite images
imageDir = "images"  # The folder containing your images
bg = pygame.image.load(os.path.join(imageDir, 'bg.png'))
standingSprite = pygame.image.load(os.path.join(imageDir, 'Standing.gif'))
leftSprites = [pygame.image.load(os.path.join(imageDir, f'Lmove ({i}).gif')) for i in range(1, 8)]
rightSprites = [pygame.image.load(os.path.join(imageDir, f'Rmove ({i}).gif')) for i in range(1, 8)]

# Resize bg
newBgWidth = 1280  # Adjust this to your desired width
newBgHeight = 768  # Adjust this to your desired height
resizedBg = pygame.Surface((newBgWidth, newBgHeight))
resizedBg = pygame.transform.scale(bg, (newBgWidth, newBgHeight))

# Define variables for sprite animation
frameCount = 0  # To keep track of the current frame
frameDelay = 10  # Delay between frame changes (adjust as needed)

# Load a font for rendering text
font = pygame.font.Font(None, 36)  # Adjust the font and size as needed

# Simple while loop to add controls
run = True
while run:
    # Clear the screen only once at the beginning of each frame
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the mouse coordinates
    mouseX, mouseY = pygame.mouse.get_pos()

    # Specify controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        lastMove = "L"

    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += vel
        lastMove = "R"

    if keys[pygame.K_SPACE] and not isJump:  # Only allow jumping if not already jumping
        isJump = True
        initialY = y  # Record the initial y-position before jumping

    if isJump:
        if jumpCount >= -10:
            if jumpCount < 0 and not falling:
                y += (jumpCount * abs(jumpCount)) * jumpSpeed *2 # Adjust the jump speed here
                falling = True
            else:
                y -= (jumpCount * abs(jumpCount)) * jumpSpeed *2 # Adjust the jump speed here
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
            falling = False

    # Draw the (resized) background
    win.blit(resizedBg, (0, 0))

    # Draw the player sprite based on movement and direction
    if isJump:
        frameCount = 0  # Reset frame count when jumping
        win.blit(standingSprite, (x, y))
    elif keys[pygame.K_LEFT]:
        frameCount += 1
        if frameCount >= len(leftSprites) * frameDelay:
            frameCount = 0
        currentFrame = leftSprites[frameCount // frameDelay]
        win.blit(currentFrame, (x, y))
    elif keys[pygame.K_RIGHT]:
        frameCount += 1
        if frameCount >= len(rightSprites) * frameDelay:
            frameCount = 0
        currentFrame = rightSprites[frameCount // frameDelay]
        # Flip the sprite horizontally to face right
        currentFrame = pygame.transform.flip(currentFrame, True, False)
        win.blit(currentFrame, (x, y))
    else:
        frameCount = 0  # Reset frame count when standing still
        win.blit(standingSprite, (x, y))

    # Display the mouse coordinates as text (with Y inverted)
    text = font.render(f"Mouse: ({mouseX}, {screenHeight - mouseY})", True, (255, 255, 255))
    win.blit(text, (10, 10))  # Adjust the position as needed

    # Update the display
    pygame.display.update()

pygame.quit()
