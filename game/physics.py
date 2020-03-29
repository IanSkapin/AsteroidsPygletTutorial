import pyglet
from .resources import HEIGHT, WIDTH


class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = self.velocity_y = 0.0

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.check_bounds()

    def check_bound(self, dimension_str: str, minimum: int, maximum: int):
        """In place update dimension x or y"""
        if self.__dict__[dimension_str] < minimum:
            self.__dict__[dimension_str] = maximum
        elif self.__dict__[dimension_str] > maximum:
            self.__dict__[dimension_str] = minimum

    def check_bounds(self):
        self.check_bound('_x', -self.image.width / 2, WIDTH + self.image.width / 2)
        self.check_bound('_y', -self.image.height / 2, HEIGHT + self.image.height / 2)

