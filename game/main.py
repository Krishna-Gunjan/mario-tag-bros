# main.py
import pygame
import sys
from Screen import Screen
from Character import Character
from Block import Barrier

pygame.init()

screen_manager = Screen()
screen_manager.load_theme('theme.json')
screen = screen_manager.set_screen()
ground = screen_manager.draw_ground(screen)

block1 = Barrier(100, 100, 100, 100)
blocks = [ground, block1]  # Add more blocks to this list as needed

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

    screen_manager.set_background_color(screen)

    for block in blocks:
        block.draw_barrier(screen)

    character.update()
    character.handle_collisions(blocks)

    screen_manager.draw_character(screen, character)

    screen_manager.draw_ground(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
