from manim import *
from manim import XKCD as xkcd

class Intro(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        
        banner = ManimBanner(dark_theme=False)
        text = Text("Made with", font="sans-serif", color=xkcd.BLACK)

        self.play(Write(text))
        self.wait(1)
        self.play(text.animate.to_edge(UP))
        self.play(banner.create())
        self.play(banner.expand())
        self.wait(2)
        self.play(Unwrite(banner), Unwrite(text))
        self.wait(2)

class Duction(Scene):
    def construct(self):
        # self.wait(2) # For the crossfade thing
        camera = SVGMobject('./img/camera')
        rust = SVGMobject('./img/rust')
        text = Text("In", font="sans-serif")
        
        self.play(Write(camera))
        self.play(camera.animate.move_to(LEFT * 2.5))
        rust.move_to(RIGHT * 2.5)
        self.play(Write(text), Write(rust))
        self.wait(2)
        self.play(Unwrite(camera),Unwrite(text))
        self.play(rust.animate.move_to(LEFT * 0))
        self.play(rust.animate.scale(84.0))

        self.wait(2)

class Rasterization(Scene):
    def construct(self):
        pass

