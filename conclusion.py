

from manim import *
from colour import Color 

class conclusion(Scene):
    def construct(self):
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares.shift(LEFT*4 + UP*1.2) 
        self.wait(1.4)
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
        game_group = VGroup(
            squares, red_circ, red_circ_copy, blue_circ, blue_circ_copy, green_circ, green_circ_copy, yellow_circ, yellow_circ_copy
        )
        game_group.scale(0.8)
        self.play(Write(game_group), run_time=1)
        phi = MathTex(r"\varphi = (x_1 \lor \overline{x_2} \lor x_3) \land (x_2 \lor x_3 \lor \overline{x_4})").scale(0.8)
        phi.shift(LEFT*2 + DOWN*3)
        self.play(Write(phi))

        persons = [5, 13, 2, 8, 3, 11, 16, 9]
        ages = [27, 72, 4, 29, 22, 18, 39, 21]

        square2 = VGroup(
            *[VGroup(Square(color=Color(hue = j/16, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.65),
                     Text("Person " + str(persons[j])+ "\nAge: " + str(ages[j])).scale(0.4))
                     for j in range(8)]
        ).arrange_in_grid(2, 4, buff=0).scale(0.8)
        square2.shift(RIGHT*2)
        self.play(Write(square2), run_time=1)
        self.wait(2)
        rounded_rect_v2 = RoundedRectangle(width=13, height=6.7, corner_radius=0.5, color=RED)
        rounded_rect_v2.set_fill(RED, opacity=0.5)
        self.bring_to_back(rounded_rect_v2)
        self.play(FadeIn(rounded_rect_v2))
        text_NP_complete = Text("NP-complete").scale(0.8)
        text_NP_complete.shift(UP*2.8 + RIGHT*3.2)
        self.play(Write(text_NP_complete))
        self.wait(2)
        self.play(FadeOut(game_group), FadeOut(phi), FadeOut(square2), FadeOut(rounded_rect_v2), FadeOut(text_NP_complete))
        


