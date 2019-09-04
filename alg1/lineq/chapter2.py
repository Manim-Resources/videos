from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Introduction to Linear Equations")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        self.play(Write(title), Write(rect))
        self.wait()

        self.play(Uncreate(title), Uncreate(rect))
        self.wait()

        axes = Axes(
            x_min=-5,
            x_max=5,
            y_min=-3,
            y_max=3,
            number_line_config={
                "include_tip": False,
            }
        )

        f1 = FunctionGraph(lambda x: x)
        f2 = FunctionGraph(lambda x: 3*x, color=RED)

        self.play(Write(axes), Write(f1), Write(f2))
        self.wait()


class SlopeCalc(Scene):
    def construct(self):
        eqt = TexMobject("y=0.5x+1").scale(1.5)
        eqt.shift(3 * UP)

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=-2,
            y_max=2,
            number_line_config={
                "include_tip": False,
            }
        )
        f = ParametricFunction(
            lambda t: np.array([t, 0.5*t+1, 0]),
            t_min=-3,
            t_max=3,
            color=BLUE
        )
        eq = VGroup(axes, f).shift(1 * DOWN)

        self.play(Write(eqt))
        self.wait()

        self.play(Write(eq))
        self.wait()

        self.play(eq.shift, 2 * RIGHT)

        self.plot(2)
        self.plot(1)

        eq1 = TexMobject(r"\Delta x = 2 - 1 = 1")
        eq1.scale(1.5)
        eq1.shift(2 * LEFT + 1 * UP)

        eq2 = TexMobject(r"\Delta y = 2 - 1.5 = 0.5")
        eq2.scale(1.5)
        eq2.shift(2 * LEFT - 1 * UP)

        eq3 = TexMobject(r"\frac{\Delta y}{\Delta x} = 0..5")
        eq3.scale(1.5)
        eq3.shift(2 * LEFT - 2 * UP)

        self.play(Write(eq1))
        self.wait()

        self.play(Write(eq2))
        self.wait()

        self.play(Write(eq3))
        self.wait()

    def plot(self, x):
        y = x * 0.5 + 1

        p = Circle(radius=0.1,  color=YELLOW,
                   fill_opacity=1).shift(x * RIGHT + y * UP)
        p.shift(2 * RIGHT + 1 * DOWN)

        t = TexMobject(r"({},{})".format(str(x), str(y)))
        t.shift((x + 2) * RIGHT + (y - 0.25) * UP)

        self.play(Write(t))
        self.play(Write(p))
        self.wait()
