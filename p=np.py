
from manim import *
from colour import Color

class pnp(Scene):
    def construct(self):
        oval = Ellipse(width=2.5, height=3, color=GRAY)
        oval.set_fill(GRAY, opacity=0.5)
        oval.shift(UP*1)
        text_p = Text("P").scale(1.3)
        text_p.move_to(oval.get_center())
        self.play(Write(oval), Write(text_p), run_time=1)

        oval2 = Ellipse(width=9, height=4, color=GREEN)
        oval2.set_fill(GREEN, opacity=0.5)
        oval2.move_to(oval.get_center())
        oval2.shift([-1, 0, 0])
        oval2_center = oval2.get_center()
        self.bring_to_back(oval2)
        text_np = Text("NP").scale(1.3)
        text_np.move_to(oval2.get_center() + RIGHT*3.5)
        self.play(Write(oval2), Write(text_np), run_time=1)
        self.wait(1)

        

        self.play(Indicate(oval))
        self.wait(1)
        oval_2_copy = Ellipse(width=9, height = 4, color=GRAY)
        oval_2_copy.set_fill(GRAY, opacity=0.5)
        oval_2_copy.move_to(oval2.get_center())
        self.play(Transform(oval, oval_2_copy))
        self.wait(0.5)

        text_equals = Text("=").scale(1.3)
        text_equals.next_to(text_p, RIGHT*1.3)
        self.play(FadeIn(text_equals))

        self.wait(1)
        # transform oval back to original
        self.play(Transform(oval, Ellipse(width=2.5, height=3, color=GRAY).set_fill(GRAY, opacity=0.5).shift(UP*1)),
                  FadeOut(text_equals))
        self.wait(1)



        oval_3 = Ellipse(width=3, height=2, color=RED)
        oval_3.set_fill(RED, opacity=0.5)
        self.bring_to_front(oval_3)
        oval_3.move_to(oval.get_center() + LEFT * 3.8)
        text_np_complete = Text("NP-Complete").scale(0.45)
        text_np_complete.move_to(oval_3.get_center())
        oval_center = oval.get_center()
        

        # draw a star
        star = Star(color=YELLOW)
        star.set_fill(YELLOW, opacity=1)
        star.scale(0.15)
        # star.move_to(oval_3.get_center() + DOWN*0.4)
        star.next_to(text_np_complete, RIGHT)
        star_2 = Star(color=Color(hue=0.6, saturation=1, luminance=0.5))
        star_2.set_fill(Color(hue=0.6, saturation=1, luminance=0.5), opacity=1)
        star_2.scale(0.15)
        star_2.move_to(oval.get_center() + LEFT*0.7)
        self.play(Write(oval_3), Write(text_np_complete), Write(star), run_time=1)
        self.wait(1)
        oval_3_copy = Ellipse(width = 4.6, height = 2, color=RED)
        oval_3_copy.set_fill(RED, opacity=0.5)
        oval_3_copy.move_to(oval_3.get_center() + RIGHT*1.1)
        self.play(Transform(oval_3, oval_3_copy), star.animate.move_to(star_2.get_center()), run_time=0.5)
        # self.play(star.animate.move_to(star_2.get_center()),
        #            Transform(oval_3, oval_3_copy))
        self.wait(0.5)
        self.play(Indicate(star))
        self.play(Transform(oval, oval_2_copy))
        self.wait(0.5)
        self.play(FadeIn(text_equals))
        # transform oval back to original
        self.wait(1)
        self.play(Transform(oval, Ellipse(width=2.5, height=3, color=GRAY).set_fill(GRAY, opacity=0.5).shift(UP*1)),
                  Transform(oval_3, Ellipse(width=3, height=2, color=RED).set_fill(RED, opacity=0.5).move_to(oval_center + LEFT * 3.8)),
                  FadeOut(star), FadeOut(text_equals))
        self.wait(1)
        # transform red ellipse back to normal

        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        squares.shift(LEFT*5)
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

        game_group = VGroup(squares, red_circ, blue_circ, green_circ, yellow_circ,
                            red_circ_copy, blue_circ_copy, green_circ_copy, yellow_circ_copy)
        game_group.scale(0.7)
        game_group.shift(DOWN*2)
        game_group_copy = game_group.copy()
        # self.play(Write(game_group), run_time=1)

        star.next_to(text_np_complete, RIGHT)

        text_solution = Text("Is there a solution?").scale(0.8)
        text_solution.next_to(game_group, RIGHT)
        self.play(Write(game_group), Write(text_solution), run_time=1)
        text_np = MathTex(r"\in \text{NP-Complete}")
        text_np.next_to(text_solution, RIGHT)
        self.wait(1.3)
        self.play(Write(text_np))
        self.wait(2)
        self.play(FadeOut(text_np), FadeOut(text_solution), Transform(game_group, star))
        self.wait(0.5)

        text_show_np_complete = Text("To prove NP-Complete: ").scale(0.8)
        text_show_np_complete.next_to(game_group_copy, RIGHT)
        text_show_np_complete.shift(RIGHT + UP*0.6)
        self.play(Write(game_group_copy), FadeOut(game_group))
        self.play(Write(text_show_np_complete))
        text_step_1 = Text("1. Show that it is in NP").scale(0.6)
        text_step_1.next_to(text_show_np_complete, DOWN)
        self.play(Write(text_step_1))
        self.wait(1)
        star_new = Star(color=PURPLE)
        star_new.set_fill(PURPLE, opacity=1)
        star_new.scale(0.15)
        star_new.move_to(oval2.get_center() + DOWN + LEFT*1.2)
        game_group_copy_2 = game_group_copy.copy()
        self.play(Transform(game_group_copy_2, star_new))

        text_step_2 = Text("2. Perform reduction from existing \n\tNP Complete problem").scale(0.6)
        text_step_2.next_to(text_step_1, DOWN)
        self.play(Write(text_step_2))
        self.wait(1)

        another_star = Star(color=Color(hue=0.6, saturation=1, luminance=0.5))
        another_star.set_fill(Color(hue=0.6, saturation=1, luminance=0.5), opacity=1)
        another_star.scale(0.15)
        another_star.next_to(text_np_complete, RIGHT)
        self.play(FadeIn(another_star))
        # draw curvy arrow from another_star to star_new
        squig_arrow = CurvedArrow(start_point=another_star.get_center(), end_point=star_new.get_center(), angle=-TAU/4)
        # make arrow head smaller
        squig_arrow.tip_length = 0.02
        self.play(Write(squig_arrow))



        self.wait(2)