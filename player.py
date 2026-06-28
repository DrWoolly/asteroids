import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float, shot_cooldown: float = PLAYER_SHOT_COOLDOWN) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0
        self.radius = radius
        self.shot_cooldown = shot_cooldown

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt)-> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):

        if self.shot_cooldown <= 0:
            new_shot = Shot(self.position.x, self.position.y)
            new_shot.velocity = pygame.Vector2(0, 1)
            new_shot.velocity = new_shot.velocity.rotate(self.rotation)
            new_shot.position += new_shot.velocity
            new_shot.velocity * PLAYER_SHOT_SPEED
            self.shot_cooldown = PLAYER_SHOT_COOLDOWN



    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_k]:
            self.shoot()

        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt