import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Define colors and screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 3. Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Window")

# 4. Set up the game clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # 5. Handle events (user input, quitting the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add other event handlers here (e.g., key presses)

    # 6. Game logic updates (movement, collisions, etc.)
    # Your game logic code will go here

    # 7. Drawing (rendering the game objects)
    screen.fill(WHITE) # Fill the screen with a background color

    # Draw game objects (e.g., pygame.draw.rect, blitting images)
    # pygame.draw.rect(screen, BLACK, (100, 100, 50, 50)) # Example: draw a black square

    # 8. Update the display to show the new frame
    pygame.display.flip() # or pygame.display.update()

    # 9. Cap the frame rate at 60 FPS
    clock.tick(60)

# 10. Quit Pygame when the loop finishes
pygame.quit()
sys.exit()
