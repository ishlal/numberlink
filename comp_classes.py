
from manim import *
from colour import Color

class complexity(Scene):
    def construct(self):
        # draw an oval
        oval = Ellipse(width=4, height=2, color=GRAY)
        oval.set_fill(GRAY, opacity=0.5)
        oval.shift(UP*1)
        text_p = Text("P").scale(1.5)
        text_p.move_to(oval.get_center())
        self.play(Write(oval), Write(text_p), run_time=1)
        self.wait(2)
        text_p_copy = text_p.copy()
        text_p_copy.move_to(text_p.get_center())
        self.play(text_p_copy.animate.move_to(DOWN*1.5 + LEFT * 4), run_time=1)
        self.wait(1)
        text_polynomial = Text(" = Polynomial Time").scale(0.8)
        text_polynomial.next_to(text_p_copy, RIGHT)
        text_polynomial.shift(RIGHT*0.2 + DOWN*0.1)
        self.play(Write(text_polynomial))
        self.wait(1)
        text_quickly = Text(" - Problems that can be solved quickly").scale(0.6)
        text_quickly.next_to(text_polynomial, DOWN)
        text_quickly.shift(DOWN*0.3)
        self.play(Write(text_quickly))
        self.wait(1)
        text_oldest = Text(" - Finding oldest person in group").scale(0.6)
        text_oldest.next_to(text_quickly, DOWN)
        self.play(Write(text_oldest))
        self.wait(1)
        self.play(FadeOut(text_p_copy), FadeOut(text_polynomial), FadeOut(text_quickly), FadeOut(text_oldest))
        self.wait(1)
        # draw an oval
        oval2 = Ellipse(width=8, height=4, color=GREEN)
        oval2.set_fill(GREEN, opacity=0.5)
        oval2.move_to(oval.get_center())
        self.bring_to_back(oval2)
        text_np = Text("NP").scale(1.5)
        text_np.move_to(oval2.get_center() + RIGHT*3)
        self.play(Write(oval2), Write(text_np), run_time=1)
        self.wait(1)
        text_np_copy = text_np.copy()
        text_np_copy.move_to(text_np.get_center())
        self.play(text_np_copy.animate.move_to(DOWN*1.5 + LEFT * 6), run_time=1)
        self.wait(1)
        text_nondeterministic = Text(" = Nondeterministic Polynomial Time").scale(0.8)
        text_nondeterministic.next_to(text_np_copy, RIGHT)
        text_nondeterministic.shift(RIGHT*0.2 + DOWN*0.1)
        self.play(Write(text_nondeterministic))
        self.wait(1)
        text_quickly = Text(" - Problems that can be checked quickly").scale(0.6)
        text_quickly.next_to(text_nondeterministic, DOWN)
        text_quickly.shift(DOWN*0.3)
        self.play(Write(text_quickly))
        self.wait(1)
        text_friends = Text(" - Checking if 8 people are pairwise friends").scale(0.6)
        text_friends.next_to(text_quickly, DOWN)
        self.play(Write(text_friends))
        self.wait(1)
        self.play(FadeOut(text_np_copy), FadeOut(text_nondeterministic), FadeOut(text_quickly), FadeOut(text_friends))
        self.wait(1)