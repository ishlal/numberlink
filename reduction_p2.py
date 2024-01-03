

from manim import *
from colour import Color

class reduction_p2(Scene):
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
        self.add(x_1_group)


        x_2_vertex = MathTex(r"x_2").scale(0.8)
        x_2_circ = Circle(color=WHITE).scale(0.35)
        x_2_vertex.move_to([-5.14860305, -0.00087135, 0])
        x_2_circ.move_to(x_2_vertex.get_center())
        x_2_prime = MathTex(r"x_2'").scale(0.8)
        x_2_prime.move_to([2.85139695, -0.00087135, 0])
        x_2_prime_circ = Circle(color=WHITE).scale(0.35)
        x_2_prime_circ.move_to(x_2_prime.get_center())
        x_2_group = VGroup(x_2_vertex, x_2_circ, x_2_prime, x_2_prime_circ)
        self.add(x_2_group)

        x_3_vertex = MathTex(r"x_3").scale(0.8)
        x_3_circ = Circle(color=WHITE).scale(0.35)
        x_3_vertex.move_to([-5.14860305, -1.20087135, 0])
        x_3_circ.move_to(x_3_vertex.get_center())
        x_3_prime = MathTex(r"x_3'").scale(0.8)
        x_3_prime.move_to([2.85139695, -1.20087135, 0])
        x_3_prime_circ = Circle(color=WHITE).scale(0.35)
        x_3_prime_circ.move_to(x_3_prime.get_center())
        x_3_group = VGroup(x_3_vertex, x_3_circ, x_3_prime, x_3_prime_circ)
        self.add(x_3_group)

        x_4_vertex = MathTex(r"x_4").scale(0.8)
        x_4_circ = Circle(color=WHITE).scale(0.35)
        x_4_vertex.move_to([-5.14860305, -2.40087135, 0])
        x_4_circ.move_to(x_4_vertex.get_center())
        x_4_prime = MathTex(r"x_4'").scale(0.8)
        x_4_prime.move_to([2.85139695, -2.40087135, 0])
        x_4_prime_circ = Circle(color=WHITE).scale(0.35)
        x_4_prime_circ.move_to(x_4_prime.get_center())
        x_4_group = VGroup(x_4_vertex, x_4_circ, x_4_prime, x_4_prime_circ)
        self.add(x_4_group)

        clause_1_vertex = MathTex(r"C_1").scale(0.8)
        clause_1_circ = Circle(color=WHITE).scale(0.35)
        clause_1_vertex.move_to([-3.64860305, 2.29912865, 0])
        clause_1_circ.move_to(clause_1_vertex.get_center())
        clause_1_prime = MathTex(r"C_1'").scale(0.8)
        clause_1_prime.move_to([-3.64860305, -3.40087135, 0])
        clause_1_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_1_prime_circ.move_to(clause_1_prime.get_center())
        clause_1_group = VGroup(clause_1_vertex, clause_1_circ, clause_1_prime, clause_1_prime_circ)
        self.add(clause_1_group)

        clause_2_vertex = MathTex(r"C_2").scale(0.8)
        clause_2_circ = Circle(color=WHITE).scale(0.35)
        clause_2_vertex.move_to([-1.14860305, 2.29912865, 0])
        clause_2_circ.move_to(clause_2_vertex.get_center())
        clause_2_prime = MathTex(r"C_2'").scale(0.8)
        clause_2_prime.move_to([-1.14860305, -3.40087135, 0])
        clause_2_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_2_prime_circ.move_to(clause_2_prime.get_center())
        clause_2_group = VGroup(clause_2_vertex, clause_2_circ, clause_2_prime, clause_2_prime_circ)
        self.add(clause_2_group)

        clause_3_vertex = MathTex(r"C_3").scale(0.8)
        clause_3_circ = Circle(color=WHITE).scale(0.35)
        clause_3_vertex.move_to([1.35139695, 2.29912865, 0])
        clause_3_circ.move_to(clause_3_vertex.get_center())
        clause_3_prime = MathTex(r"C_3'").scale(0.8)
        clause_3_prime.move_to([1.35139695, -3.40087135, 0])
        clause_3_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_3_prime_circ.move_to(clause_3_prime.get_center())
        clause_3_group = VGroup(clause_3_vertex, clause_3_circ, clause_3_prime, clause_3_prime_circ)
        self.add(clause_3_group)

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

        self.add(line_x_1_1, line_x_1_2, 
                 line_x_2_1, line_x_2_2, 
                 line_x_3_1, line_x_3_2, 
                 line_x_4_1, line_x_4_2, 
                 line_c_1_1, line_c_1_2, line_c_1_3, 
                 line_c_2_1, line_c_2_2, line_c_2_3, 
                 line_c_3_1, line_c_3_2, line_c_3_3)
        
        small_circle_n11 = Circle(color=WHITE).scale(0.1)
        small_circle_n11.set_fill(WHITE, opacity=1)
        small_circle_n11.move_to([-3.99860305, 0.84912865, 0])
        text_n111 = MathTex(r"n_{111}").scale(0.22)
        text_n111.set_color(BLACK)
        text_n111.move_to(small_circle_n11.get_center())
        small_circle_n11_group = VGroup(small_circle_n11, text_n111)
        self.add(small_circle_n11_group)

        small_circle_n120 = Circle(color=WHITE).scale(0.1)
        small_circle_n120.set_fill(WHITE, opacity=1)
        small_circle_n120.move_to([-3.64860305, 0.34912865, 0])
        text_n120 = MathTex(r"n_{120}").scale(0.22)
        text_n120.set_color(BLACK)
        text_n120.move_to(small_circle_n120.get_center())
        small_circle_n120_group = VGroup(small_circle_n120, text_n120)
        self.add(small_circle_n120_group)

        small_circle_n131 = Circle(color=WHITE).scale(0.1)
        small_circle_n131.set_fill(WHITE, opacity=1)
        small_circle_n131.move_to([-3.29860305, -1.55087135, 0])
        text_n131 = MathTex(r"n_{131}").scale(0.22)
        text_n131.set_color(BLACK)
        text_n131.move_to(small_circle_n131.get_center())
        small_circle_n131_group = VGroup(small_circle_n131, text_n131)
        self.add(small_circle_n131_group)

        small_circle_n210 = Circle(color=WHITE).scale(0.1)
        small_circle_n210.set_fill(WHITE, opacity=1)
        small_circle_n210.move_to([-1.49860305, 1.54912865, 0])
        text_n210 = MathTex(r"n_{210}").scale(0.22)
        text_n210.set_color(BLACK)
        text_n210.move_to(small_circle_n210.get_center())
        small_circle_n210_group = VGroup(small_circle_n210, text_n210)
        self.add(small_circle_n210_group)

        small_circle_n231 = Circle(color=WHITE).scale(0.1)
        small_circle_n231.set_fill(WHITE, opacity=1)
        small_circle_n231.move_to([-1.14860305, -1.55087135, 0])
        text_n231 = MathTex(r"n_{231}").scale(0.22)
        text_n231.set_color(BLACK)
        text_n231.move_to(small_circle_n231.get_center())
        small_circle_n231_group = VGroup(small_circle_n231, text_n231)
        self.add(small_circle_n231_group)

        small_circle_n241 = Circle(color=WHITE).scale(0.1)
        small_circle_n241.set_fill(WHITE, opacity=1)
        small_circle_n241.move_to([-0.79860305, -2.75087135, 0])
        text_n241 = MathTex(r"n_{241}").scale(0.22)
        text_n241.set_color(BLACK)
        text_n241.move_to(small_circle_n241.get_center())
        small_circle_n241_group = VGroup(small_circle_n241, text_n241)
        self.add(small_circle_n241_group)

        small_circle_n321 = Circle(color=WHITE).scale(0.1)
        small_circle_n321.set_fill(WHITE, opacity=1)
        small_circle_n321.move_to([1.00139695, -0.35087135, 0])
        text_n321 = MathTex(r"n_{321}").scale(0.22)
        text_n321.set_color(BLACK)
        text_n321.move_to(small_circle_n321.get_center())
        small_circle_n321_group = VGroup(small_circle_n321, text_n321)
        self.add(small_circle_n321_group)

        small_circle_n330 = Circle(color=WHITE).scale(0.1)
        small_circle_n330.set_fill(WHITE, opacity=1)
        small_circle_n330.move_to([1.35139695, -0.85087135, 0])
        text_n330 = MathTex(r"n_{330}").scale(0.22)
        text_n330.set_color(BLACK)
        text_n330.move_to(small_circle_n330.get_center())
        small_circle_n330_group = VGroup(small_circle_n330, text_n330)
        self.add(small_circle_n330_group)

        small_circle_n341 = Circle(color=WHITE).scale(0.1)
        small_circle_n341.set_fill(WHITE, opacity=1)
        small_circle_n341.move_to([1.70139695, -2.75087135, 0])
        text_n341 = MathTex(r"n_{341}").scale(0.22)
        text_n341.set_color(BLACK)
        text_n341.move_to(small_circle_n341.get_center())
        small_circle_n341_group = VGroup(small_circle_n341, text_n341)
        self.add(small_circle_n341_group)

        threeSATeq = MathTex(r"\varphi = (", r"x_1", r"\lor",  r"\overline{x_2}",  r"\lor",  r"x_3", r") \land (", r"\overline{x_1}",  
                             r"\lor",  r"x_3", r"\lor",  r"x_4", r") \land (", r"x_2",  r"\lor",  r"\overline{x_3}",  r"\lor",  r"x_4", r")")
        threeSATeq.to_edge(UP)
        phi = threeSATeq.copy()
        self.add(threeSATeq)

        self.wait(2)

        # self.play(FadeOut(threeSATeq))
        # generic_eq = MathTex(r"\varphi = (x_1 \lor \overline{x_2} \overline x_3) \land ...")
        # generic_eq.to_edge(UP)
        # self.play(Write(generic_eq), 
        #           FadeOut(small_circle_n210),
        #           FadeOut(small_circle_n231),
        #             FadeOut(small_circle_n241),
        #             FadeOut(small_circle_n321),
        #             FadeOut(small_circle_n330),
        #             FadeOut(small_circle_n341))
        # self.wait(1)

        
        # "let's take a look at the high and low paths for x_1. Both of these paths have one additional
        # vertex on the path. The vertex on the high path corresponds to the negated x_1 in clause 2
        # and the vertex on the low path corresponds to the negated x_1 in clause 1"

        self.play(
            line_x_1_1.animate.set_color(GREEN)
        )
        self.wait(0.5)
        self.play(line_x_1_2.animate.set_color(RED))
        self.wait(2)
        self.play(Indicate(threeSATeq[7]), Indicate(small_circle_n210))
        self.wait(0.5)
        self.play(threeSATeq[7].animate.set_color(PURPLE), small_circle_n210.animate.set_color(PURPLE))
        self.wait(0.5)
        self.play(Indicate(threeSATeq[1]), Indicate(small_circle_n11))
        self.wait(0.5)
        self.play(threeSATeq[1].animate.set_color(ORANGE), small_circle_n11.animate.set_color(ORANGE))
        self.wait(0.5)
        self.wait(2)

        # suppose we were to choose the high path for x_1, meaning that x_1 would have the assignment TRUE
        self.play(line_x_1_2.animate.set_color(WHITE), small_circle_n11.animate.set_color(WHITE), small_circle_n210.animate.set_color(WHITE), threeSATeq[1].animate.set_color(WHITE), threeSATeq[7].animate.set_color(WHITE))
        self.wait(0.5)
        text_x1_true = MathTex(r"x_1 = \text{TRUE}").set_color(GREEN).scale(0.7)
        text_x1_true.next_to(line_x_1_1, RIGHT)
        text_x1_true.shift(RIGHT)
        self.play(Write(text_x1_true), run_time=0.5)

        # since the high path contains vertex n_210, then we would be unable to choose the leftmost
        # path connecting C_2 and C_2' because the two paths share a vertex.

        self.play(Indicate(small_circle_n210))
        self.wait(0.5)
        self.play(Indicate(line_c_2_1))
        self.play(line_c_2_1.animate.set_color(ORANGE))
        self.wait(0.5)
        self.play(small_circle_n210.animate.set_color(Color(hue=0, saturation=1, luminance=0.5)))
        self.wait(1.5)

        # note how n_210 corresponds to the first literal of the second clause being evaluated
        # to FALSE since x_1 is negated
        self.play(Indicate(threeSATeq[7]))
        self.wait(1)
        old_threesateq7 = threeSATeq[7].copy()
        self.play(Transform(threeSATeq[7], MathTex(r"F").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).move_to(old_threesateq7.get_center())))
        self.wait(1)

        # instead suppose we chose the bottom path for x_1, meaning that x_1 is assigned false
        self.play(line_x_1_1.animate.set_color(WHITE), 
                  small_circle_n210.animate.set_color(WHITE), 
                  Transform(threeSATeq[7], old_threesateq7), 
                  FadeOut(text_x1_true),
                  line_c_2_1.animate.set_color(WHITE))
        
        self.play(line_x_1_2.animate.set_color(GREEN))
        self.wait(0.5)
        text_x1_false = MathTex(r"x_1 = \text{FALSE}").set_color(GREEN).scale(0.7)
        text_x1_false.next_to(line_x_1_2, RIGHT)
        text_x1_false.shift(RIGHT)
        self.play(Write(text_x1_false), run_time=0.5)
        self.wait(1.5)

        # now for c_1 and c_1' we cannot choose the leftmost path because of n_111
        self.play(Indicate(small_circle_n11))
        self.wait(0.5)
        self.play(Indicate(line_c_1_1))
        self.play(line_c_1_1.animate.set_color(ORANGE))
        self.wait(0.5)
        self.play(small_circle_n11.animate.set_color(Color(hue=0, saturation=1, luminance=0.5)))
        self.wait(1.5)

        # Again, note that this vertex corresponds to the first literal of the first clause being FALSE
        # with this, we can see that if a literal evaluates to FALSE, then the corresponding clause path cannot be chosen
    
        self.play(Indicate(threeSATeq[1]))
        self.wait(1)
        old_threesateq1 = threeSATeq[1].copy()
        self.play(Transform(threeSATeq[1], MathTex(r"F").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).move_to(old_threesateq1.get_center())))
        self.wait(2)
        self.play(FadeOut(text_x1_false), line_x_1_2.animate.set_color(WHITE), small_circle_n11.animate.set_color(WHITE), line_c_1_1.animate.set_color(WHITE), Transform(threeSATeq[1], old_threesateq1))

        # further, if all three literals within a clause are FALSE, then we cannot choose a single clause path
        # which is an issue since the clause vertices are in our terminal set.

        threesateq_1_copy = threeSATeq[1].copy()
        self.play(line_x_1_2.animate.set_color(ORANGE), small_circle_n11.animate.set_color(Color(hue=0, saturation=1, luminance=0.5)))
        self.play(Transform(threeSATeq[1], MathTex(r"F").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).move_to(threesateq_1_copy.get_center())))
        self.wait(0.3)
        threesateq_3_copy = threeSATeq[3].copy()
        self.play(line_x_2_1.animate.set_color(ORANGE), small_circle_n120.animate.set_color(Color(hue=0, saturation=1, luminance=0.5)))
        self.play(Transform(threeSATeq[3], MathTex(r"F").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).move_to(threesateq_3_copy.get_center())))
        self.wait(0.3)
        threesateq_5_copy = threeSATeq[5].copy()
        self.play(line_x_3_2.animate.set_color(ORANGE), small_circle_n131.animate.set_color(Color(hue=0, saturation=1, luminance=0.5)))
        self.play(Transform(threeSATeq[5], MathTex(r"F").scale(0.8).set_color(Color(hue=0, saturation=1, luminance=0.5)).move_to(threesateq_5_copy.get_center())))
        self.wait(1)
        self.play(Indicate(line_c_1_1), Indicate(line_c_1_2), Indicate(line_c_1_3))
        self.play(Indicate(line_c_1_1), Indicate(line_c_1_2), Indicate(line_c_1_3))
        self.wait(2)

        # But what happens when all literals in a clause are FALSE? Then the entire clause is FALSE,
        # and the entire 3SAT equation is false!

        phi_transform_1 = MathTex(r"\varphi = (", r"F", r") \land(\overline{x_1} \lor x_3 \lor x_4) \land(x_2 \lor \overline{x_3} \lor x_4)")
        phi_transform_1.to_edge(UP)
        phi_transform_1[1].set_color(Color(hue=0, saturation=1, luminance=0.5))
        self.play(Transform(threeSATeq, phi_transform_1))
        self.wait(2)
        phi_transform_2 = MathTex(r"\varphi = ", r"F")
        phi_transform_2.to_edge(UP)
        phi_transform_2[1].set_color(Color(hue=0, saturation=1, luminance=0.5))
        self.play(Transform(threeSATeq, phi_transform_2))
        self.wait(1)

        self.play(
            # FadeOut(threeSATeq),
            line_x_1_2.animate.set_color(WHITE),
            line_x_2_1.animate.set_color(WHITE),
            line_x_3_2.animate.set_color(WHITE),
            small_circle_n11.animate.set_color(WHITE),
            small_circle_n120.animate.set_color(WHITE),
            small_circle_n131.animate.set_color(WHITE),
        )
        self.wait(1)

        # create a group for the graph
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
        
        # self.play(graph_group.animate.scale(0.7).shift(RIGHT*3 + UP))
        graph_group_copy = graph_group.copy()
        #If our 3SAT formula is satisfiable, then there will be at least one literal that is true in 
        # each clause, giving us a flow solution

        self.play(Transform(threeSATeq, phi))

        text_var_1 = MathTex(r"x_1 = \text{TRUE}").set_color(GREEN).scale(0.7)
        text_var_2 = MathTex(r"x_2 = \text{FALSE}").set_color(RED).scale(0.7)
        text_var_3 = MathTex(r"x_3 = \text{TRUE}").set_color(GREEN).scale(0.7)
        text_var_4 = MathTex(r"x_4 = \text{TRUE}").set_color(GREEN).scale(0.7)

        text_var_1.next_to(x_1_group, RIGHT)
        text_var_2.next_to(x_2_group, RIGHT)
        text_var_3.next_to(x_3_group, RIGHT)
        text_var_4.next_to(x_4_group, RIGHT)
        text_group = VGroup(text_var_1, text_var_2, text_var_3, text_var_4)
        text_group_box = SurroundingRectangle(text_group, buff=0.1)
        self.play(Write(text_group), Write(text_group_box))
        self.wait(2)

        self.play(
            line_x_1_1.animate.set_color(ORANGE),
            line_x_2_2.animate.set_color(ORANGE),
            line_x_3_1.animate.set_color(ORANGE),
            line_x_4_1.animate.set_color(ORANGE),
        )

        self.wait(2)
        self.play(
            line_c_1_1.animate.set_color(ORANGE),
            line_c_2_2.animate.set_color(ORANGE),
            line_c_3_3.animate.set_color(ORANGE),
        )

        self.wait(5)

        # so now we've answered the question. Flow is an NP-Complete problem. It's pretty hard.
        star = Star(color=Color(hue=0.6, saturation=1, luminance=0.5)).scale(0.2)
        star.set_fill(Color(hue=0.6, saturation=1, luminance=0.5), opacity=1)
        star.shift(DOWN*2 + RIGHT*2)
        self.play(
            FadeOut(threeSATeq), FadeOut(text_group), FadeOut(text_group_box),
        )

        self.play(Transform(graph_group, star))

        oval = Ellipse(width=2.5, height=3, color=GRAY)
        oval.set_fill(GRAY, opacity=0.5)
        oval.shift(UP*1)
        text_p = Text("P").scale(1.3)
        text_p.move_to(oval.get_center())

        oval2 = Ellipse(width=9, height=4, color=GREEN)
        oval2.set_fill(GREEN, opacity=0.5)
        oval2.move_to(oval.get_center())
        oval2.shift([-1, 0, 0])
        oval2_center = oval2.get_center()
        self.bring_to_back(oval2)
        text_np = Text("NP").scale(1.3)
        text_np.move_to(oval2.get_center() + RIGHT*3.5)

        oval_3 = Ellipse(width=3, height=2, color=RED)
        oval_3.set_fill(RED, opacity=0.5)
        self.bring_to_front(oval_3)
        oval_3.move_to(oval.get_center() + LEFT * 3.8)
        text_np_complete = Text("NP-Complete").scale(0.6)
        text_np_complete.move_to(oval_3.get_center())
        self.play(Write(oval_3), Write(text_np_complete), Write(oval), Write(text_p), Write(oval2), Write(text_np))
        self.wait(1)
        self.bring_to_front(graph_group)
        self.play(graph_group.animate.move_to(text_np_complete.get_center() + DOWN*0.5))
        self.wait(2)

        # star_copy = Star(color=Color(hue=0.6, saturation=1, luminance=0.5)).scale(0.2)
        # star_copy.set_fill(Color(hue=0.6, saturation=1, luminance=0.5), opacity=1)
        # star_copy.move_to(graph_group.get_center())
        # star_copy.shift(DOWN*3)
        # self.play(FadeIn(star_copy))
        # graph_group_copy.scale(0.3)
        # graph_group_copy.move_to(star_copy.get_center() + RIGHT*2+UP*0)
        # graph_group_copy[7].set_color(ORANGE)
        # graph_group_copy[10].set_color(ORANGE)
        # graph_group_copy[11].set_color(ORANGE)
        # graph_group_copy[13].set_color(ORANGE)
        # graph_group_copy[15].set_color(ORANGE)
        # graph_group_copy[19].set_color(ORANGE)
        # graph_group_copy[23].set_color(ORANGE)

        # self.play(FadeIn(graph_group_copy))
        self.wait(3)


        