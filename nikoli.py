from manim import *
from colour import Color

class RightTriangleScene(Scene):
    def construct(self):
        # self.set_speech_service(RecorderService())
        image_nikoli = ImageMobject("images/nikoli.png").scale(0.8)
        image_nikoli.to_edge(UP)
        # with self.voiceover(text="This circle is drawn as I speak.") as tracker:
        #     self.play(FadeIn(image_nikoli))
        #     tracker.add_frame()
        self.play(FadeIn(image_nikoli))
        # self.wait(1)

        sudoku = ImageMobject("images/sudoku.jpg").scale(1.5)
        sudoku.shift(LEFT*5 + DOWN*0.5)
        self.play(FadeIn(sudoku))
        text_sudoku = Text("Sudoku")
        text_sudoku.next_to(sudoku, DOWN)
        self.play(Write(text_sudoku))
        self.wait(1)

        shikaku = ImageMobject("images/Shikaku.webp").scale(1.6)
        shikaku.shift(RIGHT*5 + DOWN*0.5)
        self.play(FadeIn(shikaku))
        text_shikaku = Text("Shikaku")
        text_shikaku.next_to(shikaku, DOWN)
        self.play(Write(text_shikaku))

        self.wait(1)

        numberlink = ImageMobject("images/numberlink.png").scale(0.6)
        numberlink.shift(DOWN*0.5)
        self.play(FadeIn(numberlink))
        text_numberlink = Text("NumberLink")
        text_numberlink.next_to(numberlink, DOWN)
        self.play(Write(text_numberlink))
        

        self.wait(2)
