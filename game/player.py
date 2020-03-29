import pyglet
import math
from pyglet.window import key
from .physics import PhysicalObject
from .resources import player_image, WIDTH, engine_image


class Player(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(img=player_image, *args, **kwargs)
        self.thrust = 300
        self.rotate_speed = 200
        self.top_speed = WIDTH
        self.key_handler = key.KeyStateHandler()

        self.engine_sprite = pyglet.sprite.Sprite(img=engine_image, *args, **kwargs)
        self.engine_sprite.visible = False

    def can_accelerate(self, velocity, force):
        return self.top_speed > velocity + force

    def update(self, dt):
        super().update(dt)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP]:
            # convert to radians the rotation in degrees
            angle_radians = -math.radians(self.rotation)
            # get the x and y components
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            # update the velocity
            if self.can_accelerate(self.velocity_x, force_x):
                self.velocity_x += force_x
            if self.can_accelerate(self.velocity_y, force_y):
                self.velocity_y += force_y
            # update the engine position
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
        # show the engine while UP is held
        self.engine_sprite.visible = self.key_handler[key.UP]

    def delete(self):
        self.engine_sprite.delete()
        super().delete()

