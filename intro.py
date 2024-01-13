from manim import *
from colour import Color 

class Intro(Scene):
    def construct(self):
        # add image to left side of screen
        image = ImageMobject("images/flow.png")
        image.scale(1.2)
        image.to_edge(LEFT)
        image.shift(UP)
        self.play(FadeIn(image))
        self.wait(1)
        text_flow = Text("Flow Free")
        text_flow.scale(1.1)
        text_flow.next_to(image, DOWN)
        self.play(Write(text_flow))
        self.wait(2)
        blist = BulletedList("Released in 2012", "Big Duck Games LLC", "Stars: 4.8/5").scale(1.2)
        # text1 = Text("- Released in 2012")
        # text2 = Text("- Big Duck Games LLC")
        # text3 = Text("- Stars: 4.8/5")
        blist.shift(UP + RIGHT*2)
        text1 = blist[0]
        text2 = blist[1]
        text3 = blist[2]

        # text1.shift(UP + RIGHT*2)
        # text2.shift(RIGHT*2)
        # text3.shift(DOWN + RIGHT*2)

        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(1)
        self.play(Write(text3))
        self.wait(2)