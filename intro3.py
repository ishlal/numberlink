from manim import *
from colour import Color

class Intro3(Scene):
    def construct(self):
        squares_5 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        red_circ = Circle(color=Color(hue=0.0, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        blue_circ = Circle(color=Color(hue=0.6, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        green_circ = Circle(color=Color(hue=0.3, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        yellow_circ = Circle(color=Color(hue=0.15, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        red_circ.set_fill()
        red_circ_copy = red_circ.copy()
        blue_circ_copy = blue_circ.copy()
        green_circ_copy = green_circ.copy()
        yellow_circ_copy = yellow_circ.copy()
        red_circ.move_to(squares_5[3].get_center())
        red_circ_copy.move_to(squares_5[22].get_center())
        blue_circ.move_to(squares_5[7].get_center())
        blue_circ_copy.move_to(squares_5[19].get_center())
        green_circ.move_to(squares_5[4].get_center())
        green_circ_copy.move_to(squares_5[8].get_center())
        yellow_circ.move_to(squares_5[6].get_center())
        yellow_circ_copy.move_to(squares_5[24].get_center())
        game_group_5 = VGroup(
            squares_5, red_circ, blue_circ, green_circ, yellow_circ,
            red_circ_copy, blue_circ_copy, green_circ_copy, yellow_circ_copy
        )

        self.play(FadeIn(game_group_5))

        self.wait(2)

        squares_6 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(36)]
        ).arrange_in_grid(6, 6, buff=0)
        red_circ = Circle(color=Color(hue=0.0, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        blue_circ = Circle(color=Color(hue=0.6, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        green_circ = Circle(color=Color(hue=0.3, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        yellow_circ = Circle(color=Color(hue=0.15, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        orange_circ = Circle(color=Color(hue=0.1, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.35)
        red_circ_copy = red_circ.copy()
        blue_circ_copy = blue_circ.copy()
        green_circ_copy = green_circ.copy()
        yellow_circ_copy = yellow_circ.copy()
        orange_circ_copy = orange_circ.copy()
        red_circ.move_to(squares_6[0].get_center())
        red_circ_copy.move_to(squares_6[33].get_center())
        blue_circ.move_to(squares_6[21].get_center())
        blue_circ_copy.move_to(squares_6[30].get_center())
        green_circ.move_to(squares_6[6].get_center())
        green_circ_copy.move_to(squares_6[27].get_center())
        yellow_circ.move_to(squares_6[26].get_center())
        yellow_circ_copy.move_to(squares_6[31].get_center())
        orange_circ.move_to(squares_6[15].get_center())
        orange_circ_copy.move_to(squares_6[18].get_center())

        game_group_6 = VGroup(
            squares_6, red_circ, blue_circ, green_circ, yellow_circ, orange_circ,
            red_circ_copy, blue_circ_copy, green_circ_copy, yellow_circ_copy, orange_circ_copy
        )
        self.play(Transform(game_group_5, game_group_6))
        self.wait(2)

        squares_7 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.4) for j in range(49)]
        ).arrange_in_grid(7, 7, buff=0)

        red_circ.move_to(squares_7[16].get_center())
        red_circ_copy.move_to(squares_7[38].get_center())
        blue_circ.move_to(squares_7[2].get_center())
        blue_circ_copy.move_to(squares_7[42].get_center())
        green_circ.move_to(squares_7[1].get_center())
        green_circ_copy.move_to(squares_7[29].get_center())
        yellow_circ.move_to(squares_7[35].get_center())
        yellow_circ_copy.move_to(squares_7[40].get_center())
        orange_circ.move_to(squares_7[12].get_center())
        orange_circ_copy.move_to(squares_7[33].get_center())

        game_group_7 = VGroup(
            squares_7, red_circ, blue_circ, green_circ, yellow_circ, orange_circ,
            red_circ_copy, blue_circ_copy, green_circ_copy, yellow_circ_copy, orange_circ_copy
        )

        self.play(Transform(game_group_5, game_group_7))

        self.wait(2)

        squares_9 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(81)]
        ).arrange_in_grid(9, 9, buff=0)

        red_circ = Circle(color=Color(hue=0.0, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.25)
        blue_circ = Circle(color=Color(hue=0.6, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.25)
        green_circ = Circle(color=Color(hue=0.3, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.25)
        yellow_circ = Circle(color=Color(hue=0.15, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.25)
        orange_circ = Circle(color=Color(hue=0.1, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.25)
        pink_circ = Circle(color=Color(hue=0.9, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.25)
        cyan_circ = Circle(color=Color(hue=0.5, saturation=1.0, luminance=0.5), fill_opacity=1).scale(0.25)
        red_circ_copy = red_circ.copy()
        blue_circ_copy = blue_circ.copy()
        green_circ_copy = green_circ.copy()
        yellow_circ_copy = yellow_circ.copy()
        orange_circ_copy = orange_circ.copy()
        pink_circ_copy = pink_circ.copy()
        cyan_circ_copy = cyan_circ.copy()

        red_circ.move_to(squares_9[20].get_center())
        red_circ_copy.move_to(squares_9[60].get_center())
        blue_circ.move_to(squares_9[69].get_center())
        blue_circ_copy.move_to(squares_9[80].get_center())
        green_circ.move_to(squares_9[55].get_center())
        green_circ_copy.move_to(squares_9[62].get_center())
        yellow_circ.move_to(squares_9[39].get_center())
        yellow_circ_copy.move_to(squares_9[64].get_center())
        orange_circ.move_to(squares_9[68].get_center())
        orange_circ_copy.move_to(squares_9[71].get_center())
        pink_circ.move_to(squares_9[24].get_center())
        pink_circ_copy.move_to(squares_9[51].get_center())
        cyan_circ.move_to(squares_9[46].get_center())
        cyan_circ_copy.move_to(squares_9[77].get_center())



        red_edges = VGroup(
            *[VGroup(Line(squares_9[20].get_center(), squares_9[23].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[23].get_center(), squares_9[59].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[59].get_center(), squares_9[60].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20))])
        
        blue_edges = VGroup(
            *[VGroup(Line(squares_9[69].get_center(), squares_9[78].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[78].get_center(), squares_9[80].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), stroke_width=20))])
        
        green_edges = VGroup(
            *[VGroup(Line(squares_9[55].get_center(), squares_9[56].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[56].get_center(), squares_9[38].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[38].get_center(), squares_9[36].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[36].get_center(), squares_9[0].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[0].get_center(), squares_9[8].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[8].get_center(), squares_9[62].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20))])
        
        yellow_edges = VGroup(
            *[VGroup(Line(squares_9[39].get_center(), squares_9[66].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[66].get_center(), squares_9[64].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20))])

        orange_edges = VGroup(
            *[VGroup(Line(squares_9[68].get_center(), squares_9[67].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[67].get_center(), squares_9[31].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[31].get_center(), squares_9[28].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[28].get_center(), squares_9[10].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[10].get_center(), squares_9[16].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[16].get_center(), squares_9[70].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[70].get_center(), squares_9[71].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), stroke_width=20))])

        pink_edges = VGroup(
            *[VGroup(Line(squares_9[24].get_center(), squares_9[51].get_center(), color=Color(hue=0.9, saturation=1, luminance=0.5), stroke_width=20))])
        
        cyan_edges = VGroup(
            *[VGroup(Line(squares_9[46].get_center(), squares_9[45].get_center(), color=Color(hue=0.5, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[45].get_center(), squares_9[72].get_center(), color=Color(hue=0.5, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares_9[72].get_center(), squares_9[77].get_center(), color=Color(hue=0.5, saturation=1, luminance=0.5), stroke_width=20))])

        game_group_9 = VGroup(
            squares_9, red_circ, blue_circ, green_circ, yellow_circ, orange_circ, pink_circ, cyan_circ,
            red_circ_copy, blue_circ_copy, green_circ_copy, yellow_circ_copy, orange_circ_copy, pink_circ_copy, cyan_circ_copy
        )
        self.play(Transform(game_group_5, game_group_9))
        self.wait(3)
        self.play(FadeIn(red_edges), FadeIn(blue_edges), FadeIn(green_edges), FadeIn(yellow_edges), 
                  FadeIn(orange_edges), FadeIn(pink_edges), FadeIn(cyan_edges))
        # self.play(FadeIn(red_edges))
        # self.play(FadeIn(blue_edges))
        # self.play(FadeIn(green_edges))
        # self.play(FadeIn(yellow_edges))
        # self.play(FadeIn(orange_edges))
        # self.play(FadeIn(pink_edges))
        # self.play(FadeIn(cyan_edges))
        self.wait(2)
        self.play(FadeOut(red_edges), FadeOut(blue_edges), FadeOut(green_edges), FadeOut(yellow_edges),
                    FadeOut(orange_edges), FadeOut(pink_edges), FadeOut(cyan_edges),
                    FadeOut(game_group_5))

