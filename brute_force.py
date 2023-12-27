
from manim import *
from colour import Color

class difficulty(Scene):
    def construct(self):
        ques = Text("How do we determine if an instance of Flow has a solution?")
        ques.scale(0.8)
        ques.shift(UP*3)
        self.play(Write(ques), run_time=2)
        self.wait(2)
        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.45) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0) 
        # squares.shift(LEFT*4)
        red_circ = Circle(color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        red_circ_copy = red_circ.copy()
        red_circ.move_to(squares[5].get_center())
        red_circ_copy.move_to(squares[22].get_center())
        blue_circ = Circle(color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        blue_circ.move_to(squares[6].get_center())
        blue_circ_copy = blue_circ.copy()
        blue_circ_copy.move_to(squares[8].get_center())
        green_circ = Circle(color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        green_circ.move_to(squares[13].get_center())
        green_circ_copy = green_circ.copy()
        green_circ_copy.move_to(squares[15].get_center())
        yellow_circ = Circle(color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1).scale(0.35)
        yellow_circ.move_to(squares[18].get_center())
        yellow_circ_copy = yellow_circ.copy()
        yellow_circ_copy.move_to(squares[20].get_center())
        self.play(FadeIn(squares),Write(red_circ), Write(red_circ_copy), 
                  Write(blue_circ), Write(blue_circ_copy), 
                  Write(green_circ), Write(green_circ_copy),
                    Write(yellow_circ), Write(yellow_circ_copy), run_time=1)
        
        self.wait(0.5)
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
        self.play(dot.animate.move_to(squares[0].get_center()), run_time=0.3)
        self.play(dot.animate.move_to(squares[2].get_center()), run_time=0.3)
        self.play(dot.animate.move_to(squares[22].get_center()), run_time=0.4)

        self.wait(0.5)
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
        self.play(dot2.animate.move_to(squares[8].get_center()), run_time=0.3)

        red_x = ImageMobject("images/x.png").scale(0.1)
        red_x.next_to(squares[14], RIGHT)
        self.play(FadeIn(red_x), run_time=0.2)
        self.wait(0.5)
        self.play(FadeOut(red_x), FadeOut(path), FadeOut(path2), FadeOut(dot), FadeOut(dot2))
        self.wait(0.3)

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
        self.play(dot.animate.move_to(squares[10].get_center()), run_time=0.3)
        self.play(dot.animate.move_to(squares[12].get_center()), run_time=0.3)
        self.play(dot.animate.move_to(squares[22].get_center()), run_time=0.4)
        self.wait(0.2)

        path3 = VMobject()
        dot3 = Dot()
        dot3.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        dot3.move_to(yellow_circ_copy.get_center())
        path3.set_points_as_corners([dot3.get_center(), dot3.get_center()])
        path3.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        path3.stroke_width = 20
        def update_path3(path3):
            previous_path3 = path3.copy()
            previous_path3.add_points_as_corners([dot3.get_center()])
            path3.become(previous_path3)
        path3.add_updater(update_path3)
        self.add(path3, dot3)
        self.play(dot3.animate.move_to(squares[21].get_center()), run_time=0.3)
        self.play(dot3.animate.move_to(squares[16].get_center()), run_time=0.3)
        self.play(dot3.animate.move_to(squares[18].get_center()), run_time=0.4)

        self.play(FadeIn(red_x), run_time=0.2)
        self.wait(0.5)
        self.play(FadeOut(red_x), FadeOut(path), FadeOut(path3), FadeOut(dot), FadeOut(dot3))
        self.wait(0.3)

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
        self.play(dot.animate.move_to(squares[0].get_center()), run_time=0.3)
        self.play(dot.animate.move_to(squares[4].get_center()), run_time=0.3)
        self.play(dot.animate.move_to(squares[24].get_center()), run_time=0.3)
        self.play(dot.animate.move_to(squares[22].get_center()), run_time=0.4)
        self.wait(0.3)

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
        self.play(dot2.animate.move_to(squares[8].get_center()), run_time=0.3)

        path3 = VMobject()
        dot3 = Dot()
        dot3.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        dot3.move_to(yellow_circ_copy.get_center())
        path3.set_points_as_corners([dot3.get_center(), dot3.get_center()])
        path3.set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        path3.stroke_width = 20
        def update_path3(path3):
            previous_path3 = path3.copy()
            previous_path3.add_points_as_corners([dot3.get_center()])
            path3.become(previous_path3)
        path3.add_updater(update_path3)
        self.add(path3, dot3)
        self.play(dot3.animate.move_to(squares[21].get_center()), run_time=0.3)
        self.play(dot3.animate.move_to(squares[16].get_center()), run_time=0.3)
        self.play(dot3.animate.move_to(squares[18].get_center()), run_time=0.3)
        self.wait(0.3)

        path4 = VMobject()
        dot4 = Dot()
        dot4.set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        dot4.move_to(green_circ.get_center())
        path4.set_points_as_corners([dot4.get_center(), dot4.get_center()])
        path4.set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        path4.stroke_width = 20
        def update_path4(path4):
            previous_path4 = path4.copy()
            previous_path4.add_points_as_corners([dot4.get_center()])
            path4.become(previous_path4)
        path4.add_updater(update_path4)
        self.add(path4, dot4)
        self.play(dot4.animate.move_to(squares[10].get_center()), run_time=0.3)
        self.play(dot4.animate.move_to(squares[15].get_center()), run_time=0.3)
        self.wait(0.3)

        checkmark = ImageMobject("images/check.png").scale(0.1)
        checkmark.next_to(squares[14], RIGHT)
        self.play(FadeIn(checkmark), run_time=0.2)
        self.wait(0.5)
        self.play(FadeOut(ques), FadeOut(checkmark), FadeOut(path), FadeOut(path2), FadeOut(path3), FadeOut(path4), FadeOut(dot), FadeOut(dot2), FadeOut(dot3), FadeOut(dot4),
                  FadeOut(squares), FadeOut(red_circ), FadeOut(red_circ_copy), FadeOut(blue_circ), FadeOut(blue_circ_copy), FadeOut(green_circ), 
                  FadeOut(green_circ_copy), FadeOut(yellow_circ), FadeOut(yellow_circ_copy), run_time=0.3)

        


        self.wait(3.5)
