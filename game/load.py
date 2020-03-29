import random
import pyglet
import math
from .resources import WIDTH, HEIGHT, asteroid_image


def asteroids(num_asteroids, player_position):
    populate_asteroids = []
    for i in range(num_asteroids):
        x, y = player_position
        while distance((x, y), player_position) < 100:
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
        new_asteroid = pyglet.sprite.Sprite(img=asteroid_image, x=x, y=y)
        new_asteroid.rotation = random.randint(0, 360)
        populate_asteroids.append(new_asteroid)
    return populate_asteroids


def distance(a=(0, 0), b=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt(
        (a[0] - b[0]) ** 2 +
        (a[1] - b[1]) ** 2
    )
