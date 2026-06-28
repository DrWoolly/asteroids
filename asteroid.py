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
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20.0, 50.0)
            rotation = self.velocity.rotate(self.rotation)
