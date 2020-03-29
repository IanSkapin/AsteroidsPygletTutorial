import pyglet

from game import resources
from game import load

game_window = pyglet.window.Window(resources.WIDTH, resources.HEIGHT)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=resources.HEIGHT - 25)
level_label = pyglet.text.Label(text="Version 1: Static Graphics",
                                x=resources.WIDTH / 2,
                                y=resources.HEIGHT - 25, anchor_x='center')

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

asteroids = load.asteroids(3, player_ship.position)

#@game_window.event
#def on_mouse_press():

#@game_window.event
#def on_key_press():

@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()
    player_ship.draw()
    [rock.draw() for rock in asteroids]


if __name__ == '__main__':
    pyglet.app.run()