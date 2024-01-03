

from manim import *
from colour import Color

class reduction_p3(Scene):
    def construct(self):
        x_1_vertex = MathTex(r"x_1").scale(0.8)
        x_1_circ = Circle(color=WHITE).scale(0.35)
        x_1_vertex.move_to([-5.14860305, 1.19912865, 0])
        x_1_circ.move_to(x_1_vertex.get_center())
        x_1_prime = MathTex(r"x_1'").scale(0.8)
        x_1_prime.move_to([2.85139695, 1.19912865, 0])
        x_1_prime_circ = Circle(color=WHITE).scale(0.35)
        x_1_prime_circ.move_to(x_1_prime.get_center())
        x_1_group = VGroup(x_1_vertex, x_1_circ, x_1_prime, x_1_prime_circ)
        


        x_2_vertex = MathTex(r"x_2").scale(0.8)
        x_2_circ = Circle(color=WHITE).scale(0.35)
        x_2_vertex.move_to([-5.14860305, -0.00087135, 0])
        x_2_circ.move_to(x_2_vertex.get_center())
        x_2_prime = MathTex(r"x_2'").scale(0.8)
        x_2_prime.move_to([2.85139695, -0.00087135, 0])
        x_2_prime_circ = Circle(color=WHITE).scale(0.35)
        x_2_prime_circ.move_to(x_2_prime.get_center())
        x_2_group = VGroup(x_2_vertex, x_2_circ, x_2_prime, x_2_prime_circ)
        

        x_3_vertex = MathTex(r"x_3").scale(0.8)
        x_3_circ = Circle(color=WHITE).scale(0.35)
        x_3_vertex.move_to([-5.14860305, -1.20087135, 0])
        x_3_circ.move_to(x_3_vertex.get_center())
        x_3_prime = MathTex(r"x_3'").scale(0.8)
        x_3_prime.move_to([2.85139695, -1.20087135, 0])
        x_3_prime_circ = Circle(color=WHITE).scale(0.35)
        x_3_prime_circ.move_to(x_3_prime.get_center())
        x_3_group = VGroup(x_3_vertex, x_3_circ, x_3_prime, x_3_prime_circ)


        x_4_vertex = MathTex(r"x_4").scale(0.8)
        x_4_circ = Circle(color=WHITE).scale(0.35)
        x_4_vertex.move_to([-5.14860305, -2.40087135, 0])
        x_4_circ.move_to(x_4_vertex.get_center())
        x_4_prime = MathTex(r"x_4'").scale(0.8)
        x_4_prime.move_to([2.85139695, -2.40087135, 0])
        x_4_prime_circ = Circle(color=WHITE).scale(0.35)
        x_4_prime_circ.move_to(x_4_prime.get_center())
        x_4_group = VGroup(x_4_vertex, x_4_circ, x_4_prime, x_4_prime_circ)


        clause_1_vertex = MathTex(r"C_1").scale(0.8)
        clause_1_circ = Circle(color=WHITE).scale(0.35)
        clause_1_vertex.move_to([-3.64860305, 2.29912865, 0])
        clause_1_circ.move_to(clause_1_vertex.get_center())
        clause_1_prime = MathTex(r"C_1'").scale(0.8)
        clause_1_prime.move_to([-3.64860305, -3.40087135, 0])
        clause_1_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_1_prime_circ.move_to(clause_1_prime.get_center())
        clause_1_group = VGroup(clause_1_vertex, clause_1_circ, clause_1_prime, clause_1_prime_circ)


        clause_2_vertex = MathTex(r"C_2").scale(0.8)
        clause_2_circ = Circle(color=WHITE).scale(0.35)
        clause_2_vertex.move_to([-1.14860305, 2.29912865, 0])
        clause_2_circ.move_to(clause_2_vertex.get_center())
        clause_2_prime = MathTex(r"C_2'").scale(0.8)
        clause_2_prime.move_to([-1.14860305, -3.40087135, 0])
        clause_2_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_2_prime_circ.move_to(clause_2_prime.get_center())
        clause_2_group = VGroup(clause_2_vertex, clause_2_circ, clause_2_prime, clause_2_prime_circ)


        clause_3_vertex = MathTex(r"C_3").scale(0.8)
        clause_3_circ = Circle(color=WHITE).scale(0.35)
        clause_3_vertex.move_to([1.35139695, 2.29912865, 0])
        clause_3_circ.move_to(clause_3_vertex.get_center())
        clause_3_prime = MathTex(r"C_3'").scale(0.8)
        clause_3_prime.move_to([1.35139695, -3.40087135, 0])
        clause_3_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_3_prime_circ.move_to(clause_3_prime.get_center())
        clause_3_group = VGroup(clause_3_vertex, clause_3_circ, clause_3_prime, clause_3_prime_circ)


        line_x_1_1 = Line(x_1_circ.get_top(), x_1_prime_circ.get_top())
        line_x_1_2 = Line(x_1_circ.get_bottom(), x_1_prime_circ.get_bottom())
        line_x_2_1 = Line(x_2_circ.get_top(), x_2_prime_circ.get_top())
        line_x_2_2 = Line(x_2_circ.get_bottom(), x_2_prime_circ.get_bottom())
        line_x_3_1 = Line(x_3_circ.get_top(), x_3_prime_circ.get_top())
        line_x_3_2 = Line(x_3_circ.get_bottom(), x_3_prime_circ.get_bottom())
        line_x_4_1 = Line(x_4_circ.get_top(), x_4_prime_circ.get_top())
        line_x_4_2 = Line(x_4_circ.get_bottom(), x_4_prime_circ.get_bottom())
        line_c_1_1 = Line(clause_1_circ.get_left(), clause_1_prime_circ.get_left())
        line_c_1_2 = Line(clause_1_circ.get_bottom(), clause_1_prime_circ.get_top())
        line_c_1_3 = Line(clause_1_circ.get_right(), clause_1_prime_circ.get_right())
        line_c_2_1 = Line(clause_2_circ.get_left(), clause_2_prime_circ.get_left())
        line_c_2_2 = Line(clause_2_circ.get_bottom(), clause_2_prime_circ.get_top())
        line_c_2_3 = Line(clause_2_circ.get_right(), clause_2_prime_circ.get_right())
        line_c_3_1 = Line(clause_3_circ.get_left(), clause_3_prime_circ.get_left())
        line_c_3_2 = Line(clause_3_circ.get_bottom(), clause_3_prime_circ.get_top())
        line_c_3_3 = Line(clause_3_circ.get_right(), clause_3_prime_circ.get_right())

        
        
        small_circle_n11 = Circle(color=WHITE).scale(0.1)
        small_circle_n11.set_fill(WHITE, opacity=1)
        small_circle_n11.move_to([-3.99860305, 0.84912865, 0])
        text_n111 = MathTex(r"n_{111}").scale(0.22)
        text_n111.set_color(BLACK)
        text_n111.move_to(small_circle_n11.get_center())
        small_circle_n11_group = VGroup(small_circle_n11, text_n111)


        small_circle_n120 = Circle(color=WHITE).scale(0.1)
        small_circle_n120.set_fill(WHITE, opacity=1)
        small_circle_n120.move_to([-3.64860305, 0.34912865, 0])
        text_n120 = MathTex(r"n_{120}").scale(0.22)
        text_n120.set_color(BLACK)
        text_n120.move_to(small_circle_n120.get_center())
        small_circle_n120_group = VGroup(small_circle_n120, text_n120)


        small_circle_n131 = Circle(color=WHITE).scale(0.1)
        small_circle_n131.set_fill(WHITE, opacity=1)
        small_circle_n131.move_to([-3.29860305, -1.55087135, 0])
        text_n131 = MathTex(r"n_{131}").scale(0.22)
        text_n131.set_color(BLACK)
        text_n131.move_to(small_circle_n131.get_center())
        small_circle_n131_group = VGroup(small_circle_n131, text_n131)


        small_circle_n210 = Circle(color=WHITE).scale(0.1)
        small_circle_n210.set_fill(WHITE, opacity=1)
        small_circle_n210.move_to([-1.49860305, 1.54912865, 0])
        text_n210 = MathTex(r"n_{210}").scale(0.22)
        text_n210.set_color(BLACK)
        text_n210.move_to(small_circle_n210.get_center())
        small_circle_n210_group = VGroup(small_circle_n210, text_n210)


        small_circle_n231 = Circle(color=WHITE).scale(0.1)
        small_circle_n231.set_fill(WHITE, opacity=1)
        small_circle_n231.move_to([-1.14860305, -1.55087135, 0])
        text_n231 = MathTex(r"n_{231}").scale(0.22)
        text_n231.set_color(BLACK)
        text_n231.move_to(small_circle_n231.get_center())
        small_circle_n231_group = VGroup(small_circle_n231, text_n231)


        small_circle_n241 = Circle(color=WHITE).scale(0.1)
        small_circle_n241.set_fill(WHITE, opacity=1)
        small_circle_n241.move_to([-0.79860305, -2.75087135, 0])
        text_n241 = MathTex(r"n_{241}").scale(0.22)
        text_n241.set_color(BLACK)
        text_n241.move_to(small_circle_n241.get_center())
        small_circle_n241_group = VGroup(small_circle_n241, text_n241)


        small_circle_n321 = Circle(color=WHITE).scale(0.1)
        small_circle_n321.set_fill(WHITE, opacity=1)
        small_circle_n321.move_to([1.00139695, -0.35087135, 0])
        text_n321 = MathTex(r"n_{321}").scale(0.22)
        text_n321.set_color(BLACK)
        text_n321.move_to(small_circle_n321.get_center())
        small_circle_n321_group = VGroup(small_circle_n321, text_n321)


        small_circle_n330 = Circle(color=WHITE).scale(0.1)
        small_circle_n330.set_fill(WHITE, opacity=1)
        small_circle_n330.move_to([1.35139695, -0.85087135, 0])
        text_n330 = MathTex(r"n_{330}").scale(0.22)
        text_n330.set_color(BLACK)
        text_n330.move_to(small_circle_n330.get_center())
        small_circle_n330_group = VGroup(small_circle_n330, text_n330)


        small_circle_n341 = Circle(color=WHITE).scale(0.1)
        small_circle_n341.set_fill(WHITE, opacity=1)
        small_circle_n341.move_to([1.70139695, -2.75087135, 0])
        text_n341 = MathTex(r"n_{341}").scale(0.22)
        text_n341.set_color(BLACK)
        text_n341.move_to(small_circle_n341.get_center())
        small_circle_n341_group = VGroup(small_circle_n341, text_n341)

        line_x_1_1.set_color(ORANGE)
        line_x_2_2.set_color(ORANGE)
        line_x_3_1.set_color(ORANGE)
        line_x_4_1.set_color(ORANGE)
        line_c_1_1.set_color(ORANGE)
        line_c_2_2.set_color(ORANGE)
        line_c_3_3.set_color(ORANGE)

        graph_group = VGroup(x_1_group, x_2_group, x_3_group, x_4_group, 
                             clause_1_group, clause_2_group, clause_3_group,
                                line_x_1_1, line_x_1_2,
                                line_x_2_1, line_x_2_2,
                                line_x_3_1, line_x_3_2,
                                line_x_4_1, line_x_4_2,
                                line_c_1_1, line_c_1_2, line_c_1_3,
                                line_c_2_1, line_c_2_2, line_c_2_3,
                                line_c_3_1, line_c_3_2, line_c_3_3,
                                small_circle_n11_group, small_circle_n120_group, small_circle_n131_group,
                                small_circle_n210_group, small_circle_n231_group, small_circle_n241_group,
                                small_circle_n321_group, small_circle_n330_group, small_circle_n341_group)
        # move graph_group to center of screen
        graph_group.move_to([0, 0, 0])
        self.play(FadeIn(graph_group))
        self.wait(1)
        self.play(
            x_1_group[0:2].animate.set_color(YELLOW)
        )
        self.wait(0.1)
        self.play(
            x_1_group[2:4].animate.set_color(YELLOW)
        )
        self.wait(0.1)
        self.play(x_2_group[0:2].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(x_2_group[2:4].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(x_3_group[0:2].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(x_3_group[2:4].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(x_4_group[0:2].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(x_4_group[2:4].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(clause_1_group[0:2].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(clause_1_group[2:].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(clause_2_group[0:2].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(clause_2_group[2:].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(clause_3_group[0:2].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(clause_3_group[2:].animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(small_circle_n210.animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(small_circle_n11.animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(small_circle_n321.animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(small_circle_n330.animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(small_circle_n231.animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.play(small_circle_n341.animate.set_color(YELLOW), run_time=0.1)
        self.wait(0.1)
        self.wait(1.5)
        self.play(small_circle_n120.animate.set_color(Color(hue=0, saturation=1, luminance=0.5)), run_time=0.5)
        self.wait(0.5)
        self.play(small_circle_n131.animate.set_color(Color(hue=0, saturation=1, luminance=0.5)), run_time=0.5)
        self.wait(0.5)
        self.play(small_circle_n241.animate.set_color(Color(hue=0, saturation=1, luminance=0.5)), run_time=0.5)
        self.wait(2.5)

        #game version 1
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
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
        self.play(FadeOut(graph_group), FadeIn(squares), Write(text_version1), FadeIn(red_circ), FadeIn(red_circ_copy), 
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
        self.play(FadeIn(red_line_1), FadeIn(red_line_2), FadeIn(blue_line_1), FadeIn(blue_line_2), FadeIn(blue_line_3), FadeIn(blue_line_4), 
                  FadeIn(green_line_1), FadeIn(green_line_2), FadeIn(yellow_line_1))
        text_np_complete = Text("NP-complete").scale(0.7)
        text_np_complete.next_to(text_version1, DOWN)
        self.play(Write(text_np_complete))
        group_version_1 = VGroup(
            squares, red_circ, red_circ_copy, blue_circ, blue_circ_copy, green_circ, green_circ_copy, yellow_circ, yellow_circ_copy,
            red_line_1, red_line_2, blue_line_1, blue_line_2, blue_line_3, blue_line_4, green_line_1, green_line_2, yellow_line_1,
            text_version1, text_np_complete
        )
        self.wait(2)
        self.play(group_version_1.animate.shift(LEFT*5 + UP*2))
        image_paper = ImageMobject("images/lynch_paper.png").scale(0.7)
        self.play(FadeIn(image_paper))
        self.wait(4)

        self.play(image_paper.animate.scale(0.35).next_to(text_np_complete, DOWN))
        
        self.wait(2)

        #game version 2
        squares_2 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares_2.shift(UP*2)
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
        self.play(FadeIn(red_line_1_2), FadeIn(blue_line_1_2), FadeIn(blue_line_2_2), 
                  FadeIn(green_line_1_2), FadeIn(yellow_line_1_2), FadeIn(yellow_line_2_2), 
                  FadeIn(yellow_line_3_2), FadeIn(yellow_line_4_2), FadeIn(yellow_line_5_2))
        
        text_np_complete_2 = Text("NP-complete").scale(0.7)
        text_np_complete_2.next_to(text_version2, DOWN)
        self.play(Write(text_np_complete_2))
        group_version_2 = VGroup(
            squares_2, red_circ_2, red_circ_copy_2, blue_circ_2, blue_circ_copy_2, green_circ_2, green_circ_copy_2, yellow_circ_2, yellow_circ_copy_2,
            red_line_1_2, blue_line_1_2, blue_line_2_2, green_line_1_2, yellow_line_1_2, yellow_line_2_2, yellow_line_3_2, yellow_line_4_2, yellow_line_5_2,
            text_version2, text_np_complete_2
        )
        self.wait(2)
        image_paper = ImageMobject("images/japanese_paper.png").scale(0.8)
        # image_paper.next_to(text_np_complete_2, DOWN)
        self.play(FadeIn(image_paper))
        self.wait(4)
        self.play(image_paper.animate.scale(0.35).next_to(text_np_complete_2, DOWN))
        self.wait(2)
        # self.play(FadeOut(image_paper))
        # self.wait(2)

        #game version 3
        squares_3 = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares_3.shift(RIGHT*5 + UP*2)
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
        self.play(FadeIn(red_line_1_3), FadeIn(red_line_2_3), FadeIn(blue_line_1_3), 
                  FadeIn(blue_line_2_3), FadeIn(blue_line_3_3), FadeIn(blue_line_4_3), 
                  FadeIn(blue_line_5_3), FadeIn(blue_line_6_3), FadeIn(blue_line_7_3), 
                  FadeIn(blue_line_8_3), FadeIn(blue_line_9_3), FadeIn(blue_line_10_3), 
                  FadeIn(green_line_1_3), FadeIn(yellow_line_1_3), FadeIn(yellow_line_2_3), 
                  FadeIn(yellow_line_3_3))
        # group_version_3 = VGroup(
        #     squares_3, red_circ_3, red_circ_copy_3, blue_circ_3, blue_circ_copy_3, green_circ_3, green_circ_copy_3, yellow_circ_3, yellow_circ_copy_3,
        #     red_line_1_3, red_line_2_3, blue_line_1_3, blue_line_2_3, blue_line_3_3, blue_line_4_3, blue_line_5_3, blue_line_6_3, blue_line_7_3, blue_line_8_3, blue_line_9_3, blue_line_10_3,
        #     green_line_1_3, yellow_line_1_3, yellow_line_2_3, yellow_line_3_3,
        #     text_version3, text_np_complete_3
        # )
        text_np_complete_3 = Text("NP-complete").scale(0.7)
        text_np_complete_3.next_to(text_version3, DOWN)
        self.play(Write(text_np_complete_3))
        zig_zag_paper = ImageMobject("images/zigzag.png").scale(0.8)
        # image_paper.next_to(text_np_complete_2, DOWN)
        self.wait(1)
        self.play(FadeIn(zig_zag_paper))
        self.wait(4)
        self.play(zig_zag_paper.animate.scale(0.35).next_to(text_np_complete_3, DOWN))
        self.wait(2)
        self.wait(3)


