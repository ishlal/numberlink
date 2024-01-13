

from manim import *
from colour import Color 

class rem_red(Scene):
    def construct(self):
        text_reduction = Text("Reduction").scale(1.2)
        text_reduction.to_edge(UP)
        line = Line(start=text_reduction.get_corner(DOWN+LEFT) + DOWN*0.3 + LEFT*0.3, end=text_reduction.get_corner(DOWN+RIGHT) + DOWN*0.3 + RIGHT*0.3)
        self.play(Write(text_reduction), Create(line))
        self.wait(2)
        box_reduction = Rectangle(height=2, width=4)
        box_reduction.set_color(GRAY)
        box_reduction.set_fill(GRAY).set_opacity(1)
        box_reduction.move_to(ORIGIN)
        triangle_1 = Polygon(ORIGIN + LEFT, box_reduction.get_corner(UP+LEFT) + DOWN*0.3 + LEFT*0.5, box_reduction.get_corner(DOWN+LEFT) + UP*0.3 + LEFT*0.5)
        triangle_1.set_color(GRAY)
        triangle_1.set_fill(GRAY).set_opacity(1)
        self.bring_to_back(triangle_1)
        rectangle_2 = Rectangle(height=1, width=1)
        rectangle_2.set_color(GRAY)
        rectangle_2.set_fill(GRAY).set_opacity(1)
        rectangle_2.move_to((box_reduction.get_corner(UP+RIGHT) + box_reduction.get_corner(DOWN + RIGHT))/2)
        reduction_machine = VGroup(box_reduction, triangle_1, rectangle_2)
        text_reduction_machine = Text("Reduction Machine").scale(0.5)
        text_reduction_machine.move_to(box_reduction.get_center())
        self.play(Create(box_reduction), Create(triangle_1), Create(rectangle_2),
                  Write(text_reduction_machine))
        self.wait(2)
        var_phi = MathTex(r"\varphi",  r"= (x_1 \lor \overline{x_2} \lor x_3) \land (\overline{x_1} \lor x_3 \lor x_4) \land (x_2 \lor \overline{x_3} \lor x_4)")
        var_phi.shift(DOWN*3)
        self.play(Write(var_phi))
        self.wait(2)
        var_phi_copy = var_phi[0].copy()
        self.play(FadeOut(var_phi), var_phi_copy.animate.move_to(ORIGIN + LEFT*4).scale(1.5))
        self.wait(2)
        self.play(var_phi_copy.animate.shift(RIGHT*2.5))
        self.play(FadeOut(var_phi_copy))
        self.wait(2)

        circles = VGroup(
            *[VGroup(Circle(color=WHITE,
                     fill_opacity=1).scale(0.15),
                     Text(str(j+1)).scale(0.5).set_color(BLACK)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.7)
        circles.shift(RIGHT*3 + UP*1.2)

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
        # self.play(Write(edges), run_time=1)
        # self.wait(1)

        # bring circles to front
        # self.bring_to_front(circles[5], circles[22], circles[6], circles[8], circles[13], circles[15], circles[18], circles[20])

        # change color of circles[5] to red and enlarge it

        circles[5][0].scale(1.6)
        circles[5][0].set_color(Color(hue=0, saturation=1, luminance=0.5))
        circles[22][0].scale(1.6)
        circles[22][0].set_color(Color(hue=0, saturation=1, luminance=0.5))
        circles[6][0].scale(1.6)
        circles[6][0].set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        circles[8][0].scale(1.6)
        circles[8][0].set_color(Color(hue=0.6, saturation=1, luminance=0.5))
        circles[13][0].scale(1.6)
        circles[13][0].set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        circles[15][0].scale(1.6)
        circles[15][0].set_color(Color(hue=0.3, saturation=1, luminance=0.5))
        circles[18][0].scale(1.6)
        circles[18][0].set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        circles[20][0].scale(1.6)
        circles[20][0].set_color(Color(hue=0.15, saturation=1, luminance=0.5))
        # self.play(circles[5][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
        #            circles[22][0].animate.set_color(Color(hue=0, saturation=1, luminance=0.5)),
        #            circles[6][0].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
        #             circles[8][0].animate.set_color(Color(hue=0.6, saturation=1, luminance=0.5)),
        #              circles[13][0].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
        #               circles[15][0].animate.set_color(Color(hue=0.3, saturation=1, luminance=0.5)),
        #                circles[18][0].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
        #                 circles[20][0].animate.set_color(Color(hue=0.15, saturation=1, luminance=0.5)),
        #                          run_time=0.3)



        # graph_img = ImageMobject("images/graph_img.png").scale(0.01)
        graph_img = VGroup(
            edges, circles
        )
        graph_img.move_to(ORIGIN)
        graph_img.scale(0.01)
        self.play(FadeIn(graph_img))
        self.bring_to_back(graph_img[1])
        self.play(graph_img.animate.shift(RIGHT*5).scale(60))
        self.wait(2)
        varphi = MathTex(r"\varphi").scale(1.5)
        varphi.move_to(ORIGIN + LEFT*4)
        self.play(FadeIn(varphi))
        self.wait(1)

        img_check = ImageMobject("images/check.png").scale(0.1)
        img_check_copy = img_check.copy()
        img_check.next_to(varphi, DOWN)
        img_check.shift(DOWN * 0.9)
        img_check_copy.next_to(graph_img, DOWN)
        self.play(FadeIn(img_check))
        self.wait(1)
        self.play(FadeIn(img_check_copy))
        self.wait(2)
        self.play(FadeOut(img_check), FadeOut(img_check_copy))

        img_x = ImageMobject("images/x.png").scale(0.1)
        img_x_copy = img_x.copy()
        img_x.next_to(varphi, DOWN)
        img_x.shift(DOWN*0.9)
        img_x_copy.next_to(graph_img, DOWN)
        self.play(FadeIn(img_x))
        self.wait(1)
        self.play(FadeIn(img_x_copy))
        self.wait(2)
        self.play(FadeOut(img_x), FadeOut(img_x_copy))

        self.play(FadeOut(varphi),
                  FadeOut(box_reduction), 
                  FadeOut(triangle_1),
                    FadeOut(rectangle_2),
                  FadeOut(text_reduction_machine))
        

        squares = VGroup(
            *[VGroup(Square(color=WHITE),
                     fill_opacity=0.5).scale(0.3) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0)
        text_version1 = Text("Version 1").scale(0.7)
        text_version1.next_to(squares, DOWN)
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
        red_line_1 = Line(squares[20].get_center(), squares[24].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_1.stroke_width = 15
        red_line_2 = Line(squares[24].get_center(), squares[19].get_center(), color=Color(hue=0, saturation=1, luminance=0.5), fill_opacity=1)
        red_line_2.stroke_width = 15
        blue_line_1 = Line(squares[15].get_center(), squares[18].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_1.stroke_width = 15
        blue_line_2 = Line(squares[18].get_center(), squares[13].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_2.stroke_width = 15
        blue_line_3 = Line(squares[13].get_center(), squares[14].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_3.stroke_width = 15
        blue_line_4 = Line(squares[14].get_center(), squares[4].get_center(), color=Color(hue=0.6, saturation=1, luminance=0.5), fill_opacity=1)
        blue_line_4.stroke_width = 15
        green_line_1 = Line(squares[0].get_center(), squares[5].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1)
        green_line_1.stroke_width = 15
        green_line_2 = Line(squares[5].get_center(), squares[7].get_center(), color=Color(hue=0.3, saturation=1, luminance=0.5), fill_opacity=1)
        green_line_2.stroke_width = 15
        yellow_line_1 = Line(squares[1].get_center(), squares[3].get_center(), color=Color(hue=0.15, saturation=1, luminance=0.5), fill_opacity=1)
        yellow_line_1.stroke_width = 15
        self.play(graph_img.animate.move_to(ORIGIN).scale(0.01))
        self.play(FadeIn(squares), Write(text_version1), FadeIn(red_circ), FadeIn(red_circ_copy), 
                  FadeIn(blue_circ), FadeIn(blue_circ_copy), 
                  FadeIn(green_circ), FadeIn(green_circ_copy),
                    FadeIn(yellow_circ), FadeIn(yellow_circ_copy), FadeOut(graph_img), run_time=1)
        # self.play(FadeIn(red_line_1), FadeIn(red_line_2))
        # self.wait(0.5)
        # self.play(FadeIn(blue_line_1), FadeIn(blue_line_2), FadeIn(blue_line_3), FadeIn(blue_line_4))
        # self.wait(0.5)
        # self.play(FadeIn(green_line_1), FadeIn(green_line_2))
        # self.wait(0.5)
        # self.play(FadeIn(yellow_line_1))
        # self.wait(1)
        self.wait(2)
        self.play(FadeIn(red_line_1), FadeIn(red_line_2), FadeIn(blue_line_1), FadeIn(blue_line_2), FadeIn(blue_line_3), FadeIn(blue_line_4), 
                  FadeIn(green_line_1), FadeIn(green_line_2), FadeIn(yellow_line_1))
        self.wait(2)
        self.play(
            FadeOut(squares), FadeOut(text_version1), FadeOut(red_circ), FadeOut(red_circ_copy), 
                  FadeOut(blue_circ), FadeOut(blue_circ_copy), 
                  FadeOut(green_circ), FadeOut(green_circ_copy),
                    FadeOut(yellow_circ), FadeOut(yellow_circ_copy),
                    FadeOut(red_line_1), FadeOut(red_line_2), FadeOut(blue_line_1), FadeOut(blue_line_2), FadeOut(blue_line_3), FadeOut(blue_line_4),
                    FadeOut(green_line_1), FadeOut(green_line_2), FadeOut(yellow_line_1))
        
        self.wait(2)
        blist = BulletedList("Boolean formula should be arbitrary", "Procedure should be generalizable")
        self.play(Write(blist[0]))
        self.wait(2)
        self.play(Write(blist[1]))
        self.wait(2)