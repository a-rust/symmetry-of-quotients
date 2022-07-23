from multiprocessing.connection import wait
from pickle import FALSE
from select import select
from tokenize import Number
from turtle import right
from manim import *


class Symmetry(Scene):
    def construct(self):

        ax = Axes(x_range=[-4, 4, 1], y_range=[-4, 4, 1], x_length=8, y_length=8
                  ).add_coordinates()

        dots_zero = VGroup()

        line_zero_x = []
        line_zero_y = []
        line_zero = VGroup()

        for i in range(-3, 4, 1):
            if (i-0) % 3 == 0 or (0-i) % 3 == 0:
                dots_zero.add(
                    Dot((i, 0, 0), color=RED))
                dots_zero.add(
                    Dot((0, i, 0), color=RED))

        for i in range(-3, 4, 1):
            for j in range(-3, 4, 1):
                if i % 3 == 0 and ((i-j) % 3 == 0 or (j-i) % 3 == 0):
                    dots_zero.add(
                        Dot((i, j, 0), color=RED))
                    dots_zero.add(
                        Dot((j, i, 0), color=RED))

        dots_one = VGroup()

        line_one_x = []
        line_one_y = []
        line_one = VGroup()

        for i in range(-4, 5, 1):
            if (i-1) % 3 == 0 or (1-i) % 3 == 0:
                dots_one.add(
                    Dot((1, i, 0), color=GREEN))
                dots_one.add(Dot((i, 1, 0), color=GREEN))

        for i in range(-4, 5, 1):
            for j in range(-4, 5, 1):
                if i % 3 == 1 and ((i-j) % 3 == 0 or (j-i) % 3 == 0):
                    dots_one.add(
                        Dot((i, j, 0), color=GREEN))
                    dots_one.add(
                        Dot((j, i, 0), color=GREEN))

        dots_two = VGroup()

        line_two_x = []
        line_two_y = []
        line_two = VGroup()

        for i in range(-4, 5, 1):
            if (i-2) % 3 == 0 or (2-i) % 3 == 0:
                dots_two.add(
                    Dot((i, 2, 0), color=BLUE))
                dots_two.add(
                    Dot((2, i, 0), color=BLUE))

        for i in range(-4, 5, 1):
            for j in range(-4, 5, 1):
                if i % 3 == 2 and ((i-j) % 3 == 0 or (j-i) % 3 == 0):
                    dots_two.add(
                        Dot((i, j, 0), color=BLUE))
                    dots_two.add(
                        Dot((j, i, 0), color=BLUE))

        dots = VGroup(dots_zero, dots_one, dots_two)

        zero_line = VGroup()
        for i in range(0, len(dots_zero)):
            for j in range(0, len(dots_zero)):
                zero_line.add(Line(dots_zero[i],
                                   dots_zero[j], color=RED))

        one_line = VGroup()
        for i in range(0, len(dots_one)):
            for j in range(0, len(dots_one)):
                one_line.add(Line(dots_one[i],
                                  dots_one[j], color=GREEN))

        two_line = VGroup()
        for i in range(0, len(dots_two)):
            for j in range(0, len(dots_two)):
                two_line.add(Line(dots_two[i],
                                  dots_two[j], color=BLUE))

        self.play(Create(NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1], x_length=8, y_length=8)))
        self.play(Create(ax))
        self.play(Create(dots))

        self.wait(1)

        self.play(FadeIn(zero_line))
        self.wait(1)
        self.play(FadeOut(zero_line))
        self.play(FadeIn(one_line))
        self.wait(1)
        self.play(FadeOut(one_line))
        self.play(FadeIn(two_line))
        self.wait(1)
        self.play(FadeOut(two_line))
        self.play(FadeIn(zero_line, one_line, two_line))
        self.wait(1.5)
