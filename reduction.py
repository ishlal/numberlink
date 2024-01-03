from manim import *
from colour import Color



class reduction(ZoomedScene):

    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_width=5,
            zoomed_display_height=3.5,
            image_frame_stroke_width=10,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
            },
            **kwargs
        )

    def construct(self):
        threeSATeq = MathTex(r"\varphi = (", r"x_1", r"\lor",  r"\overline{x_2}",  r"\lor",  r"x_3", r") \land (", r"\overline{x_1}",  
                             r"\lor",  r"x_3", r"\lor",  r"x_4", r") \land (", r"x_2",  r"\lor",  r"\overline{x_3}",  r"\lor",  r"x_4", r")")
        threeSATeq.to_edge(UP)
        threeSATeq_copy = threeSATeq.copy()
        self.play(Write(threeSATeq))

        x_1_copy = threeSATeq[1].copy()
        x_1_vertex = MathTex(r"x_1").scale(0.8)
        surrounding_circle_x_1 = Circle(color=WHITE).scale(0.35)
        x_1_vertex.move_to(x_1_copy.get_center())
        x_1_vertex.shift(DOWN*2 + LEFT*1)
        # surrounding_circle_x_1.surround(x_1_vertex)
        surrounding_circle_x_1.move_to(x_1_vertex.get_center())
        x_1_prime = MathTex(r"x_1'").scale(0.8)
        x_1_prime_circ = Circle(color=WHITE).scale(0.35)
        # x_1_prime.move_to(x_1_copy.get_center())
        # x_1_prime.shift(DOWN*3 + LEFT*1)
        x_1_prime.move_to(x_1_vertex.get_center() + RIGHT*4)
        # x_1_prime.next_to(x_1_vertex, RIGHT*4)
        # x_1_prime_circ.surround(x_1_prime)
        x_1_prime_circ.move_to(x_1_prime.get_center())
        x_1_group = VGroup(x_1_vertex, surrounding_circle_x_1, x_1_prime, x_1_prime_circ)
        self.play(Transform(x_1_copy, x_1_group))
        self.wait(1)

        x_2_copy = threeSATeq[3].copy()
        x_2_vertex = MathTex(r"x_2").scale(0.8)
        surrounding_circle_x_2 = Circle(color=WHITE).scale(0.35)
        x_2_vertex.move_to(x_1_vertex.get_center() + DOWN*1.2)
        surrounding_circle_x_2.move_to(x_2_vertex.get_center())
        x_2_prime = MathTex(r"x_2'").scale(0.8)
        x_2_prime_circ = Circle(color=WHITE).scale(0.35)
        x_2_prime.move_to(x_1_prime.get_center() + DOWN*1.2)
        x_2_prime_circ.move_to(x_2_prime.get_center())
        x_2_group = VGroup(x_2_vertex, surrounding_circle_x_2, x_2_prime, x_2_prime_circ)
        self.play(Transform(x_2_copy, x_2_group))
        self.wait(1)

        x_3_copy = threeSATeq[5].copy()
        x_3_vertex = MathTex(r"x_3").scale(0.8)
        surrounding_circle_x_3 = Circle(color=WHITE).scale(0.35)
        x_3_vertex.move_to(x_2_vertex.get_center() + DOWN*1.2)
        surrounding_circle_x_3.move_to(x_3_vertex.get_center())
        x_3_prime = MathTex(r"x_3'").scale(0.8)
        x_3_prime_circ = Circle(color=WHITE).scale(0.35)
        x_3_prime.move_to(x_2_prime.get_center() + DOWN*1.2)
        x_3_prime_circ.move_to(x_3_prime.get_center())
        x_3_group = VGroup(x_3_vertex, surrounding_circle_x_3, x_3_prime, x_3_prime_circ)
        self.play(Transform(x_3_copy, x_3_group))
        self.wait(1)

        x_4_copy = threeSATeq[11].copy()
        x_4_vertex = MathTex(r"x_4").scale(0.8)
        surrounding_circle_x_4 = Circle(color=WHITE).scale(0.35)
        x_4_vertex.move_to(x_3_vertex.get_center() + DOWN*1.2)
        surrounding_circle_x_4.move_to(x_4_vertex.get_center())
        x_4_prime = MathTex(r"x_4'").scale(0.8)
        x_4_prime_circ = Circle(color=WHITE).scale(0.35)
        x_4_prime.move_to(x_3_prime.get_center() + DOWN*1.2)
        x_4_prime_circ.move_to(x_4_prime.get_center())
        x_4_group = VGroup(x_4_vertex, surrounding_circle_x_4, x_4_prime, x_4_prime_circ)
        self.play(Transform(x_4_copy, x_4_group))
        self.wait(1)


        # draw edges between variable vertices.
        line_x_1_1 = Line(surrounding_circle_x_1.get_top(), x_1_prime_circ.get_top())
        line_x_1_2 = Line(surrounding_circle_x_1.get_bottom(), x_1_prime_circ.get_bottom())
        line_x_2_1 = Line(surrounding_circle_x_2.get_top(), x_2_prime_circ.get_top())
        line_x_2_2 = Line(surrounding_circle_x_2.get_bottom(), x_2_prime_circ.get_bottom())
        line_x_3_1 = Line(surrounding_circle_x_3.get_top(), x_3_prime_circ.get_top())
        line_x_3_2 = Line(surrounding_circle_x_3.get_bottom(), x_3_prime_circ.get_bottom())
        line_x_4_1 = Line(surrounding_circle_x_4.get_top(), x_4_prime_circ.get_top())
        line_x_4_2 = Line(surrounding_circle_x_4.get_bottom(), x_4_prime_circ.get_bottom())
        self.play(Write(line_x_1_1), Write(line_x_1_2), Write(line_x_2_1), 
                  Write(line_x_2_2), Write(line_x_3_1), Write(line_x_3_2), 
                  Write(line_x_4_1), Write(line_x_4_2))
        # move x1' and its circle to the right and extend the line
        # self.play(x_1_prime.animate.shift(RIGHT*2), x_1_prime_circ.animate.shift(RIGHT*2))
        # self.wait(2)
        self.wait(2)

        terminal_set = MathTex(r"T = \{(x_1, x_1'), (x_2, x_2'), (x_3, x_3'), (x_4, x_4')\}").scale(0.8)
        terminal_set.next_to(line_x_4_2, DOWN)
        self.play(Write(terminal_set))

        # draw the clause vertices

        clause_1_copy = threeSATeq[1:6].copy()
        clause_1_vertex = MathTex(r"C_1").scale(0.8)
        surrounding_circle_clause_1 = Circle(color=WHITE).scale(0.35)
        clause_1_vertex.move_to(x_1_prime.get_center() + RIGHT*3)
        clause_1_vertex.shift(UP*0.6)
        surrounding_circle_clause_1.move_to(clause_1_vertex.get_center())
        clause_1_vertex_prime = MathTex(r"C_1'").scale(0.8)
        clause_1_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_1_vertex_prime.move_to(clause_1_vertex.get_center() + DOWN*5)
        clause_1_prime_circ.move_to(clause_1_vertex_prime.get_center())
        clause_1_group = VGroup(clause_1_vertex, surrounding_circle_clause_1, clause_1_vertex_prime, clause_1_prime_circ)
        self.play(Transform(clause_1_copy, clause_1_group))
        # self.play(clause_1_copy.animate.set_color(YELLOW),
        #           surrounding_circle_clause_1.animate.set_color(YELLOW),
        #           clause_1_prime_circ.animate.set_color(YELLOW))

        clause_2_copy = threeSATeq[7:12].copy()
        clause_2_vertex = MathTex(r"C_2").scale(0.8)
        surrounding_circle_clause_2 = Circle(color=WHITE).scale(0.35)
        clause_2_vertex.move_to(clause_1_vertex.get_center() + RIGHT*2)
        surrounding_circle_clause_2.move_to(clause_2_vertex.get_center())
        clause_2_vertex_prime = MathTex(r"C_2'").scale(0.8)
        clause_2_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_2_vertex_prime.move_to(clause_2_vertex.get_center() + DOWN*5)
        clause_2_prime_circ.move_to(clause_2_vertex_prime.get_center())
        clause_2_group = VGroup(clause_2_vertex, surrounding_circle_clause_2, clause_2_vertex_prime, clause_2_prime_circ)
        self.play(Transform(clause_2_copy, clause_2_group))
        # self.play(clause_2_copy.animate.set_color(GREEN),
        #             surrounding_circle_clause_2.animate.set_color(GREEN),
        #             clause_2_prime_circ.animate.set_color(GREEN))

        clause_3_copy = threeSATeq[13:].copy()
        self.add(clause_3_copy)
        self.bring_to_front(clause_3_copy)
        clause_3_vertex = MathTex(r"C_3").scale(0.8)
        surrounding_circle_clause_3 = Circle(color=WHITE).scale(0.35)
        clause_3_vertex.move_to(clause_2_vertex.get_center() + RIGHT*2)
        surrounding_circle_clause_3.move_to(clause_3_vertex.get_center())
        clause_3_vertex_prime = MathTex(r"C_3'").scale(0.8)
        clause_3_prime_circ = Circle(color=WHITE).scale(0.35)
        clause_3_vertex_prime.move_to(clause_3_vertex.get_center() + DOWN*5)
        clause_3_prime_circ.move_to(clause_3_vertex_prime.get_center())
        clause_3_group = VGroup(clause_3_vertex, surrounding_circle_clause_3, clause_3_vertex_prime, clause_3_prime_circ)
        self.play(Transform(clause_3_copy, clause_3_group))
        # self.play(clause_3_copy.animate.set_color(RED),
        #             surrounding_circle_clause_3.animate.set_color(RED),
        #             clause_3_prime_circ.animate.set_color(RED))

        self.wait(2)

        line_c_1_1 = Line(surrounding_circle_clause_1.get_left(), clause_1_prime_circ.get_left())
        line_c_1_2 = Line(surrounding_circle_clause_1.get_bottom(), clause_1_prime_circ.get_top())
        line_c_1_3 = Line(surrounding_circle_clause_1.get_right(), clause_1_prime_circ.get_right())

        line_c_2_1 = Line(surrounding_circle_clause_2.get_left(), clause_2_prime_circ.get_left())
        line_c_2_2 = Line(surrounding_circle_clause_2.get_bottom(), clause_2_prime_circ.get_top())
        line_c_2_3 = Line(surrounding_circle_clause_2.get_right(), clause_2_prime_circ.get_right())

        line_c_3_1 = Line(surrounding_circle_clause_3.get_left(), clause_3_prime_circ.get_left())
        line_c_3_2 = Line(surrounding_circle_clause_3.get_bottom(), clause_3_prime_circ.get_top())
        line_c_3_3 = Line(surrounding_circle_clause_3.get_right(), clause_3_prime_circ.get_right())

        self.play(Write(line_c_1_1), Write(line_c_1_2), Write(line_c_1_3), 
                  Write(line_c_2_1), Write(line_c_2_2), Write(line_c_2_3), 
                  Write(line_c_3_1), Write(line_c_3_2), Write(line_c_3_3))
        self.wait(1)
        new_terminal_set = MathTex(r"T = \{(x_1, x_1'), (x_2, x_2'), (x_3, x_3'), (x_4, x_4'), (C_1, C_1'), (C_2, C_2'), (C_3, C_3')\}").scale(0.5)
        new_terminal_set.move_to(terminal_set.get_center())
        self.play(Transform(terminal_set, new_terminal_set))
        # self.play(Transform(threeSATeq[1], Text("T").move_to(threeSATeq[1].get_center()).scale(0.8).set_color(YELLOW)))
        
        
        # discuss the high and low paths for the variable vertices
        
        text_high = Text("High Path").scale(0.3).next_to(line_x_1_1, UP)
        self.play(Write(text_high))
        self.play(line_x_1_1.animate.set_color(YELLOW))
        self.wait(1)
        self.play(Transform(threeSATeq[1], MathTex(r"T").move_to(threeSATeq[1].get_center()).scale(0.8).set_color(YELLOW)))
        self.play(Transform(threeSATeq[7], MathTex(r"\overline{T}").move_to(threeSATeq[7].get_center()).scale(0.8).set_color(YELLOW)))

        text_low = Text("Low Path").scale(0.3).next_to(line_x_1_2, UP)
        self.play(Write(text_low))
        self.play(line_x_1_2.animate.set_color(RED))
        self.wait(1)
        self.play(Transform(threeSATeq[1], MathTex(r"F").move_to(threeSATeq[1].get_center()).scale(0.8).set_color(RED)))
        self.play(Transform(threeSATeq[7], MathTex(r"\overline{F}").move_to(threeSATeq[7].get_center()).scale(0.8).set_color(RED)))

        self.wait(2)

        # reset

        self.play(FadeOut(text_high), FadeOut(text_low), 
                  line_x_1_1.animate.set_color(WHITE), 
                  line_x_1_2.animate.set_color(WHITE),
                  Transform(threeSATeq[1], MathTex(r"x_1").move_to(threeSATeq[1].get_center())),
                    Transform(threeSATeq[7], MathTex(r"\overline{x_1}").move_to(threeSATeq[7].get_center())))
        self.wait(1)


        # discuss the three paths for the clause vertices

        self.play(line_c_2_1.animate.set_color(YELLOW))
        self.wait(1)
        self.play(Transform(threeSATeq[7], MathTex(r"T").move_to(threeSATeq[7].get_center()).scale(0.8).set_color(YELLOW)))

        self.wait(1)
        self.play(line_c_2_1.animate.set_color(WHITE))
        self.play(Transform(threeSATeq[7], MathTex(r"\overline{x_1}").move_to(threeSATeq[7].get_center())))
        
        self.play(line_c_2_2.animate.set_color(YELLOW))
        self.wait(1)
        self.play(Transform(threeSATeq[9], MathTex(r"T").move_to(threeSATeq[9].get_center()).scale(0.8).set_color(YELLOW)))

        self.wait(1)
        self.play(line_c_2_2.animate.set_color(WHITE))
        self.play(Transform(threeSATeq[9], MathTex(r"x_3").move_to(threeSATeq[9].get_center())))

        self.play(line_c_2_3.animate.set_color(YELLOW))
        self.wait(1)
        self.play(Transform(threeSATeq[11], MathTex(r"T").move_to(threeSATeq[11].get_center()).scale(0.8).set_color(YELLOW)))

        self.wait(1)
        self.play(line_c_2_3.animate.set_color(WHITE))
        self.play(Transform(threeSATeq[11], MathTex(r"x_4").move_to(threeSATeq[11].get_center())))

        self.wait(2)

        text_var_1 = MathTex(r"x_1 = \text{TRUE}").set_color(GREEN).scale(0.7)
        text_var_2 = MathTex(r"x_2 = \text{FALSE}").set_color(RED).scale(0.7)
        text_var_3 = MathTex(r"x_3 = \text{TRUE}").set_color(GREEN).scale(0.7)
        text_var_4 = MathTex(r"x_4 = \text{TRUE}").set_color(GREEN).scale(0.7)
        text_var_1.next_to(threeSATeq, DOWN)
        text_var_1.shift(LEFT*4.5)
        text_var_2.next_to(threeSATeq, DOWN)
        text_var_2.shift(LEFT*1.5)
        text_var_3.next_to(threeSATeq, DOWN)
        text_var_3.shift(RIGHT*1.5)
        text_var_4.next_to(threeSATeq, DOWN)
        text_var_4.shift(RIGHT*4.5)
        # text_var_2.shift(UP*3, LEFT*1.5)
        # text_var_3.shift(UP*3, RIGHT*1.5)
        # text_var_4.shift(UP*3, RIGHT*4.5)
        group_vals = VGroup(text_var_1, text_var_2, text_var_3, text_var_4)
        surr_box = SurroundingRectangle(group_vals)
        self.play(Write(group_vals), Write(surr_box), FadeOut(terminal_set))
        self.wait(1)

        self.play(
            line_x_1_1.animate.set_color(GREEN),
            line_x_2_2.animate.set_color(RED),
            line_x_3_1.animate.set_color(GREEN),
            line_x_4_1.animate.set_color(GREEN),
        )
        self.wait(1)
        
        self.play(Indicate(text_var_1))
        phi_x1_in = MathTex(r"\varphi = (", r"T", r"\lor \overline{x_2} \lor x_3) \land (", r"F",
                            r"\lor x_3 \lor x_4) \land (", r"x_2", r"\lor \overline{x_3} \lor x_4)").scale(0.8)
        phi_x1_in.to_edge(UP)
        phi_x1_in[1].set_color(YELLOW)
        phi_x1_in[3].set_color(YELLOW)
        self.play(Transform(threeSATeq, phi_x1_in))
        self.wait(1)

        self.play(Indicate(text_var_2))
        phi_x2_in = MathTex(r"\varphi = (", r"T", r"\lor", r"T", r" \lor x_3) \land (", r"F",
                            r"\lor x_3 \lor x_4) \land (", r"F", r"\lor \overline{x_3} \lor x_4)").scale(0.8)
        phi_x2_in.to_edge(UP)
        phi_x2_in[1].set_color(YELLOW)
        phi_x2_in[3].set_color(YELLOW)
        phi_x2_in[5].set_color(YELLOW)
        phi_x2_in[7].set_color(YELLOW)
        self.play(Transform(threeSATeq, phi_x2_in))
        self.wait(1)

        self.play(Indicate(text_var_3))
        phi_x3_in = MathTex(r"\varphi = (", r"T", r"\lor", r"T", r" \lor", r"T", r") \land (", r"F",
                            r"\lor", r"T",  r"\lor x_4) \land (", r"F", r"\lor", r"F", r" \lor x_4)").scale(0.8)
        phi_x3_in.to_edge(UP)
        phi_x3_in[1].set_color(YELLOW)
        phi_x3_in[3].set_color(YELLOW)
        phi_x3_in[5].set_color(YELLOW)
        phi_x3_in[7].set_color(YELLOW)
        phi_x3_in[9].set_color(YELLOW)
        phi_x3_in[11].set_color(YELLOW)
        phi_x3_in[13].set_color(YELLOW)
        self.play(Transform(threeSATeq, phi_x3_in))
        self.wait(1)

        self.play(Indicate(text_var_4))
        phi_x4_in = MathTex(r"\varphi = (", r"T", r"\lor", r"T", r" \lor", r"T", r") \land (", r"F",
                            r"\lor", r"T",  r"\lor", r"T", r") \land (", r"F", r"\lor", r"F", r" \lor", r"T", r")").scale(0.8)
        phi_x4_in.to_edge(UP)
        phi_x4_in[1].set_color(YELLOW)
        phi_x4_in[3].set_color(YELLOW)
        phi_x4_in[5].set_color(YELLOW)
        phi_x4_in[7].set_color(YELLOW)
        phi_x4_in[9].set_color(YELLOW)
        phi_x4_in[11].set_color(YELLOW)
        phi_x4_in[13].set_color(YELLOW)
        phi_x4_in[15].set_color(YELLOW)
        phi_x4_in[17].set_color(YELLOW)
        self.play(Transform(threeSATeq, phi_x4_in))
        self.wait(1)

        self.play(
            threeSATeq[3].animate.scale(2).set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
            threeSATeq[9].animate.scale(2).set_color(ORANGE),
            threeSATeq[17].animate.scale(2).set_color(PURPLE),
        )
        self.wait(1)
        self.play(
            line_c_1_2.animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
            line_c_2_2.animate.set_color(ORANGE),
            line_c_3_3.animate.set_color(PURPLE),
        )
        self.wait(2)

        self.play(
            Transform(threeSATeq, threeSATeq_copy),
            FadeOut(group_vals),
            line_x_1_1.animate.set_color(WHITE),
            line_x_2_2.animate.set_color(WHITE),
            line_x_3_1.animate.set_color(WHITE),
            line_x_4_1.animate.set_color(WHITE),
            line_c_1_2.animate.set_color(WHITE),
            line_c_2_2.animate.set_color(WHITE),
            line_c_3_3.animate.set_color(WHITE),
            FadeOut(surr_box)
        )

        self.wait(3)
        # now do the movement thingy ughem
        self.play(
            FadeOut(line_x_1_1),
            FadeOut(line_x_1_2),
            FadeOut(line_x_2_1),
            FadeOut(line_x_2_2),
            FadeOut(line_x_3_1),
            FadeOut(line_x_3_2),
            FadeOut(line_x_4_1),
            FadeOut(line_x_4_2),
            FadeOut(line_c_1_1),
            FadeOut(line_c_1_2),
            FadeOut(line_c_1_3),
            FadeOut(line_c_2_1),
            FadeOut(line_c_2_2),
            FadeOut(line_c_2_3),
            FadeOut(line_c_3_1),
            FadeOut(line_c_3_2),
            FadeOut(line_c_3_3),
        )
        self.wait(1)
        # self.play(
        #     clause_1_group[0].animate.shift(UP*0.5 + LEFT*5.5),
        #     clause_1_group[1].animate.shift(UP*0.5 + LEFT*5.5),
        #     clause_1_group[2].animate.shift(LEFT*5.5),
        #     clause_1_group[3].animate.shift(LEFT*5.5),
            
        # )

        self.play(
            clause_1_copy[0:3].animate.shift(UP*0.5 + LEFT*5.5),
            clause_1_copy[3:].animate.shift(LEFT*5.5 + DOWN*0.2),
            clause_2_copy[0:3].animate.shift(UP*0.5 + LEFT*5),
            clause_2_copy[3:].animate.shift(LEFT*5 + DOWN*0.2),
            clause_3_copy[0:3].animate.shift(UP*0.5 + LEFT*4.5),
            clause_3_copy[3:].animate.shift(LEFT*4.5 +DOWN*0.2),
            x_1_copy[2].animate.shift(RIGHT*4),
            x_1_copy[3].animate.shift(RIGHT*4),
            x_2_copy[2].animate.shift(RIGHT*4),
            x_2_copy[3].animate.shift(RIGHT*4),
            x_3_copy[2].animate.shift(RIGHT*4),
            x_3_copy[3].animate.shift(RIGHT*4),
            x_4_copy[2].animate.shift(RIGHT*4),
            x_4_copy[3].animate.shift(RIGHT*4),
        )
        
        line_c_1_1 = Line(clause_1_copy[2].get_left(), clause_1_copy[4].get_left())
        line_c_1_2 = Line(clause_1_copy[2].get_bottom(), clause_1_copy[4].get_top())
        line_c_1_3 = Line(clause_1_copy[2].get_right(), clause_1_copy[4].get_right())
        line_c_2_1 = Line(clause_2_copy[2].get_left(), clause_2_copy[4].get_left())
        line_c_2_2 = Line(clause_2_copy[2].get_bottom(), clause_2_copy[4].get_top())
        line_c_2_3 = Line(clause_2_copy[2].get_right(), clause_2_copy[4].get_right())
        line_c_3_1 = Line(clause_3_copy[2].get_left(), clause_3_copy[5].get_left())
        line_c_3_2 = Line(clause_3_copy[2].get_bottom(), clause_3_copy[5].get_top())
        line_c_3_3 = Line(clause_3_copy[2].get_right(), clause_3_copy[5].get_right())

        line_x_1_1 = Line(x_1_copy[1].get_top(), x_1_copy[3].get_top())
        line_x_1_2 = Line(x_1_copy[1].get_bottom(), x_1_copy[3].get_bottom())
        line_x_2_1 = Line(x_2_copy[1].get_top(), x_2_copy[3].get_top())
        line_x_2_2 = Line(x_2_copy[1].get_bottom(), x_2_copy[3].get_bottom())
        line_x_3_1 = Line(x_3_copy[1].get_top(), x_3_copy[3].get_top())
        line_x_3_2 = Line(x_3_copy[1].get_bottom(), x_3_copy[3].get_bottom())
        line_x_4_1 = Line(x_4_copy[1].get_top(), x_4_copy[3].get_top())
        line_x_4_2 = Line(x_4_copy[1].get_bottom(), x_4_copy[3].get_bottom())

        self.play(
            Write(line_c_1_1),
            Write(line_c_1_2),
            Write(line_c_1_3),
            Write(line_c_2_1),
            Write(line_c_2_2),
            Write(line_c_2_3),
            Write(line_c_3_1),
            Write(line_c_3_2),
            Write(line_c_3_3),
            Write(line_x_1_1),
            Write(line_x_1_2),
            Write(line_x_2_1),
            Write(line_x_2_2),
            Write(line_x_3_1),
            Write(line_x_3_2),
            Write(line_x_4_1),
            Write(line_x_4_2),

        )
        self.wait(2)

        self.graph_group = VGroup(clause_1_copy, clause_2_copy, clause_3_copy, x_1_copy, x_2_copy, x_3_copy, x_4_copy,
                            line_c_1_1, line_c_1_2, line_c_1_3, line_c_2_1, line_c_2_2, line_c_2_3, line_c_3_1, line_c_3_2, line_c_3_3,
                            line_x_1_1, line_x_1_2, line_x_2_1, line_x_2_2, line_x_3_1, line_x_3_2, line_x_4_1, line_x_4_2)
        # self.play(self.graph_group.animate.shift(UP*2.5))

        self.play(threeSATeq[1].animate.set_color(YELLOW))
        self.wait(1)
        self.play(
            self.graph_group[0][0:3].animate.set_color(YELLOW),
            self.graph_group[3][0:2].animate.set_color(YELLOW)
        )
        self.wait(1)

        # zoom camera
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(x_1_copy[1].get_center() + RIGHT*1.5)
        frame.set_color(RED)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(LEFT + DOWN*2)
        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)
        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display).set_fill(opacity=0))
        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        self.wait(2)

        self.play(Indicate(self.graph_group[7]))
        small_circle_n11 = Circle(color=WHITE).scale(0.1)
        small_circle_n11.set_fill(WHITE, opacity=1)
        line_x1_c1_int = line_intersection(([x_1_copy[1].get_bottom()[0],x_1_copy[1].get_bottom()[1], 0] , 
                                                [x_1_copy[3].get_bottom()[0],x_1_copy[3].get_bottom()[1], 0]), 
                                           ([clause_1_copy[2].get_left()[0], clause_1_copy[2].get_left()[1], 0], 
                                            [clause_1_copy[4].get_left()[0], clause_1_copy[4].get_left()[1], 0]))
        small_circle_n11.move_to(line_x1_c1_int)
        text_n111 = MathTex(r"n_{111}").scale(0.22)
        text_n111.set_color(BLACK)
        text_n111.move_to(small_circle_n11.get_center())
        self.play(Write(small_circle_n11), Write(text_n111))

        self.wait(1)

        # move the camera down
        self.play(frame.animate.shift(DOWN*1.2),
                  threeSATeq[1].animate.set_color(WHITE),
                  self.graph_group[0][0:3].animate.set_color(WHITE),
                    self.graph_group[3][0:2].animate.set_color(WHITE))
        self.wait(1)
        self.play(threeSATeq[3].animate.set_color(YELLOW))
        self.play(self.graph_group[0][0:3].animate.set_color(YELLOW),
                    self.graph_group[4][0:2].animate.set_color(YELLOW))
        
        self.play(Indicate(self.graph_group[8]))
        small_circle_n120 = Circle(color=WHITE).scale(0.1)
        small_circle_n120.set_fill(WHITE, opacity=1)
        line_x2_c1_int = line_intersection(([x_2_copy[1].get_top()[0],x_2_copy[1].get_top()[1], 0] , 
                                                [x_2_copy[3].get_top()[0],x_2_copy[3].get_top()[1], 0]), 
                                           ([clause_1_copy[2].get_bottom()[0], clause_1_copy[2].get_bottom()[1], 0], 
                                            [clause_1_copy[4].get_top()[0], clause_1_copy[4].get_top()[1], 0]))
        small_circle_n120.move_to(line_x2_c1_int)
        text_n120 = MathTex(r"n_{120}").scale(0.22)
        text_n120.set_color(BLACK)
        text_n120.move_to(small_circle_n120.get_center())
        self.play(Write(small_circle_n120), Write(text_n120))

        self.wait(1)

        # move the camera down
        self.play(frame.animate.shift(DOWN*1.2),
                  threeSATeq[3].animate.set_color(WHITE),
                  self.graph_group[0][0:3].animate.set_color(WHITE),
                    self.graph_group[4][0:2].animate.set_color(WHITE))
        self.wait(1)
        self.play(threeSATeq[5].animate.set_color(YELLOW))
        self.play(self.graph_group[0][0:3].animate.set_color(YELLOW),
                    self.graph_group[5][0:2].animate.set_color(YELLOW))
        
        self.play(Indicate(self.graph_group[9]))
        small_circle_n131 = Circle(color=WHITE).scale(0.1)
        small_circle_n131.set_fill(WHITE, opacity=1)
        line_x3_c1_int = line_intersection(([x_3_copy[1].get_bottom()[0],x_3_copy[1].get_bottom()[1], 0] , 
                                                [x_3_copy[3].get_bottom()[0],x_3_copy[3].get_bottom()[1], 0]), 
                                           ([clause_1_copy[2].get_right()[0], clause_1_copy[2].get_right()[1], 0], 
                                            [clause_1_copy[4].get_right()[0], clause_1_copy[4].get_right()[1], 0]))
        small_circle_n131.move_to(line_x3_c1_int)
        text_n131 = MathTex(r"n_{131}").scale(0.22)
        text_n131.set_color(BLACK)
        text_n131.move_to(small_circle_n131.get_center())
        self.play(Write(small_circle_n131), Write(text_n131))

        self.wait(1)

        self.play(FadeOut(frame), FadeOut(zoomed_display), FadeOut(zoomed_display_frame), FadeOut(zd_rect),
                  threeSATeq[5].animate.set_color(WHITE),
                  self.graph_group[0][0:3].animate.set_color(WHITE),
                    self.graph_group[5][0:2].animate.set_color(WHITE))

        small_circle_n210 = Circle(color=WHITE).scale(0.1)
        small_circle_n210.set_fill(WHITE, opacity=1)
        line_x1_c2_int = line_intersection(([x_1_copy[1].get_top()[0],x_1_copy[1].get_top()[1], 0] , 
                                                [x_1_copy[3].get_top()[0],x_1_copy[3].get_top()[1], 0]), 
                                           ([clause_2_copy[2].get_left()[0], clause_2_copy[2].get_left()[1], 0], 
                                            [clause_2_copy[4].get_left()[0], clause_2_copy[4].get_left()[1], 0]))
        small_circle_n210.move_to(line_x1_c2_int)
        text_n210 = MathTex(r"n_{210}").scale(0.22)
        text_n210.set_color(BLACK)
        text_n210.move_to(small_circle_n210.get_center())

        small_circle_n231 = Circle(color=WHITE).scale(0.1)
        small_circle_n231.set_fill(WHITE, opacity=1)
        line_x2_c2_int = line_intersection(([x_3_copy[1].get_bottom()[0],x_3_copy[1].get_bottom()[1], 0] , 
                                                [x_3_copy[3].get_bottom()[0],x_3_copy[3].get_bottom()[1], 0]), 
                                           ([clause_2_copy[2].get_bottom()[0], clause_2_copy[2].get_bottom()[1], 0], 
                                            [clause_2_copy[4].get_top()[0], clause_2_copy[4].get_top()[1], 0]))
        small_circle_n231.move_to(line_x2_c2_int)
        text_n221 = MathTex(r"n_{231}").scale(0.22)
        text_n221.set_color(BLACK)
        text_n221.move_to(small_circle_n231.get_center())

        small_circle_n241 = Circle(color=WHITE).scale(0.1)
        small_circle_n241.set_fill(WHITE, opacity=1)
        line_x2_c2_int = line_intersection(([x_4_copy[1].get_bottom()[0],x_4_copy[1].get_bottom()[1], 0] , 
                                                [x_4_copy[3].get_bottom()[0],x_4_copy[3].get_bottom()[1], 0]), 
                                           ([clause_2_copy[2].get_right()[0], clause_2_copy[2].get_right()[1], 0], 
                                            [clause_2_copy[4].get_right()[0], clause_2_copy[4].get_right()[1], 0]))
        small_circle_n241.move_to(line_x2_c2_int)
        text_n241 = MathTex(r"n_{241}").scale(0.22)
        text_n241.set_color(BLACK)
        text_n241.move_to(small_circle_n241.get_center())

        small_circle_321 = Circle(color=WHITE).scale(0.1)
        small_circle_321.set_fill(WHITE, opacity=1)
        line_x3_c2_int = line_intersection(([x_2_copy[1].get_bottom()[0],x_2_copy[1].get_bottom()[1], 0] , 
                                                [x_2_copy[3].get_bottom()[0],x_2_copy[3].get_bottom()[1], 0]), 
                                           ([clause_3_copy[2].get_left()[0], clause_3_copy[2].get_left()[1], 0], 
                                            [clause_3_copy[5].get_left()[0], clause_3_copy[5].get_left()[1], 0]))
        small_circle_321.move_to(line_x3_c2_int)
        text_321 = MathTex(r"n_{321}").scale(0.22)
        text_321.set_color(BLACK)
        text_321.move_to(small_circle_321.get_center())

        small_circle_330 = Circle(color=WHITE).scale(0.1)
        small_circle_330.set_fill(WHITE, opacity=1)
        line_x3_c2_int = line_intersection(([x_3_copy[1].get_top()[0],x_3_copy[1].get_top()[1], 0] , 
                                                [x_3_copy[3].get_top()[0],x_3_copy[3].get_top()[1], 0]), 
                                           ([clause_3_copy[2].get_bottom()[0], clause_3_copy[2].get_bottom()[1], 0], 
                                            [clause_3_copy[4].get_bottom()[0], clause_3_copy[4].get_bottom()[1], 0]))
        small_circle_330.move_to(line_x3_c2_int)
        text_330 = MathTex(r"n_{330}").scale(0.22)
        text_330.set_color(BLACK)
        text_330.move_to(small_circle_330.get_center())

        small_circle_341 = Circle(color=WHITE).scale(0.1)
        small_circle_341.set_fill(WHITE, opacity=1)
        line_x3_c2_int = line_intersection(([x_4_copy[1].get_bottom()[0],x_4_copy[1].get_bottom()[1], 0] , 
                                                [x_4_copy[3].get_bottom()[0],x_4_copy[3].get_bottom()[1], 0]), 
                                           ([clause_3_copy[2].get_right()[0], clause_3_copy[2].get_right()[1], 0], 
                                            [clause_3_copy[5].get_right()[0], clause_3_copy[5].get_right()[1], 0]))
        small_circle_341.move_to(line_x3_c2_int)
        text_341 = MathTex(r"n_{341}").scale(0.22)
        text_341.set_color(BLACK)
        text_341.move_to(small_circle_341.get_center())

        #write everything
        self.play(Write(small_circle_n210), Write(text_n210),
                    Write(small_circle_n231), Write(text_n221),
                    Write(small_circle_n241), Write(text_n241),
                    Write(small_circle_321), Write(text_321),
                    Write(small_circle_330), Write(text_330),
                    Write(small_circle_341), Write(text_341))

        f = open("locations.txt", "w")
        f.write(str(x_1_copy[1].get_center()) + "\n")
        f.write(str(x_1_copy[3].get_center()) + "\n")
        f.write(str(x_2_copy[1].get_center()) + "\n")
        f.write(str(x_2_copy[3].get_center()) + "\n")
        f.write(str(x_3_copy[1].get_center()) + "\n")
        f.write(str(x_3_copy[3].get_center()) + "\n")
        f.write(str(x_4_copy[1].get_center()) + "\n")
        f.write(str(x_4_copy[3].get_center()) + "\n")
        f.write(str(clause_1_copy[2].get_center()) + "\n")
        f.write(str(clause_1_copy[4].get_center()) + "\n")
        f.write(str(clause_2_copy[2].get_center()) + "\n")
        f.write(str(clause_2_copy[4].get_center()) + "\n")
        f.write(str(clause_3_copy[2].get_center()) + "\n")
        f.write(str(clause_3_copy[4].get_center()) + "\n")
        f.write(str(clause_3_copy[5].get_center()) + "\n")
        f.write(str(small_circle_n11.get_center()) + "\n")
        f.write(str(small_circle_n120.get_center()) + "\n")
        f.write(str(small_circle_n131.get_center()) + "\n")
        f.write(str(small_circle_n210.get_center()) + "\n")
        f.write(str(small_circle_n231.get_center()) + "\n")
        f.write(str(small_circle_n241.get_center()) + "\n")
        f.write(str(small_circle_321.get_center()) + "\n")
        f.write(str(small_circle_330.get_center()) + "\n")
        f.write(str(small_circle_341.get_center()) + "\n")
        f.close()
        
        self.wait(3)

