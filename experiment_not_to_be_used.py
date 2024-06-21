import pygame
import sys
import ctypes

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

pygame.init()

flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
screen = pygame.display.set_mode((screen_width, screen_height), flags)
pygame.display.set_caption("XYZ")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

character = pygame.Rect(50, 50, 50, 50)
velocity_y = 0
gravity = 1
jump_strength = -15
move_speed = 5

keys = {"left": False, "right": False, "jump": False}

CHUNK_WIDTH, CHUNK_HEIGHT = 1600, 1200

chunks = {}

def generate_chunk(x, y):
    chunk = []
    ground = pygame.Rect(x * CHUNK_WIDTH, y * CHUNK_HEIGHT + screen_height - 200, CHUNK_WIDTH, 200)
    chunk.append(ground)
    if (x, y) not in chunks:
        for i in range(3):
            barrier_x = x * CHUNK_WIDTH + 200 + i * 150
            barrier_y = y * CHUNK_HEIGHT + screen_height - 200 - i * 50
            barrier = pygame.Rect(barrier_x, barrier_y, 100, 50)
            chunk.append(barrier)
    chunks[(x, y)] = chunk

def get_chunk_coordinates(character):
    return character.x // CHUNK_WIDTH, character.y // CHUNK_HEIGHT

generate_chunk(0, 0)

def handle_collision(rect, barriers):
    for barrier in barriers:
        if rect.colliderect(barrier):
            if rect.bottom > barrier.top and rect.bottom <= barrier.top + velocity_y:
                rect.bottom = barrier.top
                return True
    return False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys["left"] = True
            elif event.key == pygame.K_RIGHT:
                keys["right"] = True
            elif event.key == pygame.K_SPACE:
                keys["jump"] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys["left"] = False
            elif event.key == pygame.K_RIGHT:
                keys["right"] = False
            elif event.key == pygame.K_SPACE:
                keys["jump"] = False

    if keys["left"]:
        character.x -= move_speed
    if keys["right"]:
        character.x += move_speed

    velocity_y += gravity
    character.y += velocity_y

    current_chunk = get_chunk_coordinates(character)

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            generate_chunk(current_chunk[0] + dx, current_chunk[1] + dy)

    for chunk_key in chunks.keys():
        if handle_collision(character, chunks[chunk_key]):
            velocity_y = 0
            if keys["jump"]:
                velocity_y = jump_strength

    camera_offset_x = screen_width // 2 - character.x - character.width // 2
    camera_offset_y = screen_height // 2 - character.y - character.height // 2

    screen.fill(WHITE)

    for chunk_key in chunks.keys():
        for barrier in chunks[chunk_key]:
            pygame.draw.rect(screen, BLACK, barrier.move(camera_offset_x, camera_offset_y))

    pygame.draw.rect(screen, BLACK, character.move(camera_offset_x, camera_offset_y))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

