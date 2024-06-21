import pygame
import sys
import ctypes
import json

class Screen():
    def __init__(self, width, height):
        self.user32 = ctypes.windll.user32
        self.screen_width = self.user32.GetSystemMetrics(0)
        self.screen_height = self.user32.GetSystemMetrics(1)

    def load_theme(self, filename):
        try:
            with open(filename, 'r') as f:
                theme = json.load(f)
                if 'background' in theme:
                    color = theme['background']
                    self.background_color = (color['red'], color['green'], color['blue'])
                else:
                    raise KeyError("Warning: 'background' not found in theme.json")
        except FileNotFoundError:
            print(f"Error: {filename} not found. Using default color.")

    def set_screen(self):
        flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
        screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags)
        pygame.display.set_caption("XYZ")
        return screen

    def set_background_color(self, screen):
        screen.fill(self.background_color)
        pygame.display.flip()


# Initialize Pygame
pygame.init()

screen_manager = Screen()
screen_manager.load_theme('theme.json')
screen = screen_manager.set_screen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_manager.set_background_color(screen)

# Quit Pygame
pygame.quit()
sys.exit()
