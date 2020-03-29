import pyglet

from game import resources
from game import load
from game.physics import PhysicalObject
from game.player import Player

game_window = pyglet.window.Window(resources.WIDTH, resources.HEIGHT)
main_batch = pyglet.graphics.Batch()

# UI
score_label = pyglet.text.Label(text="Score: 0", x=10, y=resources.HEIGHT - 25, batch=main_batch)
level_label = pyglet.text.Label(text="Version 1: Static Graphics", batch=main_batch,
                                x=resources.WIDTH / 2,
                                y=resources.HEIGHT - 25, anchor_x='center')
player_lives = load.player_lives(3, batch=main_batch)

# game's physical objects
player_ship = Player(x=resources.WIDTH / 2, y=resources.HEIGHT / 2, batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, batch=main_batch)
game_objects = [player_ship] + asteroids

# Player is an event handler so we need to push it onto the event stack
game_window.push_handlers(player_ship)

#@game_window.event
#def on_mouse_press():

#@game_window.event
#def on_key_press():

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    for o in game_objects:
        o.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
