class TurtlePen():
    
    def __init__(self, turtle):
        self.t = turtle
    
    def pen_down(self):
        self.t.down()
        
    def pen_up(self):
        self.t.up()