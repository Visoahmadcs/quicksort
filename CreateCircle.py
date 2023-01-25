from manim import *

class CreateCircle(Scene):
    def construct(self):
        #circle = Circle()
        #circle.set_fill(PINK, opacity=0.5)
        #self.play(Create(circle))

        square1 = Square()
        square2 = Square()
        square3 = Square()
        square4 = Square()
        #square1.set_fill(BLUE, opacity = 0.5)
        #square2.set_fill(BLUE, opacity = 0.5)
        #square3.set_fill(BLUE, opacity = 0.5)
        #square4.set_fill(BLUE, opacity = 0.5)
        
        #square.rotate(PI / 4)

        square2.next_to(square1,RIGHT)
        square3.next_to(square2,RIGHT)
        square4.next_to(square3,RIGHT)
        self.play(Create(square1))
        self.play(Create(square2))
        self.play(Create(square3))
        self.play(Create(square4))
        #self.play(Transform(square,circle))
        #self.play(FadeOut(square))