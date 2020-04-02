import pyglet

from game import resources
from game import load
from game.player import Player
from game.asteroid import Asteroid

game_window = pyglet.window.Window(resources.WIDTH, resources.HEIGHT)
main_batch = pyglet.graphics.Batch()

# UI
score = 0
score_label = pyglet.text.Label(text="Score: 0", x=10, y=resources.HEIGHT - 25, batch=main_batch)
level_label = pyglet.text.Label(text="Version 1: Static Graphics", batch=main_batch,
                                x=resources.WIDTH / 2,
                                y=resources.HEIGHT - 25, anchor_x='center')
player_lives = []
level_reached = 0
# Set up the game over label offscreen
game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=400, y=-300, anchor_x='center',
                                    batch=main_batch, font_size=48)

# game's physical objects
player_ship = None
num_asteroids = 3
game_objects = []

# We need to pop off as many event stack frames as we pushed on
# every time we reset the level.
event_stack_size = 0


def init(dt=None):
    global score, num_asteroids, game_over_label
    game_over_label.y = -300
    score = 0
    score_label.text = f"Score: {score}"
    num_asteroids = 3
    reset_level()


def reset_level(num_lives=3):
    global player_ship, player_lives, game_objects, event_stack_size, level_reached

    # Clear the event stack of any remaining handlers from other levels
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1

    for life in player_lives:
        life.delete()

    player_ship = Player(x=resources.WIDTH / 2, y=resources.HEIGHT / 2, batch=main_batch)

    player_lives = load.player_lives(num_lives, batch=main_batch)

    asteroids = load.asteroids(num_asteroids, player_ship.position, batch=main_batch, speed=40 + level_reached * 5)
    level_label.text = f'Level {level_reached + 1}'
    game_objects = [player_ship] + asteroids

    for o in game_objects:
        for handler in o.event_handlers:
            # Player is an event handler so we need to push it onto the event stack
            game_window.push_handlers(handler)
            event_stack_size += 1


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    global score, num_asteroids, level_reached
    player_dead = False

    asteroids_remaining = 0
    for o in game_objects:
        o.update(dt)
        if isinstance(o, Asteroid):
            asteroids_remaining += 1

    for i, obj1 in enumerate(game_objects):
        for j, obj2 in enumerate(game_objects[i+1:]):
            if not obj1.dead and not obj2.dead and obj1.collides_with(obj2):
                obj1.handle_collision_with(obj2)
                obj2.handle_collision_with(obj1)

    game_objects.extend([new for o in game_objects for new in o.get_new_objects()])
    for to_remove in [obj for obj in game_objects if obj.dead]:
        if to_remove == player_ship:
            player_dead = True
        to_remove.delete()
        game_objects.remove(to_remove)
        if isinstance(to_remove, Asteroid):
            score += 1
            score_label.text = f'Score: {score}'

    if player_dead:
        if len(player_lives) > 1:
            reset_level(len(player_lives) - 1)
        else:
            game_over_label.y = 300
            player_lives[0].delete()
            pyglet.clock.schedule_once(init, 15)
    elif asteroids_remaining == 0:
        num_asteroids += 1
        player_ship.delete()
        score += 10
        level_reached += 1
        reset_level(len(player_lives))


if __name__ == '__main__':
    init()

    pyglet.clock.schedule_interval(update, 1/120.0)

    pyglet.app.run()
