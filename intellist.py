from bullet import Bullet

class Intellist:
    
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]
    
    def update(self, game=None):
        for i in range(self.size):
            if self.array[i]:
                if type(self.array[i]) == Bullet:
                    self.array[i].update(game)
                else:
                    self.array[i].update()
            
    def draw(self):
        for i in range(self.size):
            if self.array[i]: self.array[i].draw()
    
    def add(self, element):
        for i in range(self.size):
            if not self.array[i]:
                self.array[i] = element
                return
        print("list is full")
    
    def delete(self, element):
        for i in range(self.size):
            if self.array[i] and self.array[i].x == element.x and self.array[i].y == element.y:
                self.array[i] = None
                return
        print("could not find the element")