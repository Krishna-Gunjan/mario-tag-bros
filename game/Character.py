# Character.py
import pygame
from Screen import Screen

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = pygame.Rect(100, Screen().screen_height - 200, 10, 10)
        self.x_speed = 5
        self.y_speed = 5

        self.jump_strength = -15
        self.gravity = 2

        self.left = False
        self.right = False
        self.jump = False

        self.y_velocity = 0

    def update(self):
        if self.left:
            self.player.x -= self.x_speed
        if self.right:
            self.player.x += self.x_speed
        if self.jump:
            self.y_velocity = self.jump_strength
            self.jump = False
        
        self.y_velocity += self.gravity
        self.player.y += self.y_velocity

    def handle_collisions(self, blocks):
        for block in blocks:
            if self.player.colliderect(block.rect):
                # Adjust the character's position based on the collision
                if self.y_velocity > 0:  # Falling down
                    self.player.bottom = block.rect.top
                    self.y_velocity = 0
                elif self.y_velocity < 0:  # Jumping up
                    self.player.top = block.rect.bottom
                    self.y_velocity = 0

                if self.player.right > block.rect.left and self.player.left < block.rect.right:
                    if self.left:  # Moving left
                        self.player.left = block.rect.right
                    if self.right:  # Moving right
                        self.player.right = block.rect.left
