

from manim import *
from colour import Color

class reduction_p4(Scene):
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
        graph_group.shift(LEFT*4)
        graph_group.scale(0.6)
        self.play(FadeIn(graph_group))
        self.wait(2)




        
        circles = VGroup(
            *[VGroup(Circle(color=WHITE,
                     fill_opacity=1).scale(0.15),
                     Text(str(j+1)).scale(0.5).set_color(BLACK)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.7)
        circles.shift(RIGHT*3)


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

        # bring circles to front
        # self.bring_to_front(circles[5], circles[22], circles[6], circles[8], circles[13], circles[15], circles[18], circles[20])

        # change color of circles[5] to red and enlarge it
        self.play(Write(circles), Write(edges), run_time=1)
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
        self.wait(2.5)

        text_non_planar = Text("Non-planar").scale(0.8)
        text_non_planar.next_to(graph_group, DOWN)
        self.play(Write(text_non_planar))
        text_planar = Text("Planar").scale(0.8)
        self.wait(1)
        text_planar.next_to(circles, DOWN)
        self.play(Write(text_planar))
        self.wait(3)

        #FadeOut everything
        self.play(FadeOut(graph_group), FadeOut(edges), FadeOut(circles), FadeOut(text_non_planar), FadeOut(text_planar))
        self.wait(2)
        non_planar_image = ImageMobject("images/non_planar.png")
        non_planar_image.to_edge(UP)
        self.play(FadeIn(non_planar_image))
        self.wait(1)
        non_planar_desc = ImageMobject("images/nonplanar_desc.png")
        non_planar_desc.next_to(non_planar_image, DOWN)
        self.play(FadeIn(non_planar_desc))
        self.wait(2)
        self.play(FadeOut(non_planar_image), FadeOut(non_planar_desc))
        self.wait(2)

