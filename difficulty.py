
from manim import *
from colour import Color

class difficulty(Scene):
    def construct(self):
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares.shift(LEFT*4)
        red_circ = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        red_circ_copy = red_circ.copy()
        red_circ.move_to(squares[5].get_center())
        red_circ_copy.move_to(squares[22].get_center())
        blue_circ = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        blue_circ.move_to(squares[6].get_center())
        blue_circ_copy = blue_circ.copy()
        blue_circ_copy.move_to(squares[8].get_center())
        green_circ = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        green_circ.move_to(squares[13].get_center())
        green_circ_copy = green_circ.copy()
        green_circ_copy.move_to(squares[15].get_center())
        yellow_circ = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        yellow_circ.move_to(squares[18].get_center())
        yellow_circ_copy = yellow_circ.copy()
        yellow_circ_copy.move_to(squares[20].get_center())
        self.play(FadeIn(squares),Write(red_circ), Write(red_circ_copy), 
                  Write(blue_circ), Write(blue_circ_copy), 
                  Write(green_circ), Write(green_circ_copy),
                    Write(yellow_circ), Write(yellow_circ_copy), run_time=1)
        self.wait(0.5)
        text_hard = Text("How hard is this game?").scale(0.8)
        text_hard.shift(UP*1.5 + RIGHT*3)
        self.play(Write(text_hard))
        self.wait(0.6)
        red_squares = [5, 0, 1, 2, 3, 4, 9, 14, 19, 24, 23, 22]
        blue_squares = [6, 7, 8]
        green_squares = [15, 10, 11, 12, 13]
        yellow_squares = [18, 17, 16, 21, 20]
        # red_squares_group = VGroup(*[squares[i] for i in red_squares])
        # blue_squares_group = VGroup(*[squares[i] for i in blue_squares])
        # green_squares_group = VGroup(*[squares[i] for i in green_squares])
        # yellow_squares_group = VGroup(*[squares[i] for i in yellow_squares])

        # self.wait(1)
        for i in red_squares:
            self.play(squares[i].animate.set_fill(RED, opacity=1), run_time=0.1)
        self.wait(0.2)
        for i in blue_squares:
            self.play(squares[i].animate.set_fill(BLUE, opacity=1), run_time=0.1)
        self.wait(0.2)
        for i in green_squares:
            self.play(squares[i].animate.set_fill(GREEN, opacity=1), run_time=0.1)
        self.wait(0.2)
        for i in yellow_squares:
            self.play(squares[i].animate.set_fill(YELLOW, opacity=1), run_time=0.1)
        self.wait(0.5)
        text_notvery = Text("Not very").scale(0.8)
        text_notvery.next_to(text_hard, DOWN*2)
        self.play(Write(text_notvery))
        self.wait(0.5)
        self.play(FadeOut(text_notvery), FadeOut(text_hard))
        text_meaning = Text("What does it mean for a puzzle\nor problem to be hard?").scale(0.8)
        text_meaning.shift(UP*1.5 + RIGHT*3)
        self.play(Write(text_meaning))
        self.wait(2.5)
        self.play(FadeOut(text_meaning), FadeOut(squares), FadeOut(red_circ), FadeOut(red_circ_copy),
                    FadeOut(blue_circ), FadeOut(blue_circ_copy), FadeOut(green_circ), FadeOut(green_circ_copy),
                    FadeOut(yellow_circ), FadeOut(yellow_circ_copy))