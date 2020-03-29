import random
import pyglet
import math

from .resources import WIDTH, HEIGHT, asteroid_image, player_image
from .physics import PhysicalObject


def asteroids(num_asteroids, player_position, batch=None):
    populate_asteroids = []
    for i in range(num_asteroids):
        x, y = player_position
        while distance((x, y), player_position) < 100:
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
        new_asteroid = PhysicalObject(img=asteroid_image, x=x, y=y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40
        populate_asteroids.append(new_asteroid)
    return populate_asteroids


def distance(a=(0, 0), b=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((a[0] - b[0]) ** 2 +
                     (a[1] - b[1]) ** 2)


def player_lives(num_icons, batch=None):
    lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=player_image, x=WIDTH - 15 - i * 30, y=HEIGHT - 15, batch=batch)
        new_sprite.scale = 0.5
        new_sprite.rotation = 270
        lives.append(new_sprite)
    return lives

