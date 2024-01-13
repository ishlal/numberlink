

from manim import *
from colour import Color 

class title(Scene):
    def construct(self):
        text = Text("The History of Flow").scale(2)
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))