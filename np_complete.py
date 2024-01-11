

from manim import *
from colour import Color

class npcomplete(Scene):
    def construct(self):
        oval = Ellipse(width=2.5, height=3, color=GRAY)
        oval.set_fill(GRAY, opacity=0.5)
        oval.shift(UP*1)
        text_p = Text("P").scale(1.5)
        text_p.move_to(oval.get_center())
        # self.play(Write(oval), Write(text_p), run_time=1)
        self.add(oval, text_p)

        oval2 = Ellipse(width=9, height=4, color=GREEN)
        oval2.set_fill(GREEN, opacity=0.5)
        oval2.move_to(oval.get_center())
        oval2.shift([-1, 0, 0])
        self.bring_to_back(oval2)
        text_np = Text("NP").scale(1.5)
        text_np.move_to(oval2.get_center() + RIGHT*3.5)
        # self.play(Write(oval2), Write(text_np), run_time=1)
        self.add(oval2, text_np)
        self.bring_to_back(oval2)
        self.wait(1)

        oval_3 = Ellipse(width=3, height=2, color=RED)
        oval_3.set_fill(RED, opacity=0.5)
        self.bring_to_front(oval_3)
        oval_3.move_to(oval.get_center() + LEFT * 3.8)
        text_np_complete = Text("NP-Complete").scale(0.6)
        text_np_complete.move_to(oval_3.get_center())
        self.play(Write(oval_3), Write(text_np_complete), run_time=1)
        self.wait(2)
        text_copy = text_np_complete.copy()
        self.play(text_copy.animate.shift(DOWN*3))
        text_info = Text(": Problems that are the hardest in NP").scale(0.6)
        text_info.next_to(text_copy, RIGHT)
        self.play(Write(text_info))
        self.wait(2)
        self.play(FadeOut(text_info), FadeOut(text_copy))
        self.wait(1)

        # draw a star
        star = Star(color=YELLOW)
        star.set_fill(YELLOW, opacity=1)
        star.scale(0.15)
        star.move_to(oval_3.get_center() + DOWN*0.4)
        star_2 = Star(color=BLUE)
        star_2.set_fill(BLUE, opacity=1)
        star_2.scale(0.15)
        star_2.move_to(oval.get_center() + LEFT*0.7)
        star_2.shift(LEFT*1.2 + UP*1.5)
        star_3 = Star(color=PURPLE)
        star_3.set_fill(PURPLE, opacity=1)
        star_3.scale(0.15)
        star_3.move_to(oval.get_center() + RIGHT*0.7)
        star_3.shift(RIGHT*1.2 + DOWN*1.1)
        self.play(Write(star), Write(star_2), Write(star_3))
        self.wait(1)

        # draw a squiggly arrow
        squiggly_arrow = CurvedArrow(start_point=star_2.get_center(), end_point=star.get_center(), angle=-TAU/4)
        squiggly_arrow.set_color(WHITE)
        self.play(Write(squiggly_arrow))
        self.wait(1)
        squiggly_arrow_2 = CurvedArrow(start_point=star_3.get_center(), end_point=star.get_center(), angle=TAU/4)
        squiggly_arrow_2.set_color(WHITE)
        self.play(Write(squiggly_arrow_2))
        self.wait(1)
        self.play(FadeOut(squiggly_arrow), FadeOut(squiggly_arrow_2), FadeOut(star_2), FadeOut(star_3))
        self.wait(1)
        star_4 = Star(color=PINK)
        star_4.set_fill(PINK, opacity=1)
        star_4.scale(0.15)
        star_4.move_to(oval_3.get_center() + UP*0.4)
        self.play(Write(star_4))
        self.wait(1)
        squiggly_arrow_3 = CurvedArrow(start_point=star_4.get_center(), end_point=star.get_center(), angle=TAU/4)
        squiggly_arrow_3.set_color(WHITE)
        self.play(Write(squiggly_arrow_3))
        self.wait(1)
        self.play(FadeOut(squiggly_arrow_3), FadeOut(star_4), FadeOut(star))
        self.wait(2)

        oval_bpp = Ellipse(width=4, height=5, color=YELLOW)
        oval_bpp.set_fill(YELLOW, opacity=0.2)
        oval_bpp.move_to(oval.get_center())
        oval_bpp.shift([0, -1, 0])
        text_bpp = Text("BPP").scale(0.8)
        text_bpp.move_to(oval_bpp.get_center())
        self.play(Write(oval_bpp), Write(text_bpp), run_time=1)
        self.wait(2)
        # draw rounded corner rectangle
        rounded_rect = RoundedRectangle(width=10, height=6.6, corner_radius=0.5, color=BLUE)
        rounded_rect.shift(LEFT)
        rounded_rect.set_fill(BLUE, opacity=0.2)
        text_rect = Text("PSPACE").scale(0.8)
        # move text to top left corner of rounded rectangle
        text_rect.move_to(rounded_rect.get_center() + LEFT*4 + UP*2.8)
        self.play(Write(rounded_rect), Write(text_rect), run_time=1)
        self.wait(1)

        rounded_rect_v2 = RoundedRectangle(width=14, height=7.7, corner_radius=0.5, color=PURPLE)
        # rounded_rect.shift(LEFT)
        rounded_rect_v2.set_fill(PURPLE, opacity=0.2)
        text_rect_v2 = Text("EXP").scale(0.8)
        # move text to top left corner of rounded rectangle
        text_rect_v2.move_to(rounded_rect_v2.get_center() + LEFT*5.5 + UP*3.6)
        self.play(Write(rounded_rect_v2), Write(text_rect_v2), run_time=1)
        self.wait(3)
        self.play(FadeOut(rounded_rect), FadeOut(text_rect),
                  FadeOut(oval_bpp), FadeOut(text_bpp),
                  FadeOut(oval), FadeOut(text_p),
                  FadeOut(oval2), FadeOut(text_np),
                  FadeOut(oval_3), FadeOut(text_np_complete),
                  FadeOut(rounded_rect_v2), FadeOut(text_rect_v2),
                  run_time=1)
        self.wait(2)
