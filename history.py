from manim import *
from colour import Color

class Gameplay(Scene):
    def construct(self):
        puzzled_neighbor = ImageMobject("images/puzzled_neighbor.png")
        puzzled_neighbor.shift(DOWN*0.5)
        puzzled_neighbor.scale(0.7)
        self.play(FadeIn(puzzled_neighbor))
        self.wait(1)

        brooklyn_eagle = ImageMobject("images/brooklyn.jpg")
        brooklyn_eagle.to_edge(UP)
        brooklyn_eagle.scale(1.5)
        self.play(FadeIn(brooklyn_eagle))
        self.wait(2.5)

        sam_loyd = ImageMobject("images/samloyd.jpg")
        sam_loyd.shift(LEFT*5)
        # sam_loyd.shift(DOWN)
        sam_loyd.scale(0.3)
        self.play(FadeIn(sam_loyd))

        self.wait(1.5)
        name = Text("Sam Loyd")
        name.next_to(sam_loyd, DOWN)
        name.scale(0.7)
        years = Text("1841 - 1911")
        years.next_to(name, DOWN)
        years.scale(0.5)
        self.play(Write(name))
        self.wait(0.2)
        self.play(Write(years))
        self.wait(2.2)
        self.play(FadeOut(puzzled_neighbor))
        self.wait(1)

        blist = BulletedList("Chess Player", "Mathematician", "Puzzle Composer")

        text_chessplayer = Text("Chess Player")
        text_chessplayer.next_to(sam_loyd, RIGHT)
        text_chessplayer.shift(RIGHT*0.5)
        # self.play(Write(text_chessplayer))
        self.play(Write(blist[0]))
        self.wait(0.5)
        text_mathematician = Text("Mathematician")
        text_mathematician.next_to(text_chessplayer, DOWN)
        # self.play(Write(text_mathematician))
        self.play(Write(blist[1]))
        self.wait(0.5)
        text_puzzle = Text("Puzzle Composer")
        text_puzzle.next_to(text_mathematician, DOWN)
        # self.play(Write(text_puzzle))
        self.play(Write(blist[2]))
        self.wait(2)
        # self.play(FadeOut(text_chessplayer), FadeOut(text_mathematician), FadeOut(text_puzzle))
        self.play(FadeOut(blist))
        self.wait(1)


        donkey1 = ImageMobject("images/donkey1.png").scale(0.8)
        person = ImageMobject("images/person.png").scale(0.8)
        donkey2 = ImageMobject("images/donkey2.png").scale(0.8)
        # donkey1.shift(DOWN*0.5 + LEFT)
        donkey1.shift(UP + LEFT)
        #rotate donkey1
        donkey1.rotate(-PI/2)
        person.next_to(donkey1, RIGHT)
        person.shift(DOWN)
        donkey2.rotate(PI/2)
        donkey2.next_to(donkey1, DOWN)
        self.play(FadeIn(donkey1), FadeIn(person), FadeIn(donkey2))
        self.wait(1)
        text_donkey = Text("Trick Donkeys Puzzle")
        text_donkey.next_to(person, DOWN)
        text_donkey.shift(DOWN*0.3)
        self.play(Write(text_donkey))
        self.wait(1)
        # bring person to front
        self.bring_to_front(person)
        

        self.play(donkey2.animate.rotate(PI/2))
        self.wait(0.3)
        self.play(donkey2.animate.move_to(person.get_center() + RIGHT*1.1))
        # animate moving donkey 1 so that left edge of donkey1 and right edge of person touch
        self.play(donkey1.animate.rotate(-PI/2))
        self.wait(0.4)
        self.play(donkey1.animate.move_to(person.get_center() + LEFT*1.1))
        # self.play(donkey2.animate.shift(LEFT*4.75))
        # self.play(donkey2.right_edge.move_to(person.left_edge))
        self.wait(2)

        self.play(FadeOut(donkey1), FadeOut(person), FadeOut(donkey2), FadeOut(text_donkey))

        # create right triangle with side lengths 8 and 3
        CUSTOM_SHIFT = 7/3
        triangle_1 = Polygon([-2/3 + CUSTOM_SHIFT, -2/3, 0], [-2/3 + CUSTOM_SHIFT, -5/3, 0], [-10/3 + CUSTOM_SHIFT, -5/3, 0])
        triangle_1.set_color(GREEN)
        triangle_2 = Polygon([-2/3 + CUSTOM_SHIFT, -2/3, 0], [3/3 + CUSTOM_SHIFT, -2/3, 0], [1 + CUSTOM_SHIFT, 0, 1])
        triangle_2.set_color(BLUE)
        red_blob = Polygon([-2/3 + CUSTOM_SHIFT, -2/3, 0], [3/3 + CUSTOM_SHIFT, -2/3, 0], [1 + CUSTOM_SHIFT, -3/3, 0], [0 + CUSTOM_SHIFT, -3/3, 0], [0 + CUSTOM_SHIFT, -4/3, 0], [-2/3 + CUSTOM_SHIFT, -4/3, 0])
        red_blob.set_color(RED)
        yellow_blob = Polygon([-2/3 + CUSTOM_SHIFT, -4/3, 0], [-2/3 + CUSTOM_SHIFT, -5/3, 0], [3/3 + CUSTOM_SHIFT, -5/3, 0], [3/3 + CUSTOM_SHIFT, -3/3, 0], [0 + CUSTOM_SHIFT, -3/3, 0], [0 + CUSTOM_SHIFT, -4/3, 0])
        yellow_blob.set_color(YELLOW)
        self.play(Create(triangle_1), Create(triangle_2), Create(red_blob), Create(yellow_blob))
        text_vanishing_area = Text("Vanishing Area Puzzle")
        text_vanishing_area.next_to(yellow_blob, DOWN)
        text_vanishing_area.shift(LEFT)
        self.play(Write(text_vanishing_area))
        self.wait(0.5)
        self.play(red_blob.animate.shift([-1, 0, 0]), triangle_1.animate.shift([-1, 0, 0]))
        self.wait(0.3)
        self.play(red_blob.animate.shift([0, -1/3, 0]))
        self.play(triangle_1.animate.shift([8/3, 2/3, 0]), triangle_2.animate.shift([-8/3, -1, 0]))
        purple_square = Polygon([-2/3 + CUSTOM_SHIFT, -5/3, 0], [-3/3 + CUSTOM_SHIFT, -5/3, 0], [-3/3 + CUSTOM_SHIFT, -4/3, 0], [-2/3 + CUSTOM_SHIFT, -4/3, 0])
        purple_square.set_color(PURPLE)
        # fill purple square
        self.wait(0.3)
        self.play(Create(purple_square))

        self.wait(2)

        self.play(FadeOut(triangle_1), FadeOut(triangle_2), FadeOut(red_blob), FadeOut(yellow_blob), FadeOut(purple_square), FadeOut(text_vanishing_area),
                  FadeOut(brooklyn_eagle), FadeOut(sam_loyd), FadeOut(name), FadeOut(years))
