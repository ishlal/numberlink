from manim import *
from colour import Color

class Gameplay(Scene):
    def construct(self):
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(49)]
        ).arrange_in_grid(7, 7, buff=0)
        self.play(Write(squares), run_time=1)   
        self.wait(0.4)

        red_circ = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        red_circ_copy = red_circ.copy()
        red_circ.move_to(squares[0].get_center())
        red_circ_copy.move_to(squares[24].get_center())
        blue_circ = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        blue_circ.move_to(squares[7].get_center())
        blue_circ_copy = blue_circ.copy()
        blue_circ_copy.move_to(squares[44].get_center())
        green_circ = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        green_circ.move_to(squares[12].get_center())
        green_circ_copy = green_circ.copy()
        green_circ_copy.move_to(squares[29].get_center())
        yellow_circ = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        yellow_circ.move_to(squares[17].get_center())
        yellow_circ_copy = yellow_circ.copy()
        yellow_circ_copy.move_to(squares[45].get_center())
        orange_circ = Circle(color=Color(hue=0.05, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        orange_circ.move_to(squares[10].get_center())
        orange_circ_copy = orange_circ.copy()
        orange_circ_copy.move_to(squares[30].get_center())

        self.play(FadeIn(red_circ), FadeIn(red_circ_copy), 
                  FadeIn(blue_circ), FadeIn(blue_circ_copy),
                    FadeIn(green_circ), FadeIn(green_circ_copy),
                    FadeIn(yellow_circ), FadeIn(yellow_circ_copy),
                    FadeIn(orange_circ), FadeIn(orange_circ_copy), run_time=1)
        self.wait(0.8)

        path = VMobject()
        dot = Dot()
        dot.set_color(Color(hue=0, saturation=1, luminance=0.5))
        dot.move_to(red_circ.get_center())
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        path.set_color(Color(hue=0, saturation=1, luminance=0.5))
        path.stroke_width = 20
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(dot.animate.move_to(squares[1].get_center()), run_time=0.4)
        self.play(dot.animate.move_to(squares[22].get_center()), run_time=1.2)
        self.play(dot.animate.move_to(squares[24].get_center()), run_time=0.6)
        self.wait(1)
        path2 = VMobject()
        dot2 = Dot()
        dot2.set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        dot2.move_to(blue_circ.get_center())
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        path2.set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        path2.stroke_width = 20
        def update_path2(path2):
            previous_path2 = path2.copy()
            previous_path2.add_points_as_corners([dot2.get_center()])
            path2.become(previous_path2)
        path2.add_updater(update_path2)
        self.add(path2, dot2)
        self.play(dot2.animate.move_to(squares[42].get_center()), run_time=1.3)
        self.play(dot2.animate.move_to(squares[44].get_center()), run_time=0.7)
        self.wait(1)
        path3 = VMobject()
        dot3 = Dot()
        dot3.set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        dot3.move_to(green_circ.get_center())
        path3.set_points_as_corners([dot3.get_center(), dot3.get_center()])
        path3.set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        path3.stroke_width = 20
        def update_path3(path3):
            previous_path3 = path3.copy()
            previous_path3.add_points_as_corners([dot3.get_center()])
            path3.become(previous_path3)
        path3.add_updater(update_path3)
        self.add(path3, dot3)
        self.play(dot3.animate.move_to(squares[40].get_center()), run_time=1.2)
        self.play(dot3.animate.move_to(squares[36].get_center()), run_time=1.2)
        self.play(dot3.animate.move_to(squares[29].get_center()), run_time=0.3)
        self.wait(1)

        path4 = VMobject()
        dot4 = Dot()
        dot4.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        dot4.move_to(yellow_circ.get_center())
        path4.set_points_as_corners([dot4.get_center(), dot4.get_center()])
        path4.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        path4.stroke_width = 20
        def update_path4(path4):
            previous_path4 = path4.copy()
            previous_path4.add_points_as_corners([dot4.get_center()])
            path4.become(previous_path4)
        path4.add_updater(update_path4)
        self.add(path4, dot4)
        self.play(dot4.animate.move_to(squares[16].get_center()), run_time=0.3)
        self.play(dot4.animate.move_to(squares[2].get_center()), run_time=0.6)
        self.play(dot4.animate.move_to(squares[6].get_center()), run_time=1.2)
        self.play(dot4.animate.move_to(squares[48].get_center()), run_time=1.2)
        self.play(dot4.animate.move_to(squares[45].get_center()), run_time=0.6)
        self.wait(1)

        path5 = VMobject()
        dot5 = Dot()
        dot5.set_color(Color(hue=0.05, saturation=1, luminance=0.5))
        dot5.move_to(orange_circ.get_center())
        path5.set_points_as_corners([dot5.get_center(), dot5.get_center()])
        path5.set_color(Color(hue=0.05, saturation=1, luminance=0.5))
        path5.stroke_width = 20
        def update_path5(path5):
            previous_path5 = path5.copy()
            previous_path5.add_points_as_corners([dot5.get_center()])
            path5.become(previous_path5)
        path5.add_updater(update_path5)
        self.add(path5, dot5)
        self.play(dot5.animate.move_to(squares[11].get_center()), run_time=0.3)
        self.play(dot5.animate.move_to(squares[32].get_center()), run_time=0.8)
        self.play(dot5.animate.move_to(squares[30].get_center()), run_time=0.4)
        self.wait(2)
