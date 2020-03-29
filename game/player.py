import math
from pyglet.window import key
from .physics import PhysicalObject
from .resources import player_image


class Player(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(img=player_image, *args, **kwargs)
        self.thrust = 300
        self.rotate_speed = 200
        self.keys = {key.LEFT: False, key.RIGHT: False, key.UP: False}

    def on_key_press(self, symbol, modifiers):
        for k in [key.UP, key.LEFT, key.RIGHT]:
            if symbol == k:
                self.keys[k] = True
                break

    def on_key_release(self, symbol, modifiers):
        for k in [key.UP, key.LEFT, key.RIGHT]:
            if symbol == k:
                self.keys[k] = False
                break

    def update(self, dt):
        super().update(dt)

        if self.keys[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.keys[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.keys[key.UP]:
            # convert to radians the rotation in degrees
            angle_radians = -math.radians(self.rotation)
            # get the x and y components
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            # update the velocity
            self.velocity_x += force_x
            self.velocity_y += force_y

