import pygame.draw
import random

from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

        self.radius = radius
        self.velocity = pygame.Vector2(20,20)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20.0, 50.0)
            asteroid_1_rotation = self.velocity.rotate(angle)
            asteroid_2_rotation = self.velocity.rotate(-angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

            asteroid_1.velocity = asteroid_1_rotation * 1.2
            asteroid_2.velocity = asteroid_2_rotation * 1.2



