

from manim import *
from colour import Color

class proof_npc_4(Scene):
    def construct(self):
        text_3SAT = MathTex(r"3", r"SAT").scale(1.2).to_edge(UP)
        threeSATeq_expanded = MathTex(r"\varphi = ",r"(", r"x_1", r"\lor",  r"\overline{x_2}", r"\lor", r"x_3", r")", r"\land", r"(\overline{x_1} \lor x_3 \lor x_4)", r"\land",  r"(x_2 \lor \overline{x_3} \lor x_4)")
        threeSATeq_expanded.to_edge(UP)
        threeSATeq_expanded.shift(DOWN)
        threesat_q = MathTex(r"\text{Is there an assignment of } x_1, x_2, x_3, x_4 \text{ that makes } \varphi \text{ TRUE?}")
        threesat_q.scale(0.8)
        threesat_q.next_to(threeSATeq_expanded, DOWN)
        # add a horizontal line below threesat_q
        line = Line(start=threesat_q.get_corner(DOWN+LEFT), end=threesat_q.get_corner(DOWN+RIGHT))
        self.add(text_3SAT, threeSATeq_expanded, threesat_q, line)

        squares = VGroup(
            *[VGroup(Rectangle(width=3, height=1.3, color=WHITE),
                     fill_opacity=0.5) for j in range(9)]
        ).arrange_in_grid(3, 3, buff=0)
        squares[0].set_stroke(width=15)
        squares[1].set_stroke(width=15)
        squares[2].set_stroke(width=15)
        squares[3].set_stroke(width=15)
        squares[6].set_stroke(width=15)

        squares.shift(DOWN)
        self.add(squares)

        land_copy = threeSATeq_expanded[8].copy()
        self.play(land_copy.animate.move_to(squares[0].get_center()).scale(2))
        self.wait(1)


        text_true = Text("TRUE").scale(1.1).set_color(GREEN)
        text_false = Text("FALSE").scale(1.1).set_color(RED)
        text_true.move_to(squares[1].get_center())
        text_false.move_to(squares[2].get_center())
        text_true_copy = text_true.copy()
        text_false_copy = text_false.copy()
        text_true_copy.move_to(squares[3].get_center())
        text_false_copy.move_to(squares[6].get_center())
        self.play(Write(text_true), Write(text_false), Write(text_true_copy), Write(text_false_copy))
        self.wait(1)
        true_11_top = text_true.copy()
        true_11_side = text_true_copy.copy()
        group_true_11 = VGroup(true_11_top, true_11_side)
        true_11 = Text("TRUE").scale(1.1).set_color(GREEN)
        true_11.move_to(squares[4].get_center())
        self.play(Transform(group_true_11, true_11))
        self.wait(0.3)
        true_12_top = text_false.copy()
        true_12_side = text_true_copy.copy()
        group_true_12 = VGroup(true_12_top, true_12_side)
        true_12 = Text("FALSE").scale(1.1).set_color(RED)
        true_12.move_to(squares[5].get_center())
        self.play(Transform(group_true_12, true_12))
        self.wait(0.3)
        true_21_top = text_true.copy()
        true_21_side = text_false_copy.copy()
        group_true_21 = VGroup(true_21_top, true_21_side)
        true_21 = Text("FALSE").scale(1.1).set_color(RED)
        true_21.move_to(squares[7].get_center())
        self.play(Transform(group_true_21, true_21))
        self.wait(0.3)
        true_22_top = text_false.copy()
        true_22_side = text_false_copy.copy()
        group_true_22 = VGroup(true_22_top, true_22_side)
        true_22 = Text("FALSE").scale(1.1).set_color(RED)
        true_22.move_to(squares[8].get_center())
        self.play(Transform(group_true_22, true_22))
        self.wait(3)