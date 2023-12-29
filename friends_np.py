
from manim import *
from colour import Color

class friends_np(Scene):
    def construct(self):
        hues = [13, 4, 1, 10, 5, 6, 8, 12]
        squares = VGroup(
            *[VGroup(Square(color=Color(hue = hues[j]/8, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.75),
                     Text("Person " + str(hues[j])).scale(0.5)) for j in range(8)]
        ).arrange_in_grid(2, 4, buff=0.1).scale(0.7)
        # box = Rectangle(height=2.5, width=4.5, color=WHITE)
    
        squares.shift(LEFT*4.3)
        box = SurroundingRectangle(squares, buff=0.2)
        # box.move_to(squares.get_center())
        text_verify = Text("Verify: ").scale(0.7)
        text_verify.next_to(box, UP)
        self.play(Write(squares), Write(box), Write(text_verify), run_time=1)

        placement_grid = VGroup(
            *[VGroup(Rectangle(height=2, width=4, color=WHITE).scale(0.75),
                     fill_opacity=0.5).scale(0.75) for j in range(28)]
        ).arrange_in_grid(7, 4, buff=0.5).scale(0.7)

        placement_grid.shift(RIGHT*2.8)
        # self.play(Write(placement_grid), run_time=1)

        counter = 0
        for i in range(8):
            for j in range(i+1, 8):
                if i != j:
                    square_1_copy = squares[i].copy()
                    square_2_copy = squares[j].copy()
                    square_1_copy.move_to(squares[i].get_center())
                    square_2_copy.move_to(squares[j].get_center())
                    # group the two squares together
                    square_1_target = square_1_copy.copy()
                    square_1_target.scale(0.5)
                    square_1_target.move_to(placement_grid[counter].get_center() + LEFT*0.6)
                    square_2_target = square_2_copy.copy()
                    square_2_target.scale(0.5)
                    square_2_target.next_to(square_1_target, RIGHT*0.3)
                    check_mark = ImageMobject("images/check.png").scale(0.1)
                    check_mark.next_to(square_2_target, RIGHT*0.3)

                    # transform square_1_copy to square_1_target
                    # transform square_2_copy to square_2_target
                    self.play(Transform(square_1_copy, square_1_target),
                                Transform(square_2_copy, square_2_target),
                                FadeIn(check_mark),
                              run_time=0.2)
                    counter += 1

        self.wait(2)
        check_mark_2 = ImageMobject("images/check.png").scale(0.5)
        check_mark_2.move_to(box.get_center())
        self.play(FadeIn(check_mark_2))
        self.wait(1)
        # clear screen
        
