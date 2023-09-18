import pygame
import os

pygame.init()

class win: #Window Sizing
    def __init__(self):
        # Screen Dimensions
        self.windowSize = pygame.display.set_mode((1280, 768))  # Create the display window
        self.screenWidth = 1280
        self.screenHeight = 768

class screenAssets: #Bg images (TBA: parallax bg)
    def __init__(self, rootdir):
        self.rootDir = rootdir
        # Resize bg
        self.loadBg(self.rootDir)
        self.newBgWidth = 1280  # Adjust this to desired width
        self.newBgHeight = 768  # Adjust this to desired height
        self.resizedBgImg = pygame.transform.scale(self.bg, (self.newBgWidth, self.newBgHeight))


    def loadBg(self, rootdir): #directory for game bg
        self.bg = pygame.image.load(f"{rootdir}bg.png")

class playerAssets: #sprite animation, resizing
    def __init__(self, rootdir):
        self.rootDir = rootdir
        # Load and scale the player's images

        self.leftSprites = [pygame.image.load(os.path.join("./images/Colin/Lmove/", f'Lmove ({i}).gif')) for i in range(1, 9)]
        self.rightSprites = [pygame.image.load(os.path.join("./images/Colin/Rmove/", f'Rmove ({i}).gif')) for i in range(1, 9)]
        self.standingSprites = pygame.image.load(f"images/Colin/standing.gif")
        self.idleSprites = [pygame.image.load(os.path.join("./images/Colin/idle/", f'idle ({i}).gif')) for i in range(1, 16)]
        self.originalWidth = 25  # Desired width for the sprite
        self.originalHeight = 25 # Desired height for the sprite
        self.width = self.originalWidth
        self.height = self.originalHeight
        self.currentFrame = self.leftSprites[0]  # Initialize current frame
        self.scaleFactor = 2  # Adjust the scale factor as needed
        self.width = self.originalWidth * self.scaleFactor
        self.height = self.originalHeight * self.scaleFactor

        for i in range(8):
            self.leftSprites[i] = pygame.transform.scale(self.leftSprites[i], (self.width, self.height))
            self.rightSprites[i] = pygame.transform.scale(self.rightSprites[i], (self.width, self.height))
        for i in range(15):
            self.idleSprites[i] = pygame.transform.scale(self.idleSprites[i], (self.width, self.height))
        self.standingSprites = pygame.transform.scale(self.standingSprites, (self.width, self.height))

        self.leftFrameCount = 0
        self.rightFrameCount = 0

        
        # Define variables for sprite animation
        self.frameCount = 0  # To keep track of the current frame
        self.frameDelay = 10  # Delay between frame changes (adjust as needed)
        self.playerCanIdle = True
        self.leftFrameCount = 0
        self.rightFrameCount = 0

    def flip_standing_sprite(self, direction): #flip standing sprite if in wrong pos
        if playerInfo.lastMove == "L":
            self.standingSprite = pygame.transform.flip(self.standingSprite, True, False)



playerMove = playerAssets("images/Colin/")
class playerInfo: #player maths
    def __init__(self):

        self.vel = 3    
        self.lastMove = "R"
        self.isJump = False
        self.jumpCount = 10
        self.falling = False
        self.playerX = 410
        self.playerY = 435
        self.initialY = 50 #playerAssets.playerY
        self.jumpHeight = 0.1

    def draw(self):
            if playerMove.frameCount + 1 >= 27:
                playerMove.frameCount = 0

            if not(self.standing):
                if self.left:
                    window.windowSize.blit(playerMove.leftSprites[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    window.windowSize.blit(playerMove.rightSprites[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
            else:
                if self.right:
                    window.windowSize.blit(playerMove.rightSprites[0], (self.x, self.y))
                else:
                    window.windowSize.blit(playerMove.leftSprites[0], (self.x, self.y))
            self.hitbox = (self.x + 17, self.y + 11, 29, 52) # NEW
            pygame.draw.rect(win, (255,0,0), self.hitbox,2) # To draw the hit box around the player

    def jumping(self):
        if self.isJump:
            playerAssets.playerCanIdle = False
            if self.jumpCount >= -10:
                if self.jumpCount < 0 and not self.falling:
                    self.playerY += (self.jumpCount * abs(self.jumpCount)) * self.jumpHeight * 3  # Adjust the jump speed here
                    self.falling = True
                else:
                    self.playerY -= (self.jumpCount * abs(self.jumpCount)) * self.jumpHeight * 3
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False
                self.falling = False


class fonts: #all fonts used
    def __init__(self):
        # Load a font for rendering text, and access from "fonts" folder
        self.mainFont = pygame.font.Font(os.path.join("fonts", 'SpaceMono-Regular.ttf'), 16)


window = win()
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self):
        pygame.draw.circle(window.windowSize, self.color, (self.x,self.y), self.radius)


class enemy(object):
    walkLeft = [pygame.image.load(os.path.join("./images/Enemy/Lmove/", f'Lmove ({i}).png')) for i in range(1, 12)]
    walkRight = [pygame.image.load(os.path.join("./images/Enemy/Rmove/", f'Rmove ({i}).png')) for i in range(1, 12)]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) # NEW

    def draw(self):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            window.windowSize.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.windowSize.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) # NEW
        pygame.draw.rect(window.windowSize, (255,0,0), self.hitbox,2) # Draws the hit box around the enemy

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    # NEW METHOD
    def hit(self):  # This will display when the enemy is hit
        print('hit')


        

