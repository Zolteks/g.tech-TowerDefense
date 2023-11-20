
class Intellist:
    
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]
    
    def add(self, element):
        for i in range(self.size):
            if not self.array[i]:
                self.array[i] = element
                return
        print("list is full")
    
    def delete(self, element):
        for i in range(self.size):
            if self.array == element:
                self.array[i] = None
                return
        print("could not find the element")