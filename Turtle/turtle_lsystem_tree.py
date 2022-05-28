import turtle
s = turtle.getscreen()
turtle.hideturtle()
sent = "F"
length = 250
theta = 25

class Turt:
    t = turtle.Turtle()
    def render(self):
        self.t.speed(0)
        self.t.clear()
        self.t.hideturtle()
        self.t.penup()
        self.t.home()
        self.t.left(90)
        self.t.backward(450)
        self.t.pendown()
        pop = []
        pangle = []
        for letters in sent:
            if letters == 'F':
                self.t.forward(length)
            else:
                if letters == 'G':
                    self.t.penup()
                    self.t.forward(length)
                    self.t.pendown()
                else:
                    if letters == '+':
                        self.t.right(theta)
                    else:
                        if letters == '-':
                            self.t.left(theta)
                        else:
                            if letters == '[':
                                pop.append(self.t.pos())
                                pangle.append(self.t.heading())
                            else:
                                if letters == ']':
                                    self.t.penup()
                                    self.t.setpos(pop.pop())
                                    self.t.setheading(pangle.pop())
                                    self.t.pendown()

                            
class LSystem:
    next = ''
    def generate(self, sent):
        self.next = ''
        for letters in sent:
            if letters == 'F':
                self.next += "FF+[+F-F-F]-[-F+F+F]"
            else:
                self.next += letters
        return self.next

        

def generate(sent):
    next = ''
    for letters in sent:
        if letters == 'F':
            next += "FF+[+F-F-F]-[-F+F+F]"
        else:
            next += letters
    return next


turt = Turt()
ls = LSystem()
i = 0
while i < 2:
    turt.render()
    sent = ls.generate(sent)
    length /= 2
    i += 1
