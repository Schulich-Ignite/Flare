import sys
import os
import pygame

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        # Replace this line
    if keys_pressed[pygame.K_LEFT]:
        # Replace this line
    if keys_pressed[pygame.K_RIGHT]:
        # Replace this line
    if keys_pressed[pygame.K_DOWN]:
        # Replace this line


    # Mouse events
    mouse_buttons = pygame.mouse.get_pressed()
    # Runs while you hold it
    if mouse_buttons[0]:  # If left mouse pressed
        mouse_pos = pygame.mouse.get_pos()  # Get position of mouse
        # Returns (x, y) coordinates as tuple

    if mouse_buttons[2]:  # If right mouse pressed


    """
    UPDATE section - manipulate everything on the screen
    """
    


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour


    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    