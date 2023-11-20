import pyxel

class Game:

    def __init__(self):

        pyxel.init(
            128,
            128,
            fps=30,
            quit_key=pyxel.KEY_TAB,
            capture_sec=30
        )

        pyxel.run(self.update, self.draw)
    
    def update(self):
        print("update")
    
    def draw(self):
        print("draw")