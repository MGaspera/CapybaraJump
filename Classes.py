import pygame
import os

pygame.init()

class win:
    def __init__(self):
        # Screen Dimensions
        self.windowSize = pygame.display.set_mode((1280, 768))  # Create the display window
        self.screenWidth = 1280
        self.screenHeight = 768

class assets:
    def __init__(self):
        # Define the image directory
        self.imageDirectory = "images"  # The folder containing the images
        # Load background and sprite images
        self.bg = pygame.image.load(os.path.join(self.imageDirectory, 'bg.png'))
        self.standingSprite = pygame.image.load(os.path.join(self.imageDirectory, 'Standing.gif'))
        self.leftSprites = [pygame.image.load(os.path.join(self.imageDirectory, f'Lmove ({i}).gif')) for i in range(1, 8)]
        self.rightSprites = [pygame.image.load(os.path.join(self.imageDirectory, f'Rmove ({i}).gif')) for i in range(1, 8)]
        # Resize bg
        self.newBgWidth = 1280  # Adjust this to desired width
        self.newBgHeight = 768  # Adjust this to desired height
        self.resizedBgImg = pygame.transform.scale(self.bg, (self.newBgWidth, self.newBgHeight))
        self.currentFrame = self.leftSprites[0]  # Initialize current frame
        self.leftFrameCount = 0
        self.rightFrameCount = 0

        # Define variables for sprite animation
        self.frameCount = 0  # To keep track of the current frame
        self.frameDelay = 10  # Delay between frame changes (adjust as needed)

    def flip_standing_sprite(self, direction): #flip standing sprite if in wrong pos
        if direction == "L":
            self.standingSprite = pygame.transform.flip(self.standingSprite, True, False)

class player:
    def __init__(self):
        self.x = 69
        self.y = 313
        self.original_width = 100  # Desired width for the sprite
        self.original_height = 100  # Desired height for the sprite
        self.width = self.original_width
        self.height = self.original_height
        self.vel = 3
        self.lastMove = "R"
        self.isJump = False
        self.jumpCount = 10
        self.falling = False
        self.initialY = self.y
        self.jumpSpeed = 0.1
        self.canIdle = True

        # Initialize frame counts for left and right animations
        self.leftFrameCount = 0
        self.rightFrameCount = 0

        # Load and scale the player's images
        self.leftSprites = [pygame.image.load(os.path.join("images/Colin/Lmove/", f'Lmove ({i}).gif')) for i in range(1, 9)]
        self.rightSprites = [pygame.image.load(os.path.join("images/Colin/Rmove/", f'Rmove ({i}).gif')) for i in range(1, 9)]
        self.standingSprites = pygame.image.load(os.path.join("images/Colin/", f'standing.gif'))
        self.idleSprites = [pygame.image.load(os.path.join("images/Colin/idle/", f'idle ({i}).gif')) for i in range(1, 16)]

        for i in range(8):
            self.leftSprites[i] = pygame.transform.scale(self.leftSprites[i], (self.width, self.height))
            self.rightSprites[i] = pygame.transform.scale(self.rightSprites[i], (self.width, self.height))
        for i in range(15):
            self.idleSprites[i] = pygame.transform.scale(self.idleSprites[i], (self.width, self.height))
        self.standingSprites = pygame.transform.scale(self.standingSprites, (self.width, self.height))


class fonts:
    def __init__(self):
        # Load a font for rendering text, and access from "fonts" folder
        self.mainFont = pygame.font.Font(os.path.join("fonts", 'SpaceMono-Regular.ttf'), 16)
