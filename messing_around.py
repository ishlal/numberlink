

from manim import *
from colour import Color

class messing(Scene):
    def construct(self):
        text = MathTex(r"6", r"\rightarrow", r"2").scale(1.5)
        self.play(Write(text))
        self.play(Indicate(text[0]))
        self.play(text[0].animate.set_color(RED))
        self.wait(2)