from manim import *
from colour import Color

class three_versions(Scene):
    def construct(self):
        text_title = Text("Three Versions of Flow").scale(1.2)
        text_title.shift(UP*3)
        self.play(Write(text_title), run_time=1)
        self.wait(1)
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares.shift(LEFT*5)
        text_version1 = Text("Version 1").scale(0.7)
        text_version1.next_to(squares, DOWN)
        red_circ = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        red_circ_copy = red_circ.copy()
        red_circ.move_to(squares[20].get_center())
        red_circ_copy.move_to(squares[19].get_center())
        blue_circ = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        blue_circ.move_to(squares[15].get_center())
        blue_circ_copy = blue_circ.copy()
        blue_circ_copy.move_to(squares[4].get_center())
        green_circ = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        green_circ.move_to(squares[0].get_center())
        green_circ_copy = green_circ.copy()
        green_circ_copy.move_to(squares[7].get_center())
        yellow_circ = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        yellow_circ.move_to(squares[1].get_center())
        yellow_circ_copy = yellow_circ.copy()
        yellow_circ_copy.move_to(squares[3].get_center())
        self.play(FadeIn(squares), Write(text_version1), FadeIn(red_circ), FadeIn(red_circ_copy), 
                  FadeIn(blue_circ), FadeIn(blue_circ_copy), 
                  FadeIn(green_circ), FadeIn(green_circ_copy),
                    FadeIn(yellow_circ), FadeIn(yellow_circ_copy), run_time=1)
        red_line_1 = Line(squares[20].get_center(), squares[24].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_1.stroke_width = 15
        red_line_2 = Line(squares[24].get_center(), squares[19].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_2.stroke_width = 15
        blue_line_1 = Line(squares[15].get_center(), squares[18].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_1.stroke_width = 15
        blue_line_2 = Line(squares[18].get_center(), squares[13].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_2.stroke_width = 15
        blue_line_3 = Line(squares[13].get_center(), squares[14].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_3.stroke_width = 15
        blue_line_4 = Line(squares[14].get_center(), squares[4].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_4.stroke_width = 15
        green_line_1 = Line(squares[0].get_center(), squares[5].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1)
        green_line_1.stroke_width = 15
        green_line_2 = Line(squares[5].get_center(), squares[7].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1)
        green_line_2.stroke_width = 15
        yellow_line_1 = Line(squares[1].get_center(), squares[3].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_1.stroke_width = 15
        # self.play(FadeIn(red_line_1), FadeIn(red_line_2), FadeIn(blue_line_1), FadeIn(blue_line_2), FadeIn(blue_line_3), FadeIn(blue_line_4), 
        #           FadeIn(green_line_1), FadeIn(green_line_2), FadeIn(yellow_line_1))
        self.play(FadeIn(red_line_1), FadeIn(red_line_2))
        self.wait(0.5)
        self.play(FadeIn(blue_line_1), FadeIn(blue_line_2), FadeIn(blue_line_3), FadeIn(blue_line_4))
        self.wait(0.5)
        self.play(FadeIn(green_line_1), FadeIn(green_line_2))
        self.wait(0.5)
        self.play(FadeIn(yellow_line_1))
        self.wait(1)
        squares_2 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        # squares_2.shift(LEFT*5)
        text_version2 = Text("Version 2").scale(0.7)
        text_version2.next_to(squares_2, DOWN)
        # self.play(Write(text_version2), FadeIn(squares_2), run_time=1)
        red_circ_2 = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        red_circ_copy_2 = red_circ_2.copy()
        red_circ_2.move_to(squares_2[17].get_center())
        red_circ_copy_2.move_to(squares_2[19].get_center())
        blue_circ_2 = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        blue_circ_2.move_to(squares_2[10].get_center())
        blue_circ_copy_2 = blue_circ_2.copy()
        blue_circ_copy_2.move_to(squares_2[24].get_center())
        green_circ_2 = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        green_circ_2.move_to(squares_2[6].get_center())
        green_circ_copy_2 = green_circ_2.copy()
        green_circ_copy_2.move_to(squares_2[8].get_center())
        yellow_circ_2 = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        yellow_circ_2.move_to(squares_2[5].get_center())
        yellow_circ_copy_2 = yellow_circ_2.copy()
        yellow_circ_copy_2.move_to(squares_2[16].get_center())
        self.play(Write(text_version2), FadeIn(squares_2), FadeIn(red_circ_2), FadeIn(red_circ_copy_2), 
                  FadeIn(blue_circ_2), FadeIn(blue_circ_copy_2), 
                  FadeIn(green_circ_2), FadeIn(green_circ_copy_2),
                    FadeIn(yellow_circ_2), FadeIn(yellow_circ_copy_2), run_time=1)
        self.wait(1)
        
        red_line_1_2 = Line(squares_2[17].get_center(), squares_2[19].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_1_2.stroke_width = 15
        blue_line_1_2 = Line(squares_2[10].get_center(), squares_2[20].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_1_2.stroke_width = 15
        blue_line_2_2 = Line(squares_2[20].get_center(), squares_2[24].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_2_2.stroke_width = 15
        green_line_1_2 = Line(squares_2[6].get_center(), squares_2[8].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1)
        green_line_1_2.stroke_width = 15
        yellow_line_1_2 = Line(squares_2[5].get_center(), squares_2[0].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_1_2.stroke_width = 15
        yellow_line_2_2 = Line(squares_2[0].get_center(), squares_2[4].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_2_2.stroke_width = 15
        yellow_line_3_2 = Line(squares_2[4].get_center(), squares_2[14].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_3_2.stroke_width = 15
        yellow_line_4_2 = Line(squares_2[14].get_center(), squares_2[11].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_4_2.stroke_width = 15
        yellow_line_5_2 = Line(squares_2[11].get_center(), squares_2[16].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_5_2.stroke_width = 15
        # self.play(FadeIn(red_line_1_2), FadeIn(blue_line_1_2), FadeIn(blue_line_2_2), 
        #           FadeIn(green_line_1_2), FadeIn(yellow_line_1_2), FadeIn(yellow_line_2_2), 
        #           FadeIn(yellow_line_3_2), FadeIn(yellow_line_4_2), FadeIn(yellow_line_5_2))
        self.play(FadeIn(red_line_1_2))
        self.wait(0.5)
        self.play(FadeIn(blue_line_1_2), FadeIn(blue_line_2_2))
        self.wait(0.5)
        self.play(FadeIn(green_line_1_2))
        self.wait(0.5)
        self.play(FadeIn(yellow_line_1_2), FadeIn(yellow_line_2_2), FadeIn(yellow_line_3_2), FadeIn(yellow_line_4_2), FadeIn(yellow_line_5_2))
        self.wait(1.5)

        squares_3 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares_3.shift(RIGHT*5)
        text_version3 = Text("Version 3").scale(0.7)
        text_version3.next_to(squares_3, DOWN)

        red_circ_3 = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        red_circ_copy_3 = red_circ_3.copy()
        red_circ_3.move_to(squares_3[20].get_center())
        red_circ_copy_3.move_to(squares_3[19].get_center())
        blue_circ_3 = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        blue_circ_3.move_to(squares_3[15].get_center())
        blue_circ_copy_3 = blue_circ_3.copy()
        blue_circ_copy_3.move_to(squares_3[4].get_center())
        green_circ_3 = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        green_circ_3.move_to(squares_3[12].get_center())
        green_circ_copy_3 = green_circ_3.copy()
        green_circ_copy_3.move_to(squares_3[2].get_center())
        yellow_circ_3 = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.25)
        yellow_circ_3.move_to(squares_3[0].get_center())
        yellow_circ_copy_3 = yellow_circ_3.copy()
        yellow_circ_copy_3.move_to(squares_3[1].get_center())
        self.play(Write(text_version3), FadeIn(squares_3), FadeIn(red_circ_3), FadeIn(red_circ_copy_3), 
                  FadeIn(blue_circ_3), FadeIn(blue_circ_copy_3), 
                  FadeIn(green_circ_3), FadeIn(green_circ_copy_3),
                    FadeIn(yellow_circ_3), FadeIn(yellow_circ_copy_3), run_time=1)
        
        red_line_1_3 = Line(squares_3[20].get_center(), squares_3[24].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_1_3.stroke_width = 15
        red_line_2_3 = Line(squares_3[24].get_center(), squares_3[19].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_2_3.stroke_width = 15
        blue_line_1_3 = Line(squares_3[15].get_center(), squares_3[10].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_1_3.stroke_width = 15
        blue_line_2_3 = Line(squares_3[10].get_center(), squares_3[11].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_2_3.stroke_width = 15
        blue_line_3_3 = Line(squares_3[11].get_center(), squares_3[16].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_3_3.stroke_width = 15
        blue_line_4_3 = Line(squares_3[16].get_center(), squares_3[18].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_4_3.stroke_width = 15
        blue_line_5_3 = Line(squares_3[18].get_center(), squares_3[13].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_5_3.stroke_width = 15
        blue_line_6_3 = Line(squares_3[13].get_center(), squares_3[14].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_6_3.stroke_width = 15
        blue_line_7_3 = Line(squares_3[14].get_center(), squares_3[9].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_7_3.stroke_width = 15
        blue_line_8_3 = Line(squares_3[9].get_center(), squares_3[8].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_8_3.stroke_width = 15
        blue_line_9_3 = Line(squares_3[8].get_center(), squares_3[3].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_9_3.stroke_width = 15
        blue_line_10_3 = Line(squares_3[3].get_center(), squares_3[4].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_10_3.stroke_width = 15
        green_line_1_3 = Line(squares_3[12].get_center(), squares_3[2].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1)
        green_line_1_3.stroke_width = 15
        yellow_line_1_3 = Line(squares_3[0].get_center(), squares_3[5].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_1_3.stroke_width = 15
        yellow_line_2_3 = Line(squares_3[5].get_center(), squares_3[6].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_2_3.stroke_width = 15
        yellow_line_3_3 = Line(squares_3[6].get_center(), squares_3[1].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_3_3.stroke_width = 15
        # self.play(FadeIn(red_line_1_3), FadeIn(red_line_2_3), FadeIn(blue_line_1_3), 
        #           FadeIn(blue_line_2_3), FadeIn(blue_line_3_3), FadeIn(blue_line_4_3), 
        #           FadeIn(blue_line_5_3), FadeIn(blue_line_6_3), FadeIn(blue_line_7_3), 
        #           FadeIn(blue_line_8_3), FadeIn(blue_line_9_3), FadeIn(blue_line_10_3), 
        #           FadeIn(green_line_1_3), FadeIn(yellow_line_1_3), FadeIn(yellow_line_2_3), 
        #           FadeIn(yellow_line_3_3))
        self.play(FadeIn(red_line_1_3), FadeIn(red_line_2_3))
        self.wait(0.5)
        self.play(FadeIn(blue_line_1_3), FadeIn(blue_line_2_3), FadeIn(blue_line_3_3), FadeIn(blue_line_4_3), FadeIn(blue_line_5_3), FadeIn(blue_line_6_3), FadeIn(blue_line_7_3), FadeIn(blue_line_8_3), FadeIn(blue_line_9_3), FadeIn(blue_line_10_3))
        self.wait(0.5)
        self.play(FadeIn(green_line_1_3))
        self.wait(0.5)
        self.play(FadeIn(yellow_line_1_3), FadeIn(yellow_line_2_3), FadeIn(yellow_line_3_3))
        
        self.wait(3)
        self.play(FadeOut(blue_line_1_3), FadeOut(blue_line_2_3), FadeOut(blue_line_3_3), FadeOut(blue_line_4_3), FadeOut(blue_line_5_3), FadeOut(blue_line_6_3), FadeOut(blue_line_7_3), FadeOut(blue_line_8_3), FadeOut(blue_line_9_3), FadeOut(blue_line_10_3))
        self.wait(2)
        blue_line_short_1_3 = Line(squares_3[15].get_center(), squares_3[18].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_short_1_3.stroke_width = 15
        blue_line_short_2_3 = Line(squares_3[18].get_center(), squares_3[3].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_short_2_3.stroke_width = 15
        blue_line_short_3_3 = Line(squares_3[3].get_center(), squares_3[4].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_short_3_3.stroke_width = 15
        self.play(FadeIn(blue_line_short_1_3), FadeIn(blue_line_short_2_3), FadeIn(blue_line_short_3_3))
        self.wait(2)
        self.play(FadeOut(blue_line_short_1_3), FadeOut(blue_line_short_2_3), FadeOut(blue_line_short_3_3),
                  FadeIn(blue_line_1_3), FadeIn(blue_line_2_3), FadeIn(blue_line_3_3), FadeIn(blue_line_4_3), FadeIn(blue_line_5_3), FadeIn(blue_line_6_3), FadeIn(blue_line_7_3), FadeIn(blue_line_8_3), FadeIn(blue_line_9_3), FadeIn(blue_line_10_3))

        self.wait(3)
        # illuminate squares_2
        self.play(Indicate(squares), Indicate(squares_2))
        self.wait(3)
        self.play(FadeOut(squares), FadeOut(squares_2), FadeOut(text_version1), FadeOut(text_version2), FadeOut(red_circ), FadeOut(red_circ_copy),
                    FadeOut(blue_circ), FadeOut(blue_circ_copy), FadeOut(green_circ), FadeOut(green_circ_copy),
                    FadeOut(yellow_circ), FadeOut(yellow_circ_copy), FadeOut(red_circ_2), FadeOut(red_circ_copy_2),
                    FadeOut(blue_circ_2), FadeOut(blue_circ_copy_2), FadeOut(green_circ_2), FadeOut(green_circ_copy_2),
                    FadeOut(yellow_circ_2), FadeOut(yellow_circ_copy_2), FadeOut(red_line_1), FadeOut(red_line_2), FadeOut(blue_line_1), FadeOut(blue_line_2), FadeOut(blue_line_3), FadeOut(blue_line_4), 
                  FadeOut(green_line_1), FadeOut(yellow_line_1), FadeOut(text_version3), FadeOut(red_circ_3), FadeOut(red_circ_copy_3),
                    FadeOut(blue_circ_3), FadeOut(blue_circ_copy_3), FadeOut(green_circ_3), FadeOut(green_circ_copy_3),
                    FadeOut(yellow_circ_3), FadeOut(yellow_circ_copy_3), FadeOut(red_line_1_2), FadeOut(blue_line_1_2), FadeOut(blue_line_2_2), 
                  FadeOut(green_line_1_2), FadeOut(yellow_line_1_2), FadeOut(yellow_line_2_2), 
                  FadeOut(yellow_line_3_2), FadeOut(yellow_line_4_2), FadeOut(yellow_line_5_2), FadeOut(red_line_1_3), FadeOut(red_line_2_3), FadeOut(blue_line_1_3), 
                  FadeOut(blue_line_2_3), FadeOut(blue_line_3_3), FadeOut(blue_line_4_3), 
                  FadeOut(blue_line_5_3), FadeOut(blue_line_6_3), FadeOut(blue_line_7_3), 
                  FadeOut(blue_line_8_3), FadeOut(blue_line_9_3), FadeOut(blue_line_10_3),
                  FadeOut(green_line_1_3), FadeOut(yellow_line_1_3), FadeOut(yellow_line_2_3),
                  FadeOut(yellow_line_3_3), FadeOut(text_title))
        