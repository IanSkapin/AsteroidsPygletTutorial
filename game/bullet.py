import pyglet
from .physics import PhysicalObject
from .resources import bullet_image


class Bullet(PhysicalObject):
    """Bullets fired by the player"""
    def __init__(self, *args, **kwargs):
        super().__init__(bullet_image, *args, **kwargs)
        pyglet.clock.schedule_once(self.die, .8)
        self.is_bullet = True

    def die(self, dt):
        self.dead = True
