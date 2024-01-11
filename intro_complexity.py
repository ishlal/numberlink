

from manim import *
from colour import Color

class complexity(Scene):
    def construct(self):
        complexity_text = Text("Complexity Theory").scale(1.5)
        self.play(Write(complexity_text), run_time=2.5)
        self.wait(1)
        self.play(FadeOut(complexity_text))
        self.wait(1)

        text_description = Text("Complexity Theory is about classifying problems based on how \ndifficult they are to solve.").scale(0.7)
        text_description.to_edge(UP)
        self.play(Write(text_description), run_time=2)
        self.wait(2)

        # squares = VGroup(
        #     *[VGroup(Square(color=Color(hue=j/16, saturation=1, luminance=0.5)),
        #              fill_opacity=1).scale(0.45) for j in range(16)]
        # ).arrange_in_grid(4, 4, buff=0.3)
        # squares.shift(LEFT*4)
        # self.play(Write(squares), run_time=1)
        # self.wait(2.4)

        ages = [25, 4, 22, 19, 56, 32, 69, 34, 21, 45, 18, 29, 68, 27, 72, 39]


        squares = VGroup(
            *[VGroup(Square(color=Color(hue = j/16, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.65),
                     Text("Person " + str(j+1)+ "\nAge: " + str(ages[j])).scale(0.4)) for j in range(16)]
        ).arrange_in_grid(4, 4, buff=0.1)
        squares.shift(LEFT*3 + DOWN*0.5)
        self.play(Write(squares), run_time=1)
        self.wait(1)

        text_who = Text("Who is the oldest person?").scale(0.7)
        text_who.shift(UP*1.5 + RIGHT*3)
        self.play(Write(text_who), run_time=1)
        self.wait(0.4)


        text_oldest = Text("Oldest: ").scale(0.7)
        text_oldest.shift(UP*0.5 + RIGHT*3)
        text_age = Text("Age: ").scale(0.7)
        text_age.next_to(text_oldest, DOWN)
        self.play(Write(text_oldest), Write(text_age))
        curr_max = 0
        for i in range(16):
            square_i_copy = squares[i].copy()
            square_i_copy.move_to(squares[i].get_center())
            self.add(square_i_copy)
            self.play(square_i_copy.animate.move_to(text_age.get_center() + DOWN), run_time=0.2)
            if ages[i] > curr_max:
                curr_max = ages[i]
                self.play(FadeOut(text_oldest), FadeOut(text_age), run_time=0.2) 
                text_oldest = Text("Oldest: Person " + str(i+1)).scale(0.7)
                text_oldest.shift(UP*0.5 + RIGHT*3)
                text_age = Text("Age: " + str(curr_max)).scale(0.7)
                text_age.next_to(text_oldest, DOWN)
                self.play(Write(text_oldest), Write(text_age), run_time=0.2)
                self.wait(0.2)
            else:
                self.wait(0.2)
            self.play(FadeOut(square_i_copy), run_time=0.3)
        self.wait(2)
        self.play(FadeOut(text_oldest), FadeOut(text_age), FadeOut(text_who))
        self.wait(1)
        text_friends = Text("Are there 8 people who are pairwise friends?").scale(0.5)
        text_friends.shift(UP*1.5 + RIGHT*3)
        self.play(Write(text_friends), run_time=1)
        self.wait(0.4)
        empty_squares = VGroup(
            *[VGroup(Square(color=Color(hue = 0, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.65)) for j in range(8)]
        ).arrange_in_grid(2, 4, buff=0.1)
        empty_squares.next_to(text_friends, DOWN)
        # self.add(empty_squares)
        random_subset_1 = [3, 11, 6, 2, 1, 5, 9, 13]
        to_remove = []
        for i in range(len(random_subset_1)):
            square_i_copy = squares[random_subset_1[i]].copy()
            to_remove.append(square_i_copy)
            square_i_copy.move_to(squares[random_subset_1[i]].get_center())
            self.add(square_i_copy)
            self.play(square_i_copy.animate.move_to(empty_squares[i].get_center()), run_time=0.2)
            self.wait(0.1)
        self.wait(1)
        image_x = ImageMobject("images/x.png").scale(0.2)
        image_x.next_to(empty_squares, DOWN)
        self.play(FadeIn(image_x))
        self.wait(1)
        self.play(FadeOut(image_x))
        for i in range(len(to_remove)):
            self.remove(to_remove[i])

        random_subset_2 = [15, 2, 0, 4, 11, 12, 10, 7]
        to_remove_2 = []
        for i in range(len(random_subset_2)):
            square_i_copy = squares[random_subset_2[i]].copy()
            to_remove_2.append(square_i_copy)
            square_i_copy.move_to(squares[random_subset_2[i]].get_center())
            self.add(square_i_copy)
            self.play(square_i_copy.animate.move_to(empty_squares[i].get_center()), run_time=0.2)
            self.wait(0.1)
        self.wait(1)
        self.play(FadeIn(image_x))
        self.wait(1)
        self.play(FadeOut(image_x))
        self.wait(1)
        text_qmark = Text("?").scale(2.5)
        text_qmark.next_to(empty_squares, DOWN)
        self.play(FadeIn(text_qmark))
        self.wait(2)
        for i in range(len(to_remove_2)):
            self.remove(to_remove_2[i])
        self.play(FadeOut(text_description), FadeOut(text_qmark), FadeOut(text_friends), FadeOut(empty_squares), 
                    FadeOut(squares))

        
