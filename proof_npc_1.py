

from manim import *
from colour import Color

class proof_npc_1(Scene):
    def construct(self):
        text_show_np_complete = Text("To prove NP-Complete: ").scale(0.8)
        # text_show_np_complete.shift(UP*2.5 + LEFT*3)
        text_show_np_complete.to_edge(UP)
        text_step_1 = Text("1. Show that it is in NP").scale(0.6)
        text_step_1.next_to(text_show_np_complete, DOWN)
        text_step_1.shift(LEFT*0.5)
        text_step_2 = Text("2. Perform reduction from existing \n\tNP Complete problem").scale(0.6)
        text_step_2.next_to(text_step_1, DOWN)
        text_step_2.shift(RIGHT*0.8)
        self.play(Write(text_show_np_complete), Write(text_step_1), Write(text_step_2), run_time=1)
        self.wait(2)
        self.play(text_step_2.animate.set_color(YELLOW))
        self.wait(1)
        text_2_expanded = Text("2. Perform reduction from existing NP Complete problem").scale(0.6).set_color(YELLOW)
        text_2_expanded.to_edge(UP)
        self.play(FadeOut(text_show_np_complete), FadeOut(text_step_1), Transform(text_step_2, text_2_expanded))
        self.wait(1)
        text_reduction = Text("REDUCTION: A transformation from one problem to another").scale(0.6)
        text_reduction.next_to(text_step_2, DOWN)
        self.play(Write(text_reduction))
        self.wait(1)

        big_letter_A = Text("Problem A").scale(1.2)
        big_letter_A.shift(LEFT*3.5+DOWN*0.2)
        big_letter_B = Text("Problem B").scale(1.2)
        big_letter_B.shift(RIGHT*3.5+DOWN*0.2)
        circle_A = Circle(color=BLUE, fill_opacity=0.5).scale(0.75)
        circle_A.set_fill(BLUE, opacity=0.5)
        text_A = Text("A").scale(0.7)
        circle_A.add(text_A)
        text_B = Text("B").scale(0.7)
        circle_B = Circle(color=ORANGE, fill_opacity=0.5).scale(0.75)
        circle_B.set_fill(ORANGE, opacity=0.5)
        circle_B.add(text_B)
        circle_A.next_to(big_letter_A, DOWN)
        circle_B.next_to(big_letter_B, DOWN)
        self.play(Write(big_letter_A), Write(big_letter_B), Write(circle_A), Write(circle_B))
        self.wait(1)
        curved_arrow = CurvedArrow(big_letter_A.get_center() + UP*0.3, big_letter_B.get_center()+UP*0.3, angle=-TAU/6)
        self.play(Write(curved_arrow))  
        self.wait(1)
        text_manipulate = Text("Manipulate A to \nlook like B").scale(0.6)
        text_manipulate.next_to(curved_arrow, UP)
        surr_box_text_manipulate = SurroundingRectangle(text_manipulate, color=WHITE)
        self.play(Write(text_manipulate), Write(surr_box_text_manipulate))
        self.wait(2)
        self.play(circle_A.animate.set_color(GREEN))
        self.wait(1)
        self.play(circle_B.animate.set_color(GREEN))
        self.wait(2)
        self.play(circle_A.animate.set_color(RED))
        self.wait(1)
        self.play(circle_B.animate.set_color(RED))
        self.wait(2)
        text_polynomial_reduction = Text("Polynomial Reduction").scale(0.6)
        text_polynomial_reduction.move_to(text_manipulate.get_center())
        surr_box_poly = SurroundingRectangle(text_polynomial_reduction, color=WHITE)
        self.play(Transform(text_manipulate, text_polynomial_reduction), Transform(surr_box_text_manipulate, surr_box_poly))
        self.wait(2)

        text_3SAT = MathTex("3SAT").scale(1.2)
        text_Flow = Text("Flow").scale(1.2)
        text_3SAT.move_to(big_letter_A.get_center())
        text_Flow.move_to(big_letter_B.get_center())
        threeSATeq = MathTex(r"\varphi = (x_1 \lor \overline{x_2} \lor x_3) \\ \land (\overline{x_1} \lor x_3 \lor x_4) \\ \land (x_2 \lor \overline{x_3} \lor x_4)")
        threeSATeq.scale(1)
        threeSATeq.move_to(circle_A.get_center())
        threeSATeq.shift(DOWN*0.5)
        flow_board = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.25) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)


        circles = VGroup(
            *[VGroup(Circle(color=WHITE,
                     fill_opacity=1).scale(0.15),
                     Text(str(j+1)).scale(0.5).set_color(BLACK)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.7)
        circles.shift(RIGHT*3 + UP*1.2)
        # self.play(Write(circles), run_time=1)

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
        # self.bring_to_front(circles)
        # self.bring_to_back(edges)
        flow_board = VGroup(circles, edges)

        flow_board.move_to(circle_B.get_center())
        flow_board.scale(0.6)
        flow_board.shift(DOWN*0.5)

        circles[5][0].set_color(Color(hue=0, saturation=1, luminance=0.5))
        circles[22][0].set_color(Color(hue=0, saturation=1, luminance=0.5))
        circles[6][0].set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        circles[8][0].set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        circles[13][0].set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        circles[15][0].set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        circles[18][0].set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        circles[20][0].set_color(Color(hue=0.15, saturation=1, luminance=0.5))


        # red_circ = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.2)
        # red_circ.move_to(flow_board[10].get_center())
        # red_circ_copy = red_circ.copy()
        # red_circ_copy.move_to(flow_board[18].get_center())
        # blue_circ = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.2)
        # blue_circ.move_to(flow_board[5].get_center())
        # blue_circ_copy = blue_circ.copy()
        # blue_circ_copy.move_to(flow_board[16].get_center())
        # green_circ = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.2)
        # green_circ.move_to(flow_board[6].get_center())
        # green_circ_copy = green_circ.copy()
        # green_circ_copy.move_to(flow_board[8].get_center())
        # yellow_circ = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.2)
        # yellow_circ.move_to(flow_board[19].get_center())
        # yellow_circ_copy = yellow_circ.copy()
        # yellow_circ_copy.move_to(flow_board[23].get_center())
        # flow_board_group = VGroup(flow_board, red_circ, blue_circ, green_circ, yellow_circ, red_circ_copy, blue_circ_copy, green_circ_copy, yellow_circ_copy)
        self.play(Transform(big_letter_A, text_3SAT), Transform(big_letter_B, text_Flow), Transform(circle_A, threeSATeq), Transform(circle_B, flow_board))
        self.bring_to_front(flow_board[0])
    
        self.wait(2)
        text_npcomp = MathTex(r"\in \text{NP-Complete}").scale(0.8)
        text_npcomp.next_to(text_3SAT, RIGHT)
        self.play(Write(text_npcomp))
        self.wait(2)
        self.play(FadeOut(text_npcomp), FadeOut(text_Flow), FadeOut(flow_board),
                  FadeOut(text_reduction), FadeOut(surr_box_text_manipulate), FadeOut(text_manipulate), 
                  FadeOut(curved_arrow), FadeOut(big_letter_B), 
                  FadeOut(circle_B), FadeOut(text_step_2))
        self.wait(1)
        