import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([600, 800])
print(screen)
screen.fill((200, 200, 20))

pygame.draw.circle(surface=screen, color=[255, 50, 230], center=(100, 100), radius=80, width=0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # pygame.quit()
            sys.exit()
    pygame.display.flip()
