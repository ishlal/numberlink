

from manim import *
from colour import Color 

class conclusionp2(Scene):
    def construct(self):
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(64)]
        ).arrange_in_grid(8, 8, buff=0)
         
        red_circ = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        red_circ_copy = red_circ.copy()
        red_circ.move_to(squares[12].get_center())
        red_circ_copy.move_to(squares[16].get_center())

        blue_circ = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        blue_circ.move_to(squares[8].get_center())
        blue_circ_copy = blue_circ.copy()
        blue_circ_copy.move_to(squares[33].get_center())

        green_circ = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        green_circ.move_to(squares[29].get_center())
        green_circ_copy = green_circ.copy()
        green_circ_copy.move_to(squares[44].get_center())

        yellow_circ = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        yellow_circ.move_to(squares[13].get_center())
        yellow_circ_copy = yellow_circ.copy()
        yellow_circ_copy.move_to(squares[57].get_center())

        orange_circ = Circle(color=Color(hue=0.1, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        orange_circ.move_to(squares[21].get_center())
        orange_circ_copy = orange_circ.copy()
        orange_circ_copy.move_to(squares[36].get_center())

        cyan_circ = Circle(color=Color(hue=0.5, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        cyan_circ.move_to(squares[18].get_center())
        cyan_circ_copy = cyan_circ.copy()
        cyan_circ_copy.move_to(squares[35].get_center())

        game_group = VGroup(
            squares, red_circ, red_circ_copy, blue_circ, blue_circ_copy, green_circ, green_circ_copy, yellow_circ, yellow_circ_copy, orange_circ, orange_circ_copy, cyan_circ, cyan_circ_copy
        )
        self.play(Write(game_group), run_time=1)
        self.wait(1)

        path = VMobject()
        dot = Dot()
        dot.set_color(Color(hue=0, saturation=1, luminance=0.5))
        dot.move_to(red_circ_copy).get_center()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        path.set_color(Color(hue=0, saturation=1, luminance=0.5))
        path.stroke_width = 20
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        # self.play(dot.animate.move_to(squares[59].get_center()), run_time=0.5)
        # self.play(dot.animate.move_to(squares[58].get_center()), run_time=0.5)
        # self.play(dot.animate.move_to(squares[57].get_center()), run_time=0.5)
        # self.play(dot.animate.move_to(squares[56].get_center()), run_time=0.5)
        red_path_squares = [17, 25, 26, 27, 28, 20, 12]
        blue_attempt_1 = [9, 17, 25]
        blue_attempt_2 = [9, 10, 11, 19, 27]
        blue_attempt_3 = [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 50, 42, 34, 33]
        yellow_attempt_1 = [56, 48, 40, 32, 24, 25]
        red_correctish = [17, 9, 10, 11, 12]
        yellow_continue = [26, 34]
        blue_correct = [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 50, 49, 41, 33]
        yellow_continue_2 = [42, 43, 51, 52, 53, 54, 46, 38, 30, 22, 14, 13]
        cyan_correc = [19, 27, 35]
        orange_correct = [20, 28, 36]
        green_correct = [37, 45, 44]

        for i in range(len(red_path_squares)):
            self.play(dot.animate.move_to(squares[red_path_squares[i]].get_center()), run_time=0.1)
        self.wait(0.5)
        dot2 = Dot()
        dot2.set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        dot2.move_to(blue_circ.get_center())
        path2 = VMobject()
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        path2.set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        path2.stroke_width = 20
        def update_path2(path2):
            previous_path2 = path2.copy()
            previous_path2.add_points_as_corners([dot2.get_center()])
            path2.become(previous_path2)
        path2.add_updater(update_path2)
        self.add(path2, dot2)
        for i in range(len(blue_attempt_1)):
            self.play(dot2.animate.move_to(squares[blue_attempt_1[i]].get_center()), run_time=0.1)
        self.wait(0.5)
        self.play(FadeOut(path2), FadeOut(dot2))
        
        dot2.move_to(blue_circ.get_center())
        path2 = VMobject()
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        path2.set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        path2.stroke_width = 20
        path2.add_updater(update_path2)
        self.add(path2, dot2)
        for i in range(len(blue_attempt_2)):
            self.play(dot2.animate.move_to(squares[blue_attempt_2[i]].get_center()), run_time=0.1)
        self.play(FadeOut(path2), FadeOut(dot2))

        dot2.move_to(blue_circ.get_center())
        path2 = VMobject()
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        path2.set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        path2.stroke_width = 20
        path2.add_updater(update_path2)
        self.add(path2, dot2)
        for i in range(len(blue_attempt_3)):
            self.play(dot2.animate.move_to(squares[blue_attempt_3[i]].get_center()), run_time=0.05)
        self.wait(0.5)

        dot3 = Dot()
        dot3.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        dot3.move_to(yellow_circ_copy.get_center())
        path3 = VMobject()
        path3.set_points_as_corners([dot3.get_center(), dot3.get_center()])
        path3.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        path3.stroke_width = 20
        def update_path3(path3):
            previous_path3 = path3.copy()
            previous_path3.add_points_as_corners([dot3.get_center()])
            path3.become(previous_path3)
        path3.add_updater(update_path3)
        self.add(path3, dot3)
        for i in range(len(yellow_attempt_1)):
            self.play(dot3.animate.move_to(squares[yellow_attempt_1[i]].get_center()), run_time=0.1)
        # self.play(FadeOut(path3), FadeOut(dot3))

        self.wait(0.5)
        self.play(FadeOut(path), FadeOut(dot))

        dot.move_to(red_circ_copy.get_center())
        path = VMobject()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        path.set_color(Color(hue=0, saturation=1, luminance=0.5))
        path.stroke_width = 20
        path.add_updater(update_path)
        self.add(path, dot)
        for i in range(len(red_correctish)):
            self.play(dot.animate.move_to(squares[red_correctish[i]].get_center()), run_time=0.1)
        
        self.wait(0.2)

        for i in range(len(yellow_continue)):
            self.play(dot3.animate.move_to(squares[yellow_continue[i]].get_center()), run_time=0.1)
        self.wait(0.3)

        self.play(FadeOut(path2), FadeOut(dot2))
        dot2.move_to(blue_circ.get_center())
        path2 = VMobject()
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        path2.set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        path2.stroke_width = 20
        path2.add_updater(update_path2)
        self.add(path2, dot2)
        for i in range(len(blue_correct)):
            self.play(dot2.animate.move_to(squares[blue_correct[i]].get_center()), run_time=0.05)
        self.wait(0.5)

        for i in range(len(yellow_continue_2)):
            self.play(dot3.animate.move_to(squares[yellow_continue_2[i]].get_center()), run_time=0.1)
        self.wait(0.5)

        dot4 = Dot()
        dot4.set_color(Color(hue=0.5, saturation=1, luminance=0.5))
        dot4.move_to(cyan_circ.get_center())
        path4 = VMobject()
        path4.set_points_as_corners([dot4.get_center(), dot4.get_center()])
        path4.set_color(Color(hue=0.5, saturation=1, luminance=0.5))
        path4.stroke_width = 20
        def update_path4(path4):
            previous_path4 = path4.copy()
            previous_path4.add_points_as_corners([dot4.get_center()])
            path4.become(previous_path4)
        path4.add_updater(update_path4)
        self.add(path4, dot4)
        for i in range(len(cyan_correc)):
            self.play(dot4.animate.move_to(squares[cyan_correc[i]].get_center()), run_time=0.1)

        self.wait(0.5)

        dot5 = Dot()
        dot5.set_color(Color(hue=0.1, saturation=1, luminance=0.5))
        dot5.move_to(orange_circ.get_center())
        path5 = VMobject()
        path5.set_points_as_corners([dot5.get_center(), dot5.get_center()])
        path5.set_color(Color(hue=0.1, saturation=1, luminance=0.5))
        path5.stroke_width = 20
        def update_path5(path5):
            previous_path5 = path5.copy()
            previous_path5.add_points_as_corners([dot5.get_center()])
            path5.become(previous_path5)
        path5.add_updater(update_path5)
        self.add(path5, dot5)
        for i in range(len(orange_correct)):
            self.play(dot5.animate.move_to(squares[orange_correct[i]].get_center()), run_time=0.1)
        
        self.wait(0.5)

        dot6 = Dot()
        dot6.set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        dot6.move_to(green_circ.get_center())
        path6 = VMobject()
        path6.set_points_as_corners([dot6.get_center(), dot6.get_center()])
        path6.set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        path6.stroke_width = 20
        def update_path6(path6):
            previous_path6 = path6.copy()
            previous_path6.add_points_as_corners([dot6.get_center()])
            path6.become(previous_path6)
        path6.add_updater(update_path6)
        self.add(path6, dot6)
        for i in range(len(green_correct)):
            self.play(dot6.animate.move_to(squares[green_correct[i]].get_center()), run_time=0.1)


        self.wait(2)

    