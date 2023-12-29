from manim import *
from colour import Color


class Game_To_Graph(Scene):
    def construct(self):
        
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares.shift(LEFT*4 + UP*1.2)
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
                     fill_opacity=1).scale(0.15),
                     Text(str(j+1)).scale(0.5).set_color(BLACK)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.7)
        circles.shift(RIGHT*3 + UP*1.2)
        self.play(Write(circles), run_time=1)

        self.wait(3)

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
        self.bring_to_front(circles)
        self.bring_to_back(edges)
        self.play(Write(edges), run_time=1)
        self.wait(1)

        # bring circles to front
        # self.bring_to_front(circles[5], circles[22], circles[6], circles[8], circles[13], circles[15], circles[18], circles[20])

        # change color of circles[5] to red and enlarge it
        self.play(circles[5][0].animate.scale(1.6),
                  circles[22][0].animate.scale(1.6),
                   circles[6][0].animate.scale(1.6),
                    circles[8][0].animate.scale(1.6),
                     circles[13][0].animate.scale(1.6),
                      circles[15][0].animate.scale(1.6),
                       circles[18][0].animate.scale(1.6),
                        circles[20][0].animate.scale(1.6),
                                 run_time=0.3)
        self.play(circles[5][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                   circles[22][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                   circles[6][0].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                    circles[8][0].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                     circles[13][0].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                      circles[15][0].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                       circles[18][0].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                        circles[20][0].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                                 run_time=0.3)
        self.wait(1.5)
        # my_line = Line(squares[5].get_center(), squares[0].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), stroke_width=20)
        # self.play(FadeIn(my_line), run_time=0.5)

        vertex_set = MathTex(r"V = \{1, 2, 3, 4, 5, 6, ... , 25\}").scale(0.9)
        vertex_set.next_to(squares, DOWN)
        self.play(Write(vertex_set), run_time=2)
        self.wait(1)

        edge_set = MathTex(r"E = \{\{1, 2\}, \{1,6\}, \{2, 3\}, ..., \{24, 25\}\}").scale(0.8)
        # align left of edge_set with left of vertex_set
        edge_set.next_to(vertex_set, DOWN)
        edge_set.shift(RIGHT*0.72)
        self.play(Write(edge_set), run_time=2)
        self.wait(1)

        terminal_set = MathTex(r"T = \{").scale(0.8)
        terminal_set.next_to(edge_set, DOWN)
        terminal_set.shift(LEFT*2.8)
        self.play(Write(terminal_set), run_time=1)

        red_vertex_1_copy = circles[5].copy()
        red_vertex_1_copy.move_to(circles[5].get_center())
        red_vertex_2_copy = circles[22].copy()
        red_vertex_2_copy.move_to(circles[22].get_center())
        group_red_vertex = VGroup(red_vertex_1_copy, red_vertex_2_copy)
        self.add(group_red_vertex)
        first_terminal_pair = MathTex(r"(6, 23)").set_color(Color(hue=0, saturation=1, luminance=0.5)).scale(0.8)
        first_terminal_pair.next_to(terminal_set, RIGHT)
        self.play(Transform(group_red_vertex, first_terminal_pair))
        self.wait(0.3)

        blue_vertex_1_copy = circles[6].copy()
        blue_vertex_1_copy.move_to(circles[6].get_center())
        blue_vertex_2_copy = circles[8].copy()
        blue_vertex_2_copy.move_to(circles[8].get_center())
        group_blue_vertex = VGroup(blue_vertex_1_copy, blue_vertex_2_copy)
        self.add(group_blue_vertex)
        second_terminal_pair = MathTex(r"(7, 9)").set_color(Color(hue=0.6, saturation=1, luminance=0.5)).scale(0.8)
        second_terminal_pair.next_to(first_terminal_pair, RIGHT)
        self.play(Transform(group_blue_vertex, second_terminal_pair))
        self.wait(0.3) 

        green_vertex_1_copy = circles[13].copy()
        green_vertex_1_copy.move_to(circles[13].get_center())
        green_vertex_2_copy = circles[15].copy()
        green_vertex_2_copy.move_to(circles[15].get_center())
        group_green_vertex = VGroup(green_vertex_1_copy, green_vertex_2_copy)
        self.add(group_green_vertex)
        third_terminal_pair = MathTex(r"(14, 16)").set_color(Color(hue=0.3, saturation=1, luminance=0.5)).scale(0.8)
        third_terminal_pair.next_to(second_terminal_pair, RIGHT)
        self.play(Transform(group_green_vertex, third_terminal_pair))
        self.wait(0.3)

        yellow_vertex_1_copy = circles[18].copy()
        yellow_vertex_1_copy.move_to(circles[18].get_center())
        yellow_vertex_2_copy = circles[20].copy()
        yellow_vertex_2_copy.move_to(circles[20].get_center())
        group_yellow_vertex = VGroup(yellow_vertex_1_copy, yellow_vertex_2_copy)
        self.add(group_yellow_vertex)
        fourth_terminal_pair = MathTex(r"(19, 21)").set_color(Color(hue=0.15, saturation=1, luminance=0.5)).scale(0.8)
        fourth_terminal_pair.next_to(third_terminal_pair, RIGHT)
        self.play(Transform(group_yellow_vertex, fourth_terminal_pair))

        terminal_set_end = MathTex(r"\}").scale(0.8)
        terminal_set_end.next_to(fourth_terminal_pair, RIGHT)
        self.play(Write(terminal_set_end), run_time=0.2)
        self.wait(2)

        # vertical line next to the sets
        anchor_pt = Dot()
        anchor_pt.next_to(terminal_set_end, RIGHT)
        line = Line(anchor_pt.get_center() + DOWN*0.3, anchor_pt.get_center() + UP*1.5)
        text_solution = Text("Solution Set: ").scale(0.6)
        # text_solution.next_to(line, RIGHT)
        text_solution.next_to(circles[22], DOWN)
        # text_solution.shift(UP*0.9 + RIGHT)
        self.play(Write(line), Write(text_solution), run_time=1)
        self.wait(1)


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
        
        self.bring_to_back(edges)
        self.play(Write(red_edges), run_time=3)

        red_path_animation_group = AnimationGroup(
            *[edges[1].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[0][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[1][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[2].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[2][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[4].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[3][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[6].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[4][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                    #  circles[5][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[8].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[9][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[17].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[14][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[26].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[19][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[35].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[24][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[39].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     circles[23][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
                     edges[38].animate.set_color(Color(hue=0, saturation=1, luminance=0.5))])
        self.bring_to_front(circles)
        self.play(red_path_animation_group, run_time=2)
        self.wait(1)
        # red_path = MathTex(r"6 \rightarrow 1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5  \
        #                    \rightarrow 10 \\ \rightarrow  15 \rightarrow 20 \rightarrow 25 \rightarrow 24 \rightarrow 23").scale(0.6)
        red_path = MathTex(r"6", r"\rightarrow", r"1", r"\rightarrow", r"2", r"\rightarrow", r"3", r"\rightarrow", r"4", r"\rightarrow", r"5", r"\rightarrow", r"10", 
                               r"\\", r"\rightarrow", r"15", r"\rightarrow", r"20", r"\rightarrow", r"25", r"\rightarrow", r"24", r"\rightarrow", r"23").scale(0.6)
        red_path.set_color(Color(hue=0, saturation=1, luminance=0.5))
        red_path.next_to(vertex_set, RIGHT)
        red_path.shift(RIGHT*2 + DOWN*0.5)
        red_path_group = VGroup(
            *[edges[1].copy(), circles[0].copy(), edges[0].copy(), circles[1].copy(), edges[2].copy(), 
              circles[2].copy(), edges[4].copy(), circles[3].copy(), edges[6].copy(), circles[4].copy(), 
              edges[8].copy(), circles[9].copy(), edges[17].copy(), circles[14].copy(), edges[26].copy(), 
              circles[19].copy(), edges[35].copy(), circles[24].copy(), edges[39].copy(), circles[23].copy(), 
              edges[38].copy()]
        )
        self.play(Transform(red_path_group, red_path))
        # self.play(Write(red_path), run_time=2)
        self.wait(1)

        green_edges = VGroup(
            *[VGroup(Line(squares[15].get_center(), squares[10].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[10].get_center(), squares[11].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[11].get_center(), squares[12].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[12].get_center(), squares[13].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), stroke_width=20))])
        self.play(Write(green_edges), run_time=2)

        green_path_animation_group = AnimationGroup(
            *[edges[19].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     circles[10][0].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     edges[18].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     circles[11][0].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     edges[20].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     circles[12][0].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
                     edges[22].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5))])

        self.play(green_path_animation_group, run_time=2)
        self.wait(1)

        # green_path = MathTex(r"16 \rightarrow 11 \rightarrow 12 \rightarrow 13 \rightarrow 14").scale(0.6)
        green_path = MathTex(r"16", r"\rightarrow", r"11", r"\rightarrow", r"12", r"\rightarrow", r"13", r"\rightarrow", r"14").scale(0.6)
        green_path.set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        green_path.next_to(red_path, DOWN)
        green_path_group = VGroup(
            *[edges[19].copy(), circles[10].copy(), edges[18].copy(), 
              circles[11].copy(), edges[20].copy(), circles[12].copy(), edges[22].copy()]
        )
        self.play(Transform(green_path_group, green_path))
        self.wait(1)

        blue_edges = VGroup(
            *[VGroup(Line(squares[6].get_center(), squares[7].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[7].get_center(), squares[8].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), stroke_width=20))])
        self.play(Write(blue_edges), run_time=1)

        blue_path_animation_group = AnimationGroup(
            *[edges[11].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                     circles[7][0].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                     edges[13].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5))])
        
        self.play(blue_path_animation_group, run_time=1)
        self.wait(1)

        # blue_path = MathTex(r"7 \rightarrow 8 \rightarrow 9").scale(0.6)
        blue_path = MathTex(r"7", r"\rightarrow", r"8", r"\rightarrow", r"9").scale(0.6)
        blue_path.set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        blue_path.next_to(green_path, DOWN)
        blue_path_group = VGroup(
            *[edges[11].copy(), circles[7].copy(), edges[13].copy(), circles[6].copy(), circles[8].copy()]
        )
        self.play(Transform(blue_path_group, blue_path))
        self.wait(1)
        

        yellow_edges = VGroup(
            *[VGroup(Line(squares[20].get_center(), squares[21].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[21].get_center(), squares[16].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[16].get_center(), squares[17].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20),
                     Line(squares[17].get_center(), squares[18].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), stroke_width=20))])
        self.play(Write(yellow_edges), run_time=2)

        yellow_path_animation_group = AnimationGroup(
            *[edges[36].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     circles[21][0].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     edges[32].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     circles[16][0].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     edges[28].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     circles[17][0].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
                     edges[29].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5))])
        
        self.play(yellow_path_animation_group, run_time=2)
        self.wait(1)
        # yellow_path = MathTex(r"21 \rightarrow 22 \rightarrow 17 \rightarrow 18 \rightarrow 19").scale(0.6)
        yellow_path = MathTex(r"21", r"\rightarrow", r"22", r"\rightarrow", r"17", r"\rightarrow", r"18", r"\rightarrow", r"19").scale(0.6)
        yellow_path.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        yellow_path.next_to(blue_path, DOWN)
        yellow_path_group = VGroup(
            *[edges[36].copy(), circles[21].copy(), edges[32].copy(), 
              circles[16].copy(), edges[28].copy(), circles[17].copy(), edges[29].copy()]
        )
        self.play(Transform(yellow_path_group, yellow_path))

        

        self.wait(1)

        self.play(FadeOut(squares), FadeOut(red_circ),
                  FadeOut(red_circ_copy), FadeOut(blue_circ),
                    FadeOut(blue_circ_copy), FadeOut(green_circ),
                        FadeOut(green_circ_copy), FadeOut(yellow_circ),
                        FadeOut(yellow_circ_copy), FadeOut(circles),
                        FadeOut(edges), FadeOut(vertex_set),
                            FadeOut(edge_set), FadeOut(terminal_set),
                            FadeOut(terminal_set_end), FadeOut(line),
                            FadeOut(text_solution),  FadeOut(anchor_pt),
                                FadeOut(red_edges), FadeOut(green_edges),
                                FadeOut(blue_edges), FadeOut(yellow_edges), 
                                FadeOut(group_red_vertex), FadeOut(group_blue_vertex), 
                                FadeOut(group_green_vertex), FadeOut(group_yellow_vertex), run_time=1)
        group_paths = VGroup(red_path_group, green_path_group, blue_path_group, yellow_path_group)
        self.play(group_paths.animate.scale(1.3))
        self.play(group_paths.animate.shift(UP*4+LEFT*6))
        self.wait(1)

        # add surrounding box
        surrounding_box = SurroundingRectangle(group_paths, color=WHITE)
        self.play(Write(surrounding_box), run_time=1)
        self.wait(1)

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

        text_check_quickly = Text("Check Solution").scale(0.6)
        text_check_quickly.next_to(red_path_group, RIGHT)
        text_check_quickly.shift(RIGHT*2 + UP)
        

        # add a horizontal line under text_check_quickly
        anchor_pt_2 = Dot()
        anchor_pt_2.next_to(text_check_quickly, DOWN)
        line_2 = Line(anchor_pt_2.get_center() + LEFT*2, anchor_pt_2.get_center() + RIGHT*2)
        self.play(FadeOut(text_show_np_complete), FadeOut(text_step_1), FadeOut(text_step_2), 
                  Transform(text_quickly, text_check_quickly),Write(line_2), run_time=1)
        self.wait(1)

        text_verify_1 = Text("1. All pairs of terminals \n\tare connected").scale(0.6)
        text_verify_1.next_to(line_2, DOWN)
        text_verify_2 = Text("2. All vertices are visited \n\texactly once").scale(0.6)
        text_verify_2.next_to(text_verify_1, DOWN)
        text_verify_3 = Text("3. Edges on path exist in graph").scale(0.6)
        text_verify_3.next_to(text_verify_2, DOWN)

        self.play(Write(text_verify_1), run_time=1)
        self.wait(1)
        self.play(Write(text_verify_2), run_time=1)
        self.wait(1)
        self.play(Write(text_verify_3), run_time=1)
        self.wait(1)

        self.play(text_verify_1.animate.set_color(YELLOW))

        # vertex_set = MathTex(r"V = \{1, 2, 3, 4, 5, 6, ... , 25\}").scale(0.9)
        # vertex_set.next_to(squares, DOWN)
        # edge_set = MathTex(r"E = \{\{1, 2\}, \{1,6\}, \{2, 3\}, ..., \{24, 25\}\}").scale(0.8)
        # # align left of edge_set with left of vertex_set
        # edge_set.next_to(vertex_set, DOWN)
        terminal_set = MathTex(r"T = \{(6, 23), (7, 9), (14, 16), (19, 21)\}").scale(0.8)
        terminal_set.next_to(edge_set, DOWN)
        self.play(Write(vertex_set), Write(edge_set), Write(terminal_set), run_time=1)
        self.wait(1)
        red_first = red_path_group[0].copy()
        red_first.move_to(red_path_group[0].get_center())
        red_last = red_path_group[-2:].copy()
        red_last.move_to(red_path_group[-2:].get_center())
        red_path_group_copy = VGroup(red_first, red_last)
        self.add(red_path_group_copy)
        terminal_1 = MathTex(r"(6, 23)")
        terminal_1.next_to(terminal_set, RIGHT)
        terminal_1.shift(RIGHT*2)
        terminal_1.scale(0.8)
        self.play(Transform(red_path_group_copy, terminal_1))
        self.wait(1)
        terminal_red_1 = MathTex(r"T = \{").scale(0.8)
        terminal_red_2 = MathTex(r"(6, 23)").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).next_to(terminal_red_1, RIGHT)
        terminal_red_3 = MathTex(r"(7, 9), (14, 16), (19, 21)\}").scale(0.8).next_to(terminal_red_2, RIGHT)
        terminal_red_group = VGroup(terminal_red_1, terminal_red_2, terminal_red_3)
        terminal_red_group.move_to(terminal_set.get_center())
        # self.play(terminal_1.animate.move_to(terminal_set[1:6].get_center()))
        self.play(FadeOut(red_path_group_copy), Transform(terminal_set, terminal_red_group))

        green_path_copy = green_path_group.copy()
        green_path_copy.move_to(green_path_group.get_center())
        self.add(green_path_copy)
        terminal_2 = MathTex(r"(14, 16)")
        terminal_2.next_to(terminal_set, RIGHT)
        terminal_2.shift(RIGHT*2)
        terminal_2.scale(0.8)
        self.play(Transform(green_path_copy, terminal_2))
        self.wait(1)
        terminal_green_1 = MathTex(r"T = \{").scale(0.8)
        terminal_green_2 = MathTex(r"(6, 23)").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).next_to(terminal_green_1, RIGHT)
        terminal_green_3 = MathTex(r"(7, 9), ").scale(0.8).next_to(terminal_green_2, RIGHT)
        terminal_green_4 = MathTex(r"(14, 16)").scale(0.8).set_color(Color(hue=0.3, saturation=1, luminance=0.5)).next_to(terminal_green_3, RIGHT)
        terminal_green_5 = MathTex(r"(19, 21)\}").scale(0.8).next_to(terminal_green_4, RIGHT)
        terminal_green_group = VGroup(terminal_green_1, terminal_green_2, terminal_green_3, terminal_green_4, terminal_green_5)
        terminal_green_group.move_to(terminal_set.get_center())
        self.play(FadeOut(green_path_copy), Transform(terminal_set, terminal_green_group))

        blue_path_copy = blue_path_group.copy()
        blue_path_copy.move_to(blue_path_group.get_center())
        self.add(blue_path_copy)
        terminal_3 = MathTex(r"(7, 9)")
        terminal_3.next_to(terminal_set, RIGHT)
        terminal_3.shift(RIGHT*2)
        terminal_3.scale(0.8)
        self.play(Transform(blue_path_copy, terminal_3))
        self.wait(1)
        terminal_blue_1 = MathTex(r"T = \{").scale(0.8)
        terminal_blue_2 = MathTex(r"(6, 23)").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).next_to(terminal_blue_1, RIGHT)
        terminal_blue_3 = MathTex(r"(7, 9)").scale(0.8).set_color(Color(hue=0.6, saturation=1, luminance=0.5)).next_to(terminal_blue_2, RIGHT)
        terminal_blue_4 = MathTex(r"(14, 16)").scale(0.8).set_color(Color(hue=0.3, saturation=1, luminance=0.5)).next_to(terminal_blue_3, RIGHT)
        terminal_blue_5 = MathTex(r"(19, 21)\}").scale(0.8).next_to(terminal_blue_4, RIGHT)
        terminal_blue_group = VGroup(terminal_blue_1, terminal_blue_2, terminal_blue_3, terminal_blue_4, terminal_blue_5)
        terminal_blue_group.move_to(terminal_set.get_center())
        self.play(FadeOut(blue_path_copy), Transform(terminal_set, terminal_blue_group))

        yellow_path_copy = yellow_path_group.copy()
        yellow_path_copy.move_to(yellow_path_group.get_center())
        self.add(yellow_path_copy)
        terminal_4 = MathTex(r"(19, 21)")
        terminal_4.next_to(terminal_set, RIGHT)
        terminal_4.shift(RIGHT*2)
        terminal_4.scale(0.8)
        self.play(Transform(yellow_path_copy, terminal_4))
        self.wait(1)
        terminal_yellow_1 = MathTex(r"T = \{").scale(0.8)
        terminal_yellow_2 = MathTex(r"(6, 23)").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).next_to(terminal_yellow_1, RIGHT)
        terminal_yellow_3 = MathTex(r"(7, 9)").scale(0.8).set_color(Color(hue=0.6, saturation=1, luminance=0.5)).next_to(terminal_yellow_2, RIGHT)
        terminal_yellow_4 = MathTex(r"(14, 16)").scale(0.8).set_color(Color(hue=0.3, saturation=1, luminance=0.5)).next_to(terminal_yellow_3, RIGHT)
        terminal_yellow_5 = MathTex(r"(19, 21)").scale(0.8).set_color(Color(hue=0.15, saturation=1, luminance=0.5)).next_to(terminal_yellow_4, RIGHT)
        terminal_yellow_6 = MathTex(r"\}").scale(0.8).next_to(terminal_yellow_5, RIGHT)
        terminal_yellow_group = VGroup(terminal_yellow_1, terminal_yellow_2, terminal_yellow_3, terminal_yellow_4, terminal_yellow_5, terminal_yellow_6)
        terminal_yellow_group.move_to(terminal_set.get_center())
        self.play(FadeOut(yellow_path_copy), Transform(terminal_set, terminal_yellow_group))

        self.wait(1)
        self.play(text_verify_1.animate.set_color(WHITE), text_verify_2.animate.set_color(YELLOW))

        longer_vertex_set = MathTex(r"V = \{", r"1, ", r"2, ", r"3, ", r"4, ", r"5, ", 
                                    r"6, ", r"7, ", r"8, ", r"9, ", r"10, ",
                                    r"11, ", r"12, ", r"13, ", r"14, ", r"15, ", 
                                    r"16, ", r"17, ", r"18, ", r"19, ", r"20, ",
                                    r"21, ", r"22, ", r"23, ", r"24, ", r"25", r"\}").scale(0.8)
        longer_vertex_set.shift(DOWN*1.5)
        self.play(Transform(vertex_set, longer_vertex_set))
        self.wait(1)
        self.play(Indicate(group_paths[0][0]), run_time=0.2)
        self.play(longer_vertex_set[6].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][2]), run_time=0.2)
        self.play(longer_vertex_set[1].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][4]), run_time=0.2)
        self.play(longer_vertex_set[2].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][6]), run_time=0.1)
        self.play(longer_vertex_set[3].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][8]), run_time=0.2)
        self.play(longer_vertex_set[4].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][10]), run_time=0.2)
        self.play(longer_vertex_set[5].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][12]), run_time=0.2)
        self.play(longer_vertex_set[10].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][15]), run_time=0.2)
        self.play(longer_vertex_set[15].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][17]), run_time=0.2)
        self.play(longer_vertex_set[20].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][19]), run_time=0.2)
        self.play(longer_vertex_set[25].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][21]), run_time=0.2)
        self.play(longer_vertex_set[24].animate.set_color(RED), run_time=0.2)
        self.play(Indicate(group_paths[0][23]), run_time=0.2)
        self.play(longer_vertex_set[23].animate.set_color(RED), run_time=0.2)
        self.wait(1)
        self.play(Indicate(group_paths[1][0]), run_time=0.2)
        self.play(longer_vertex_set[16].animate.set_color(GREEN), run_time=0.2)
        self.play(Indicate(group_paths[1][2]), run_time=0.2)
        self.play(longer_vertex_set[11].animate.set_color(GREEN), run_time=0.2)
        self.play(Indicate(group_paths[1][4]), run_time=0.2)
        self.play(longer_vertex_set[12].animate.set_color(GREEN), run_time=0.2)
        self.play(Indicate(group_paths[1][6]), run_time=0.2)
        self.play(longer_vertex_set[13].animate.set_color(GREEN), run_time=0.2)
        self.play(Indicate(group_paths[1][8]), run_time=0.2)
        self.play(longer_vertex_set[14].animate.set_color(GREEN), run_time=0.2)
        self.wait(1)
        self.play(Indicate(group_paths[2][0]), run_time=0.2)
        self.play(longer_vertex_set[7].animate.set_color(BLUE), run_time=0.2)
        self.play(Indicate(group_paths[2][2]), run_time=0.2)
        self.play(longer_vertex_set[8].animate.set_color(BLUE), run_time=0.2)
        self.play(Indicate(group_paths[2][4]), run_time=0.2)
        self.play(longer_vertex_set[9].animate.set_color(BLUE), run_time=0.2)
        self.wait(1)
        self.play(Indicate(group_paths[3][0]), run_time=0.2)
        self.play(longer_vertex_set[21].animate.set_color(YELLOW), run_time=0.2)
        self.play(Indicate(group_paths[3][2]), run_time=0.2)
        self.play(longer_vertex_set[22].animate.set_color(YELLOW), run_time=0.2)
        self.play(Indicate(group_paths[3][4]), run_time=0.2)
        self.play(longer_vertex_set[17].animate.set_color(YELLOW), run_time=0.2)
        self.play(Indicate(group_paths[3][6]), run_time=0.2)
        self.play(longer_vertex_set[18].animate.set_color(YELLOW), run_time=0.2)
        self.play(Indicate(group_paths[3][8]), run_time=0.2)
        self.play(longer_vertex_set[19].animate.set_color(YELLOW), run_time=0.2)
        self.wait(2)
        self.play(text_verify_2.animate.set_color(WHITE), text_verify_3.animate.set_color(YELLOW))
        self.wait(3)
        self.play(FadeOut(text_verify_1), FadeOut(text_verify_2), FadeOut(text_verify_3),
                  FadeOut(text_quickly), FadeOut(line_2), FadeOut(terminal_set),
                  FadeOut(vertex_set), FadeOut(edge_set), FadeOut(surrounding_box),
                    FadeOut(text_check_quickly), run_time=1)