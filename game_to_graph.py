from manim import *
from colour import Color


class Game_To_Graph(Scene):
    def construct(self):
        
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares.shift(LEFT*4)
        self.play(Write(squares), run_time=1)   
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
        self.play(Write(red_circ), Write(red_circ_copy), 
                  Write(blue_circ), Write(blue_circ_copy), 
                  Write(green_circ), Write(green_circ_copy),
                    Write(yellow_circ), Write(yellow_circ_copy), run_time=1)
        self.wait(1.5)

        circles = VGroup(
            *[VGroup(Circle(color=WHITE,
                     fill_opacity=1).scale(0.15)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.7)
        circles.shift(RIGHT*3)
        self.play(Write(circles), run_time=1)

        # add edges between nodes
        edges = VGroup(
                    *[VGroup(Line(circles[0].get_center(), circles[1].get_center(), color=WHITE)),
                     VGroup(Line(circles[0].get_center(), circles[5].get_center(), color=WHITE)),
                     VGroup(Line(circles[1].get_center(), circles[2].get_center(), color=WHITE)),
                     VGroup(Line(circles[1].get_center(), circles[6].get_center(), color=WHITE)),
                     VGroup(Line(circles[2].get_center(), circles[3].get_center(), color=WHITE)),
                     VGroup(Line(circles[2].get_center(), circles[7].get_center(), color=WHITE)),
                     VGroup(Line(circles[3].get_center(), circles[4].get_center(), color=WHITE)),
                     VGroup(Line(circles[3].get_center(), circles[8].get_center(), color=WHITE)),
                     VGroup(Line(circles[4].get_center(), circles[9].get_center(), color=WHITE)),
                     VGroup(Line(circles[5].get_center(), circles[6].get_center(), color=WHITE)),
                     VGroup(Line(circles[5].get_center(), circles[10].get_center(), color=WHITE)),
                     VGroup(Line(circles[6].get_center(), circles[7].get_center(), color=WHITE)),
                     VGroup(Line(circles[6].get_center(), circles[11].get_center(), color=WHITE)),
                     VGroup(Line(circles[7].get_center(), circles[8].get_center(), color=WHITE)),
                     VGroup(Line(circles[7].get_center(), circles[12].get_center(), color=WHITE)),
                     VGroup(Line(circles[8].get_center(), circles[9].get_center(), color=WHITE)),
                     VGroup(Line(circles[8].get_center(), circles[13].get_center(), color=WHITE)),
                     VGroup(Line(circles[9].get_center(), circles[14].get_center(), color=WHITE)),
                     VGroup(Line(circles[10].get_center(), circles[11].get_center(), color=WHITE)),
                     VGroup(Line(circles[10].get_center(), circles[15].get_center(), color=WHITE)),
                     VGroup(Line(circles[11].get_center(), circles[12].get_center(), color=WHITE)),
                     VGroup(Line(circles[11].get_center(), circles[16].get_center(), color=WHITE)),
                     VGroup(Line(circles[12].get_center(), circles[13].get_center(), color=WHITE)),
                     VGroup(Line(circles[12].get_center(), circles[17].get_center(), color=WHITE)),
                        VGroup(Line(circles[13].get_center(), circles[14].get_center(), color=WHITE)),
                        VGroup(Line(circles[13].get_center(), circles[18].get_center(), color=WHITE)),
                        VGroup(Line(circles[14].get_center(), circles[19].get_center(), color=WHITE)),
                        VGroup(Line(circles[15].get_center(), circles[16].get_center(), color=WHITE)),
                        VGroup(Line(circles[16].get_center(), circles[17].get_center(), color=WHITE)),
                        VGroup(Line(circles[17].get_center(), circles[18].get_center(), color=WHITE)),
                        VGroup(Line(circles[18].get_center(), circles[19].get_center(), color=WHITE)),
                        VGroup(Line(circles[15].get_center(), circles[20].get_center(), color=WHITE)),
                        VGroup(Line(circles[16].get_center(), circles[21].get_center(), color=WHITE)),
                        VGroup(Line(circles[17].get_center(), circles[22].get_center(), color=WHITE)),
                        VGroup(Line(circles[18].get_center(), circles[23].get_center(), color=WHITE)),
                        VGroup(Line(circles[19].get_center(), circles[24].get_center(), color=WHITE)),
                        VGroup(Line(circles[20].get_center(), circles[21].get_center(), color=WHITE)),
                        VGroup(Line(circles[21].get_center(), circles[22].get_center(), color=WHITE)),
                        VGroup(Line(circles[22].get_center(), circles[23].get_center(), color=WHITE)),
                        VGroup(Line(circles[23].get_center(), circles[24].get_center(), color=WHITE))
            ])
        self.play(Write(edges), run_time=1)
        self.wait(1)

        # bring circles to front
        self.bring_to_front(circles[5], circles[22], circles[6], circles[8], circles[13], circles[15], circles[18], circles[20])

        # change color of circles[5] to red and enlarge it
        self.play(circles[5].animate.scale(1.6),
                  circles[22].animate.scale(1.6),
                   circles[6].animate.scale(1.6),
                    circles[8].animate.scale(1.6),
                     circles[13].animate.scale(1.6),
                      circles[15].animate.scale(1.6),
                       circles[18].animate.scale(1.6),
                        circles[20].animate.scale(1.6),
                                 run_time=0.3)
        self.play(circles[5].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                   circles[22].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                   circles[6].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                    circles[8].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                     circles[13].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                      circles[15].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                       circles[18].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                        circles[20].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                                 run_time=0.3)
        self.wait(1.5)
        # my_line = Line(squares[5].get_center(), squares[0].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20)
        # self.play(FadeIn(my_line), run_time=0.5)

        red_edges = VGroup(
            *[VGroup(Line(squares[5].get_center(), squares[0].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[0].get_center(), squares[1].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[1].get_center(), squares[2].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[2].get_center(), squares[3].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[3].get_center(), squares[4].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[4].get_center(), squares[9].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[9].get_center(), squares[14].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[14].get_center(), squares[19].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[19].get_center(), squares[24].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[24].get_center(), squares[23].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[23].get_center(), squares[22].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20))])
        self.play(Write(red_edges), run_time=3)

        red_path_animation_group = AnimationGroup(
            *[edges[1].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[1].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[2].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[2].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[4].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[3].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[6].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[4].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[5].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[8].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[9].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[17].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[14].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[26].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[19].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[35].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[24].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[39].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[23].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[38].animate.set_color(Color(hue=0, saturation=1, luminance=0.5))])
        
        self.play(red_path_animation_group, run_time=2)
        self.wait(1)

        green_edges = VGroup(
            *[VGroup(Line(squares[15].get_center(), squares[10].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[10].get_center(), squares[11].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[11].get_center(), squares[12].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[12].get_center(), squares[13].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20))])
        self.play(Write(green_edges), run_time=2)

        green_path_animation_group = AnimationGroup(
            *[edges[19].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     circles[10].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     edges[18].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     circles[11].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     edges[20].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     circles[12].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     edges[22].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5))])

        self.play(green_path_animation_group, run_time=2)
        self.wait(1)

        blue_edges = VGroup(
            *[VGroup(Line(squares[6].get_center(), squares[7].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[7].get_center(), squares[8].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), stroke_width=20))])
        self.play(Write(blue_edges), run_time=1)

        blue_path_animation_group = AnimationGroup(
            *[edges[11].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                     circles[7].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                     edges[13].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5))])
        
        self.play(blue_path_animation_group, run_time=1)
        

        yellow_edges = VGroup(
            *[VGroup(Line(squares[20].get_center(), squares[21].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[21].get_center(), squares[16].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[16].get_center(), squares[17].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[17].get_center(), squares[18].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20))])
        self.play(Write(yellow_edges), run_time=2)

        yellow_path_animation_group = AnimationGroup(
            *[edges[36].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     circles[21].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     edges[32].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     circles[16].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     edges[28].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     circles[17].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     edges[29].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5))])
        
        self.play(yellow_path_animation_group, run_time=2)
        self.wait(1)

        

        self.wait(3)
