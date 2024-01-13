

from manim import *
from colour import Color 

class thumbnail(Scene):
    def construct(self):
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(36)]
        ).arrange_in_grid(6, 6, buff=0)
        squares.shift(LEFT*3.5)
        red_circ = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        red_circ_copy = red_circ.copy()
        red_circ.move_to(squares[9].get_center())
        red_circ_copy.move_to(squares[34].get_center())
        blue_circ = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        blue_circ.move_to(squares[15].get_center())
        blue_circ_copy = blue_circ.copy()
        blue_circ_copy.move_to(squares[33].get_center())
        green_circ = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        green_circ.move_to(squares[10].get_center())
        green_circ_copy = green_circ.copy()
        green_circ_copy.move_to(squares[28].get_center())
        yellow_circ = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        yellow_circ.move_to(squares[1].get_center())
        yellow_circ_copy = yellow_circ.copy()
        yellow_circ_copy.move_to(squares[12].get_center())
        orange_circ = Circle(color=Color(hue=0.1, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        orange_circ.move_to(squares[0].get_center())
        orange_circ_copy = orange_circ.copy()
        orange_circ_copy.move_to(squares[25].get_center())
        game_group = VGroup(red_circ, red_circ_copy, blue_circ, blue_circ_copy, green_circ, green_circ_copy, yellow_circ, yellow_circ_copy, 
                            orange_circ, orange_circ_copy, squares)
        game_group.scale(0.8)

        squares_2 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(36)]
        ).arrange_in_grid(6, 6, buff=0)
        squares_2.shift(RIGHT*3.5)
        red_circ_2 = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        red_circ_copy_2 = red_circ_2.copy()
        red_circ_2.move_to(squares_2[9].get_center())
        red_circ_copy_2.move_to(squares_2[34].get_center())
        blue_circ_2 = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        blue_circ_2.move_to(squares_2[15].get_center())
        blue_circ_copy_2 = blue_circ_2.copy()
        blue_circ_copy_2.move_to(squares_2[33].get_center())
        green_circ_2 = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        green_circ_2.move_to(squares_2[10].get_center())
        green_circ_copy_2 = green_circ_2.copy()
        green_circ_copy_2.move_to(squares_2[28].get_center())

        yellow_circ_2 = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        yellow_circ_2.move_to(squares_2[1].get_center())
        yellow_circ_copy_2 = yellow_circ_2.copy()
        yellow_circ_copy_2.move_to(squares_2[12].get_center())
        orange_circ_2 = Circle(color=Color(hue=0.1, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        orange_circ_2.move_to(squares_2[0].get_center())
        orange_circ_copy_2 = orange_circ_2.copy()
        orange_circ_copy_2.move_to(squares_2[25].get_center())

        STROKE_WIDTH = 23

        red_line_1 = Line(squares_2[9].get_center(), squares_2[3].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_1.stroke_width = STROKE_WIDTH
        red_line_2 = Line(squares_2[3].get_center(), squares_2[5].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_2.stroke_width = STROKE_WIDTH
        red_line_3 = Line(squares_2[5].get_center(), squares_2[35].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_3.stroke_width = STROKE_WIDTH
        red_line_4 = Line(squares_2[35].get_center(), squares_2[34].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_4.stroke_width = STROKE_WIDTH

        blue_line = Line(squares_2[15].get_center(), squares_2[33].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line.stroke_width = STROKE_WIDTH
        green_line = Line(squares_2[10].get_center(), squares_2[28].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1)
        green_line.stroke_width = STROKE_WIDTH

        yellow_line = Line(squares_2[1].get_center(), squares_2[2].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line.stroke_width = STROKE_WIDTH
        yellow_line_1 = Line(squares_2[2].get_center(), squares_2[32].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_1.stroke_width = STROKE_WIDTH
        yellow_line_2 = Line(squares_2[32].get_center(), squares_2[30].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_2.stroke_width = STROKE_WIDTH
        yellow_line_3 = Line(squares_2[30].get_center(), squares_2[12].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_3.stroke_width = STROKE_WIDTH

        orange_line = Line(squares_2[0].get_center(), squares_2[6].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), fill_opacity=1)
        orange_line.stroke_width = STROKE_WIDTH
        orange_line_1 = Line(squares_2[6].get_center(), squares_2[7].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), fill_opacity=1)
        orange_line_1.stroke_width = STROKE_WIDTH
        orange_line_2 = Line(squares_2[7].get_center(), squares_2[25].get_center(), color=Color(hue=0.1, saturation=1, luminance=0.5), fill_opacity=1)
        orange_line_2.stroke_width = STROKE_WIDTH

        game_group_2 = VGroup(red_circ_2, red_circ_copy_2, blue_circ_2, blue_circ_copy_2, green_circ_2, green_circ_copy_2, yellow_circ_2, yellow_circ_copy_2, 
                            orange_circ_2, orange_circ_copy_2, squares_2, red_line_1, red_line_2, red_line_3, red_line_4,
                            blue_line, green_line, yellow_line, yellow_line_1, yellow_line_2, yellow_line_3,
                            orange_line, orange_line_1, orange_line_2)
        game_group_2.scale(0.8)

        self.add(game_group, game_group_2)
        # self.add(
        #     squares_2,
        #     red_line_1, red_line_2, red_line_3, red_line_4, 
        #     blue_line, green_line, yellow_line, yellow_line_1, yellow_line_2, yellow_line_3,
        #     orange_line, orange_line_1, orange_line_2
        # )
        text_top = Text("How HARD are").scale(1.5)
        text_top.to_edge(UP)
        text_bottom = Text("Flow puzzles?").scale(1.5)
        text_bottom.to_edge(DOWN)
        self.add(text_top, text_bottom)
        