from manim import *
from colour import Color

class filler(Scene):
    def construct(self):
        text_about = Text("About The Game").scale(2.5)
        self.play(Write(text_about), run_time=3)
        self.wait(1)
        self.play(FadeOut(text_about))
        self.wait(1)