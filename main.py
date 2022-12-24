import pyglet 
from pyglet.window import key 
from player import Player
from platform_1 import Platform


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAT_WIDTH = 30

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Pyglet Experiment", resizable=False ,fullscreen=False)
pyglet.gl.glClearColor(*(255,255,255,255))


'''Position - X, Position - Y, ObjectWidth, ObjectHeight, Color'''
player = Player(window, window.width//2 - 50, window.height // 8 - 10)


platforms = [
    Platform(0,0, WINDOW_WIDTH, PLAT_WIDTH),
    Platform(0,0, PLAT_WIDTH, WINDOW_WIDTH),
    Platform(0, WINDOW_HEIGHT-PLAT_WIDTH, WINDOW_WIDTH, PLAT_WIDTH),
    Platform(WINDOW_WIDTH-PLAT_WIDTH,0, PLAT_WIDTH, WINDOW_HEIGHT)
]




@window.event
def on_draw():
    window.clear()
    player.draw()
    for p in platforms:
        p.draw()

@window.event
def on_key_press(symbol, modifiers):
    global player 
    if symbol == key.LEFT:
        player.go_left = True
        
    if symbol == key.RIGHT:
        player.go_right = True

    if symbol == key.UP:
        player.go_up = True
        
    if symbol == key.DOWN:
        player.go_down = True


@window.event 
def on_key_release(symbol, modifiers):
    global player
    if symbol == key.LEFT:
        player.go_left = False
    if symbol == key.RIGHT:
        player.go_right = False
    if symbol == key.UP:
        player.go_up = False    
    if symbol == key.DOWN:
        player.go_down = False

def update(dt):
    global player
    player.update(dt)
    player.move()



if __name__=="__main__":
    pyglet.clock.schedule_interval(update, 1.0/120)
    pyglet.app.run()