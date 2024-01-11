from manim import *
from colour import Color

class Intro2(Scene):
    def construct(self):
        image_unsolved = ImageMobject("images/unsolved.png")
        image_solved = ImageMobject("images/solved.png")
        image_unsolved.scale(0.7)
        image_unsolved.to_edge(LEFT)
        image_unsolved.shift(UP*0.5)
        self.play(FadeIn(image_unsolved))
        self.wait(1)
        text_unsolved = Text("Initial Game State")
        text_unsolved.scale(0.8)
        text_unsolved.next_to(image_unsolved, DOWN)
        self.play(Write(text_unsolved))
        self.wait(2)

        image_solved.scale(0.7)
        image_solved.to_edge(RIGHT)
        image_solved.shift(UP*0.5)
        self.play(FadeIn(image_solved))
        self.wait(1)
        text_solved = Text("Solved Game State")
        text_solved.scale(0.8)
        text_solved.next_to(image_solved, DOWN)
        self.play(Write(text_solved))
        self.wait(4)
        self.play(FadeOut(image_unsolved), FadeOut(image_solved), FadeOut(text_unsolved), FadeOut(text_solved))
