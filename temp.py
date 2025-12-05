import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Text Example")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont('arial', 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)

    text_surface = font.render("System for the thing test with GUI", True, BLUE)
    
    text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))

    screen.blit(text_surface, text_rect)

    pygame.display.update()

pygame.quit()
sys.exit()