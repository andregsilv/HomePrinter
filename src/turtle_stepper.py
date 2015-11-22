class TurtleStepper():
    
    def __init__(self, turtle, is_axis_x):
        self.t = turtle
        self.is_axis_x = is_axis_x
        
    def __move__(self, steps, reverse=False):
        signaled_steps = steps * (-1 if reverse else 1)
        
        x, y = self.t.pos()
        
        if self.is_axis_x:
            newpos = (x + signaled_steps, y)
        else: 
            newpos = (x, y + signaled_steps)
        
        self.t.setpos(newpos)
        
        
    def step(self, reverse=False):
        self.__move__(1, reverse)
        
    def half(self, reverse=False):
        self.__move__(0.5, reverse)
        