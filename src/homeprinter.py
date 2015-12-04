from utils import *

class HomePrinter():
    def __init__(self, stepper_x, stepper_y, actuator_z):
        self.stx = stepper_x
        self.sty = stepper_y
        self.actz = actuator_z
        
        self.steps_per_milimiter_x = 1
        self.steps_per_milimiter_y = 1
        
        self.set_offset(0, 0)
        
        # TODO: enable fractions of a step
        #self.fractions_x = [1]
        #self.fractions_y = [1]
        
    def set_offset(self, offset_x, offset_y):
        self.current_x = offset_x
        self.current_y = offset_y
        
    def step_x(self, reverse=False):
        self.stx.step(reverse)
        self.current_x = self.current_x + (-1 if reverse else 1)

    def step_y(self, reverse=False):
        self.sty.step(reverse)
        self.current_y = self.current_y + (-1 if reverse else 1)

    def move(self, x, y): # Bresenham's line algorithm adaptation
        print("Deltas:", x, y)
    
        MAX_STEP_FRACTION = 1
        MAX_ERROR = 1 / MAX_STEP_FRACTION / 2.0
    
        revx = x < 0
        revy = y < 0
        
        
        if abs(x) < MAX_ERROR:
            for y in range(0, y, 1 if y > 0 else -1):
                self.step_y(revy)
            return
        
        error = 0
        deltaerr = abs(y / x)    # Assume deltax != 0 (line is not vertical),
        for i in range(0, x, 1 if x > 0 else -1):
            self.step_x(revx)
            
            error = error + deltaerr
            while error >= MAX_ERROR:
                self.step_y(revy)
                error = error - 1
                

    def draw_line(self, x1, y1, x2, y2):
        deltax = x2 - x1
        deltay = y2 - y1
        
        if (self.current_x != x1 or self.current_y != y1):
            self.actz.pen_up()
            self.move(x1 - self.current_x, y1 - self.current_y),
        self.actz.pen_down()
        self.move(deltax, deltay)
    
    def draw_rect(self, x1, y1, width, height):
        x2 = x1 + width
        y2 = y1 + height
        
        printer.draw_line(x1, y1, x2, y1)
        
        printer.draw_line(x2, y1, x2, y2)
        
        printer.draw_line(x2, y2, x1, y2)
        
        printer.draw_line(x1, y2, x1, y1)
        
if __name__ == "__main__":
    DEMO = True

    if DEMO:
        import turtle
        from turtle_stepper import *
        from turtle_pen import *
        
        turtle.setup(600, 600)
        turtle.title("Printer Canvas")

        t = turtle.Turtle()
        t.left(120) # shows cursor like an inclinated pen
        t.speed(7)
        
        stx = TurtleStepper(t, True)
        sty = TurtleStepper(t, False)
        actz = TurtlePen(t)
        
    else:
        pass
        
    printer = HomePrinter(stx, sty, actz)
    printer.draw_rect(-50, -50, 100, 100)
    
    if DEMO:
        turtle.done()
        
    