import numpy as np
from manim import *
from manim.utils.color import XKCD

class Tracing1(Scene):
    def construct(self):
        camera_body = RoundedRectangle(0.24, width=4.2, height=3)
        camera_lens = RoundedRectangle(0.24, width=0.5, height=2).shift(RIGHT*2.16)
        camera_body.set_fill(WHITE, 1)
        camera_lens.set_fill(WHITE, 1)
        
        camera = Group(camera_body, camera_lens)
        
        self.play(Create(camera_body), Create(camera_lens), camera.animate.scale(0.4).shift(LEFT*4))
        
        sphere = Circle(radius=0.8)
        square = Square(side_length=1.32)
        triangle = Triangle()
        
        sphere.set_fill(XKCD.AMETHYST, 1)
        square.set_fill(XKCD.EMERALD, 1)
        triangle.set_fill(XKCD.BLUEBERRY, 1)
        
        sphere.shift(UP*1).shift(LEFT*0.4)
        square.shift(LEFT*1.2).shift(DOWN).rotate(-PI/6)
        triangle.shift(RIGHT*1.2).shift(DOWN*1.2).rotate(PI/4)
        
        scene = Group(sphere, square, triangle)
        
        self.play(Create(sphere), Create(square), Create(triangle), scene.animate.shift(RIGHT*4))
        
        light = Dot()
        light.set_fill(XKCD.WHITE, 1)
        
        self.play(Create(light), light.animate.shift(LEFT).shift(UP*3))
        
        rays = []
        for v in triangle.get_vertices():
            ray = Line(v, camera.get_center())
            ray.set_stroke(WHITE, 2)
            rays.append(ray)
        self.play(*[Create(r) for r in rays])
        self.wait(1)
        self.play(*[Uncreate(r) for r in rays])

class GPU(Scene):
    def construct(self):
        body = RoundedRectangle(0.24, width=6, height=2.32)
        body.set_fill(WHITE, 0.8)
        self.play(Create(body))
        
        fans = [SVGMobject("img/fan.svg").scale(0.94) for _ in range(3)]
        fans[1].shift(LEFT*2).rotate(-PI/5)
        fans[2].shift(RIGHT*2).rotate(PI/6)
        self.play(*[Create(f) for f in fans])
        
        self.play(
            *[Rotate(
                fan,
                angle=-80*PI,
                about_point=fan.get_center(),
                rate_func=rate_functions.ease_in_out_cubic,
                run_time=12
            ) for fan in fans]
        )
        
        self.wait(1)
        self.play(*[Uncreate(f) for f in fans])
        self.play(Uncreate(body))

class BreakIntoTris(Scene):
    def construct(self):
        square = Square(side_length=2)
        square.set_fill(XKCD.WHITE, 1)
        
        self.play(Create(square))
        
        verts = square.get_vertices()
        tri1 = Polygon(verts[0], verts[1], verts[2]).set_fill(XKCD.AMETHYST, 1)
        tri2 = Polygon(verts[0], verts[2], verts[3]).set_fill(XKCD.BLUEBERRY, 1)
        
        self.play(Create(tri1, run_time = 2))
        self.play(Create(tri2, run_time = 2))
        self.wait(1)