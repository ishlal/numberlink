from manim import *
from colour import Color

class RightTriangleScene(Scene):
    def construct(self):
        # Create vertices of the triangle
        CUSTOM_SHIFT = 7/3
        triangle_1 = Polygon([-2/3 + CUSTOM_SHIFT, -2/3, 0], [-2/3 + CUSTOM_SHIFT, -5/3, 0], [-10/3 + CUSTOM_SHIFT, -5/3, 0])
        triangle_1.set_color(GREEN)
        self.play(Create(triangle_1))
        triangle_2 = Polygon([-2/3 + CUSTOM_SHIFT, -2/3, 0], [3/3 + CUSTOM_SHIFT, -2/3, 0], [1 + CUSTOM_SHIFT, 0, 1])
        triangle_2.set_color(BLUE)
        self.play(Create(triangle_2))
        red_blob = Polygon([-2/3 + CUSTOM_SHIFT, -2/3, 0], [3/3 + CUSTOM_SHIFT, -2/3, 0], [1 + CUSTOM_SHIFT, -3/3, 0], [0 + CUSTOM_SHIFT, -3/3, 0], [0 + CUSTOM_SHIFT, -4/3, 0], [-2/3 + CUSTOM_SHIFT, -4/3, 0])
        red_blob.set_color(RED)
        self.play(Create(red_blob))
        yellow_blob = Polygon([-2/3 + CUSTOM_SHIFT, -4/3, 0], [-2/3 + CUSTOM_SHIFT, -5/3, 0], [3/3 + CUSTOM_SHIFT, -5/3, 0], [3/3 + CUSTOM_SHIFT, -3/3, 0], [0 + CUSTOM_SHIFT, -3/3, 0], [0 + CUSTOM_SHIFT, -4/3, 0])
        yellow_blob.set_color(YELLOW)
        self.play(Create(yellow_blob))
        self.wait(2)
        self.play(red_blob.animate.shift([-1, 0, 0]), triangle_1.animate.shift([-1, 0, 0]))
        self.wait(0.5)
        self.play(red_blob.animate.shift([0, -1/3, 0]))
        self.play(triangle_1.animate.shift([8/3, 2/3, 0]), triangle_2.animate.shift([-8/3, -1, 0]))
        self.wait(2)