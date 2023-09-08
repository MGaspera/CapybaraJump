import pygame
import os

# Create the display window
win = pygame.display.set_mode((1280, 768))


def publicVariables():
    #Screen Dimensions
    
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

    # Load a font for rendering text, and access from "fonts" folder
    font = pygame.font.Font(os.path.join("fonts", 'SpaceMono-Regular.ttf'), 16)

        