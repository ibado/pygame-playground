import pygame
import os

WIDTH, HEIGHT = 900, 500
BACKGROUND_COLOR = (225, 245, 205)
FPS = 60
STEP = 6

SPACESHIP_WIDTH = 47
SPACESHIP_HEIGHT = 34

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My own game")

SPACESHIP_IMAGE1 = pygame.transform.scale(
    pygame.image.load("spaceship.png"), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
)

SPACESHIP_IMAGE2 = pygame.transform.rotate(SPACESHIP_IMAGE1, 180.0)

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def draw_content(spaceship1, spaceship2):
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(SPACESHIP_IMAGE1, (spaceship1.x, spaceship1.y))
    WIN.blit(SPACESHIP_IMAGE2, (spaceship2.x, spaceship2.y))
    pygame.display.update()

def handle_key_events(keys, spaceship_position):
    if keys[pygame.K_UP] and spaceship_position.y - STEP >= 0:
        spaceship_position.y -= STEP
    elif keys[pygame.K_DOWN] and spaceship_position.y + SPACESHIP_HEIGHT + STEP <= HEIGHT:
        spaceship_position.y += STEP



def main():
    sp1_x = WIDTH / 3 - SPACESHIP_WIDTH / 2
    sp2_x = WIDTH * 2 / 3 - SPACESHIP_WIDTH / 2
    sp_y = HEIGHT / 2 - SPACESHIP_HEIGHT / 2

    spaceship1 = Position(sp1_x, sp_y)
    spaceship2 = Position(sp2_x, sp_y)

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        keys_pressed = pygame.key.get_pressed()
        handle_key_events(keys_pressed, spaceship1)
 
        draw_content(spaceship1, spaceship2)


if __name__ == "__main__":
    main()
