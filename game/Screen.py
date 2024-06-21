# Screen.py
import ctypes
import json
import pygame

class Screen():
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.screen_width = self.user32.GetSystemMetrics(0)
        self.screen_height = self.user32.GetSystemMetrics(1)
        self.background_color = (255, 255, 255)  # Default background color

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
    
    def draw_ground(self, screen):
        ground = pygame.Rect(25, self.screen_height - 50, self.screen_width, 25)
        pygame.draw.rect(screen, (0, 255, 0), ground)
        pygame.display.flip()
        return ground

    def set_background_color(self, screen):
        screen.fill(self.background_color)
        pygame.display.flip()

    def draw_character(self, screen, character):
        pygame.draw.rect(screen, (255, 0, 0), character.player)

    def draw_block(self, screen, block):
        block.draw(screen)
