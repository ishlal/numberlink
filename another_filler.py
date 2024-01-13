

from manim import *
from colour import Color 

class another_filler(Scene):
    def construct(self):
        text_paths = Text("Paths must be non-intersecting").scale(1.2)
        text_conc = Text("Have paths share vertices!").scale(1.2)
        
        text_paths.shift(UP)
        text_conc.shift(DOWN)
        line_conc = Line(start=text_conc.get_corner(DOWN+LEFT) + DOWN*0.3 + LEFT*0.3, end=text_conc.get_corner(DOWN+RIGHT) + DOWN*0.3 + RIGHT*0.3)
        self.play(Write(text_paths))
        self.wait(2)
        self.play(Write(text_conc), Write(line_conc))
        self.wait(2)