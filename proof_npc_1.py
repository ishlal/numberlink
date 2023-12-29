

from manim import *
from colour import Color

class proof_npc_1(Scene):
    def construct(self):
        text_show_np_complete = Text("To prove NP-Complete: ").scale(0.8)
        text_show_np_complete.next_to(surrounding_box, DOWN)
        text_show_np_complete.shift(DOWN*0.3)
        text_step_1 = Text("1. Show that it is in NP").scale(0.6)
        text_step_1.next_to(text_show_np_complete, DOWN)
        text_step_1.shift(LEFT*0.5)
        text_step_2 = Text("2. Perform reduction from existing \n\tNP Complete problem").scale(0.6)
        text_step_2.next_to(text_step_1, DOWN)
        text_step_2.shift(RIGHT*0.8)
        self.play(Write(text_show_np_complete), Write(text_step_1), Write(text_step_2), run_time=1)
        self.wait(1)
        self.play(text_step_1.animate.set_color(YELLOW))
        self.wait(1)
        text_quickly = Text(" -> Problems that can be checked quickly").scale(0.6)
        text_quickly.next_to(text_step_1, RIGHT)
        self.play(Write(text_quickly), run_time=1)
        self.wait(2)