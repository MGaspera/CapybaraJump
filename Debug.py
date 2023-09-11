import pygame
from Classes import win, fonts

def debugMode():
    # Update the mouse coordinates
    mouseX, mouseY = pygame.mouse.get_pos()
    # Display the mouse coordinates as text with Y inverted
    text = fonts().mainFont.render(f"Mouse: ({mouseX}, {win().screenHeight - mouseY})", True, (255, 255, 255))
    win().windowSize.blit(text, (10, 10))  # Adjust the position as needed
    