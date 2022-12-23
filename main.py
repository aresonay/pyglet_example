import pyglet 
from pyglet.window import key 


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Pyglet Experiment", resizable=False ,fullscreen=False)
pyglet.gl.glClearColor(*(255,255,255,255))


'''Position - X, Position - Y, ObjectWidth, ObjectHeight, Color'''
rect01 = pyglet.shapes.Rectangle(window.width//2 - 50, window.height // 8 - 10, 20, 20, color=(0,0,0))


@window.event
def on_draw():
    window.clear()
    rect01.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        rect01.x -= 5
    if symbol == key.D:
        rect01.x += 5

@window.event 
def on_key_release(symbol, modifiers):
    if symbol == key.A:
        pass
    if symbol == key.D:
        pass 



if __name__=="__main__":
    pyglet.app.run()