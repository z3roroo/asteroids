import pygame # pyright: ignore[reportMissingImports]
from constants import LINE_WIDTH
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    
    def __init__(self, x, y, direction):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        self.velocity = direction * 500

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt