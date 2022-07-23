from multiprocessing.connection import wait
from pickle import FALSE
from select import select
from tokenize import Number
from turtle import right
from manim import *


class EquivClasses(Scene):
    def construct(self):

        zero = Square(1.5, color=RED, fill_opacity=0.5,).shift(LEFT*2)
        one = Square(1.5, color=GREEN, fill_opacity=0.5)
        two = Square(1.5, color=BLUE, fill_opacity=0.5).shift(RIGHT*2)

        shapes = VGroup(zero, one, two)
        self.play(SpiralIn(shapes, 8, 0.2))

        equiv_zero = MathTex('3Z').scale(1).shift(UP*1.5, LEFT*2)
        equiv_one = MathTex('1+3Z').scale(1).shift(UP*1.5)
        equiv_two = MathTex('2+3Z').scale(1).shift(UP*1.5, RIGHT*2)

        equiv = VGroup(equiv_zero, equiv_one, equiv_two)

        self.play(FadeIn(equiv))
        self.wait(1)

        class_zero = MathTex(0).scale(1).shift(LEFT*2)
        class_one = MathTex(1).scale(1)
        class_two = MathTex(2).scale(1).shift(RIGHT*2)

        equiv_class = VGroup(class_zero, class_one, class_two)

        self.play(FadeIn(equiv_class))
        self.wait(0.5)
        self.play(Uncreate(equiv_class))

        class_zero = MathTex(3).scale(1).shift(LEFT*2)
        class_one = MathTex(4).scale(1)
        class_two = MathTex(5).scale(1).shift(RIGHT*2)

        equiv_class = VGroup(class_zero, class_one, class_two)

        self.play(FadeIn(equiv_class))
        self.wait(0.5)
        self.play(Uncreate(equiv_class))

        class_zero = MathTex('...').scale(1).shift(LEFT*2)
        class_one = MathTex('...').scale(1)
        class_two = MathTex('...').scale(1).shift(RIGHT*2)

        equiv_class = VGroup(class_zero, class_one, class_two)

        self.play(FadeIn(equiv_class))
        self.wait(0.5)
        self.play(Uncreate(equiv_class))
        self.wait(1)
        self.clear()
