import random
import pyglet

from .resources import WIDTH, HEIGHT, player_image
from .asteroid import Asteroid
from .util import distance


def asteroids(num_asteroids, player_position, batch=None):
    populate_asteroids = []
    for i in range(num_asteroids):
        x, y = player_position
        while distance((x, y), player_position) < 100:
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
        new_asteroid = Asteroid(x=x, y=y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40
        populate_asteroids.append(new_asteroid)
    return populate_asteroids


def player_lives(num_icons, batch=None):
    lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=player_image, x=WIDTH - 15 - i * 30, y=HEIGHT - 15, batch=batch)
        new_sprite.scale = 0.5
        new_sprite.rotation = 270
        lives.append(new_sprite)
    return lives

