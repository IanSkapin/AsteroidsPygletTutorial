import pyglet
from .resources import HEIGHT, WIDTH
from .util import distance


class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = self.velocity_y = 0.0
        self.dead = False
        self.new_objects = []
        # bullets
        self.reacts_to_bullets = True
        self.is_bullet = False
        self.event_handlers = []

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
        """Check if the object is off the screen and wrap it around the other side"""
        self.check_bound('_x', -self.image.width / 2, WIDTH + self.image.width / 2)
        self.check_bound('_y', -self.image.height / 2, HEIGHT + self.image.height / 2)

    def collides_with(self, other):
        if not self.reacts_to_bullets and other.is_bullet or \
                self.is_bullet and not other.reacts_to_bullets:
            return False
        collision_distance = (self.scale * self.image.width) / 2 + \
                             (other.scale * other.image.width) / 2
        actual_distance = distance(self.position, other.position)
        return actual_distance <= collision_distance

    def handle_collision_with(self, other):
        if self.__class__ != other.__class__:
            self.dead = True

    def get_new_objects(self):
        """Get the new objects and clear the list"""
        output = self.new_objects[:]
        self.new_objects = []
        return output
