# main.py
import pygame
import sys
from Screen import Screen
from Character import Character

pygame.init()

screen_manager = Screen()
screen_manager.load_theme('theme.json')
screen = screen_manager.set_screen()
screen_manager.draw_ground(screen)

character = Character()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.left = True
            elif event.key == pygame.K_RIGHT:
                character.right = True
            elif event.key == pygame.K_SPACE:
                character.jump = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character.left = False
            elif event.key == pygame.K_RIGHT:
                character.right = False
            elif event.key == pygame.K_SPACE:
                character.jump = False

    screen.fill((255, 255, 255))

    character.y_speed += character.gravity
    character.player.y += character.y_speed
    character.update()
    screen_manager.draw_character(screen, character)
    screen_manager.draw_ground(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()


pygame.quit()
sys.exit()
