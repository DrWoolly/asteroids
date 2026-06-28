import sys
import pygame
from asteroid import Asteroid
from asteroid_field import AsteroidField
from player import Player
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialise game objects
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create update and draw containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)


    while True:
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("GAME OVER!")
                sys.exit()
        
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
