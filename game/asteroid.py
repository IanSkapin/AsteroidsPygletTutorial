import pyglet
import random

from .resources import asteroid_image
from .physics import PhysicalObject


class Asteroid(PhysicalObject):
    def __init__(self, *args, **kwargs):
        self.collision_speedup = kwargs.pop('collision_speedup', 100)
        super().__init__(asteroid_image, *args, **kwargs)
        self.rotate_speed = random.random() * 100 - 50

    def handle_collision_with(self, other):
        super().handle_collision_with(other)
        if self.dead and self.scale > 0.25:
            for i in range(random.randint(2, 3)):
                new_asteroid = Asteroid(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.velocity_x = (random.random() - 0.5) * self.collision_speedup + self.velocity_x
                new_asteroid.velocity_y = (random.random() - 0.5) * self.collision_speedup + self.velocity_y
                new_asteroid.scale = self.scale / 2
                self.new_objects.append(new_asteroid)

    def update(self, dt):
        super().update(dt)
        self.rotation += self.rotate_speed * dt

