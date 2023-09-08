import pygame
import PublicVariables
from PublicVariables import publicVariables

def debugMode():
    # Update the mouse coordinates
    mouseX, mouseY = pygame.mouse.get_pos()
    # Display the mouse coordinates as text with Y inverted
    text = PublicVariables.font.render(f"Mouse: ({mouseX}, {PublicVariables.screenHeight - mouseY})", True, (255, 255, 255))
    PublicVariables.win.blit(text, (10, 10))  # Adjust the position as needed