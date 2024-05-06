import pyglet

animation = pyglet.image.load_animation('images/explosion.gif')

sprite = pyglet.sprite.Sprite(animation)

sprite.x = 100
sprite.y = 100

new_window = pyglet.window.Window(width=1400, height=800, caption="Game", resizable=False )

#@new_window.event
def on_draw():
    new_window.clear()
    sprite.draw()

pyglet.clock.schedule_interval(on_draw, 4)

pyglet.app.run()