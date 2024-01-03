

from manim import *
from colour import Color

class proof_npc_2(Scene):
    def construct(self):
        text_3SAT = MathTex(r"3", r"SAT").scale(1.2)
        text_3SAT.shift(LEFT*3.5+DOWN*0.2)
        threeSATeq = MathTex(r"\varphi = (x_1 \lor \overline{x_2} \lor x_3) \\ \land (\overline{x_1} \lor x_3 \lor x_4) \\ \land (x_2 \lor \overline{x_3} \lor x_4)")
        threeSATeq.scale(1)
        threeSATeq.next_to(text_3SAT, DOWN)
        threeSATeq.shift(DOWN*0.5)
        self.add(threeSATeq, text_3SAT)
        self.wait(1)
        threeSATeq_expanded = MathTex(r"\varphi = ",r"(", r"x_1", r"\lor",  r"\overline{x_2}", r"\lor", r"x_3", r")", r"\land", r"(\overline{x_1} \lor x_3 \lor x_4)", r"\land",  r"(x_2 \lor \overline{x_3} \lor x_4)")
        threeSATeq_expanded.to_edge(UP)
        threeSATeq_expanded.shift(DOWN)
        text_3SAT_v2 = Text("3SAT").scale(1.2)
        text_3SAT_v2.to_edge(UP)
        self.play(Transform(threeSATeq, threeSATeq_expanded), text_3SAT.animate.move_to(text_3SAT_v2.get_center()))
        self.wait(1)
        threesat_q = MathTex(r"\text{Is there an assignment of } x_1, x_2, x_3, x_4 \text{ that makes } \varphi \text{ TRUE?}")
        threesat_q.scale(0.8)
        threesat_q.next_to(threeSATeq, DOWN)
        self.play(Write(threesat_q))
        # add a horizontal line below threesat_q
        line = Line(start=threesat_q.get_corner(DOWN+LEFT), end=threesat_q.get_corner(DOWN+RIGHT))
        self.play(Write(line))
        self.wait(1)

        definition_literal = MathTex(r"\text{Literal:}", r"\text{ Variable or negation of variable}").scale(0.8)
        definition_literal[0].set_color(BLUE)
        definition_literal.next_to(threesat_q, DOWN)
        definition_literal.shift(DOWN*0.2 + LEFT*1.2)
        self.play(Write(definition_literal))
        self.wait(1)
        literal_example = Text("Examples: ")
        literal_example.scale(0.6)
        literal_example.next_to(definition_literal, DOWN)
        literal_example.shift(LEFT)
        x_1_copy = threeSATeq_expanded[2].copy()
        self.play(Write(literal_example))
        self.play(x_1_copy.animate.move_to(literal_example.get_center() + RIGHT*1.5))
        self.play(x_1_copy.animate.set_color(BLUE))
        self.wait(1)
        x_2_copy = threeSATeq_expanded[4].copy()
        self.play(x_2_copy.animate.move_to(x_1_copy.get_center() + RIGHT))
        self.play(x_2_copy.animate.set_color(BLUE))
        self.wait(2)

        definition_clause = MathTex(r"\text{Clause:}", r"\text{ A set of }", r"\text{literals}", r"\text{ combined by logical }", r"\text{ORs}").scale(0.8)
        definition_clause[0].set_color(ORANGE)
        definition_clause[-1].set_color(YELLOW)
        definition_clause[2].set_color(BLUE)
        definition_clause.next_to(definition_literal, DOWN*3.5)
        definition_clause.shift(RIGHT*0.5)
        self.play(Write(definition_clause))
        self.wait(1)
        clause_example = Text("Example: ")
        clause_example.scale(0.6)
        clause_example.next_to(literal_example, DOWN*3.5)
        self.play(Write(clause_example))
        clause_ex = threeSATeq_expanded[2:7].copy()
        self.play(clause_ex.animate.move_to(clause_example.get_center() + RIGHT*2.5))
        self.play(clause_ex[0].animate.set_color(BLUE), 
                  clause_ex[1].animate.set_color(YELLOW),
                  clause_ex[2].animate.set_color(BLUE),
                  clause_ex[3].animate.set_color(YELLOW),
                  clause_ex[4].animate.set_color(BLUE))
        self.wait(2)

        text_cnf = MathTex(r"\text{CNF:}", r"\text{ Conjunctive Normal Form: }", r"\text{Clauses}", r"\text{ combined via logical }", r"\text{AND}").scale(0.8)
        text_cnf[0].set_color(GREEN)
        text_cnf[2].set_color(ORANGE)
        text_cnf[-1].set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        text_cnf.next_to(definition_clause, DOWN*3.5)
        text_cnf.shift(RIGHT)
        self.play(Write(text_cnf))
        self.wait(1)
        cnf_example = Text("Example: ")
        cnf_example.scale(0.6)
        cnf_example.next_to(clause_example, DOWN*3.5)
        cnf_example.shift(LEFT*2)
        self.play(Write(cnf_example))
        cnf_ex_top = threeSATeq_expanded[1:].copy()

        cnf_ex = MathTex(r"(x_1 \lor \overline{x_2} \lor x_3)", r"\land", r"(\overline{x_1} \lor x_3 \lor x_4)", r"\land", r"(x_2 \lor \overline{x_3} \lor x_4)").scale(0.8)
        cnf_ex.move_to(cnf_example.get_center() + RIGHT*5)
        self.play(Transform(cnf_ex_top, cnf_ex))
        self.play(cnf_ex[0].animate.set_color(ORANGE),
                  cnf_ex[1].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                  cnf_ex[2].animate.set_color(ORANGE),
                  cnf_ex[3].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
                  cnf_ex[4].animate.set_color(ORANGE))

        self.wait(2)

        text_3_copy = text_3SAT[0].copy()
        self.play(text_3_copy.animate.move_to(cnf_ex.get_center() + DOWN*0.5 + LEFT*6).set_color(Color(hue=0, saturation=1, luminance=0.5)).scale(0.8))
        text_explanation = MathTex(r"\text{: Each clause can have at most }", r"3", r"\text{ literals}").scale(0.8)
        text_explanation[1].set_color(Color(hue=0, saturation=1, luminance=0.5))
        text_explanation[2].set_color(BLUE)
        text_explanation.next_to(text_3_copy, RIGHT)
        self.play(Write(text_explanation))
        self.wait(1)
        self.play(
            FadeOut(definition_literal), FadeOut(literal_example), 
            FadeOut(clause_example), FadeOut(text_cnf), 
            FadeOut(cnf_example), FadeOut(text_3_copy), 
            FadeOut(text_explanation), 
              FadeOut(definition_clause), 
              FadeOut(text_3SAT_v2), FadeOut(cnf_ex_top),
              FadeOut(x_1_copy), FadeOut(x_2_copy),
              FadeOut(clause_ex), FadeOut(cnf_ex)
        )
        self.wait(3)

