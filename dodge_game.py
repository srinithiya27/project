import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Enemies")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Enemy
enemy_width = 50
enemy_height = 50
enemy_speed = 5
enemy_list = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Function to spawn enemies
def spawn_enemy():
    x_pos = random.randint(0, WIDTH - enemy_width)
    y_pos = -enemy_height
    enemy_list.append([x_pos, y_pos])

# Game loop
running = True
spawn_timer = 0

while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Spawn enemies every 30 frames
    spawn_timer += 1
    if spawn_timer >= 30:
        spawn_enemy()
        spawn_timer = 0

    # Move enemies
    for enemy in enemy_list[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemy_list.remove(enemy)
            score += 1  # Score for dodging

    # Collision detection
    for enemy in enemy_list:
        if (player_y < enemy[1] + enemy_height and
            player_y + player_height > enemy[1] and
            player_x < enemy[0] + enemy_width and
            player_x + player_width > enemy[0]):
            running = False  # Game over

    # Draw player and enemies
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
print(f"Game Over! Final Score: {score}")
