import pyglet
import math
from pyglet.window import key
from .physics import PhysicalObject
from .resources import player_image, WIDTH, engine_image
from .bullet import Bullet


class Player(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(img=player_image, *args, **kwargs)
        self.thrust = 300
        self.rotate_speed = 200
        self.top_speed = WIDTH
        # Bullets
        self.reacts_to_bullets = False
        self.bullet_speed = 700
        # Key press handler
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        # Engine
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

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    def fire(self):
        if self.dead:
            return
        angle_radius = -math.radians(self.rotation)
        cos_angle, sin_angle = math.cos(angle_radius), math.sin(angle_radius)
        ship_radius = self.image.width / 2
        bullet_x = self.x + cos_angle * ship_radius
        bullet_y = self.y + sin_angle * ship_radius
        new_bullet = Bullet(bullet_x, bullet_y, batch=self.batch)
        new_bullet.velocity_x = self.velocity_x + cos_angle * self.bullet_speed
        new_bullet.velocity_y = self.velocity_y + sin_angle * self.bullet_speed
        self.new_objects.append(new_bullet)
