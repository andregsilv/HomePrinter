class LowLevelPrinter:
    pass
    
class PrinterCanvas:
    def __init__(self, turtle):
        self.t = turtle
        self.screen = self.t.getscreen()
        self.set_offset(0,0)
        
    def set_offset(self, x, y):
        self.offset_x = x
        self.offset_y = y
    
    def init(self):
        self.penup()
        self.t.setpos(0,0)
        
        newx = (self.screen.window_width() - 2 * self.offset_x) / 2 - self.offset_x
        newy = (self.screen.window_height() - 2 * self.offset_y) / 2 - self.offset_y
        self.move(-newx, -newy)
    
    def move(self, x, y):
        newx = self.t.xcor() + x
        newy = self.t.ycor() + y
        self.t.setpos(newx, newy)
    
    def pendown(self):
        self.t.down()
        
    def penup(self):
        self.t.up()

WIDTH = 600
HEIGHT = 600

if __name__ == "__main__":
    import turtle
    turtle.setup(height=HEIGHT, width=WIDTH)
    turtle.title("Printer Canvas")
    
    t = turtle.Turtle()
    t.left(120) # shows cursor like an inclinated pen
    t.speed(1)
    
    pc = PrinterCanvas(t)
    pc.set_offset(10,10)
    pc.init()



    turtle.done()