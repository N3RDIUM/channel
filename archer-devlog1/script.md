# Devlog 1 [Ray tracing on a POTATO PC?!]

[VISUAL] Obi-wan Kenobi saying "Hello There" [null]

Welcome to my first devlog. Today, we're gonna be starting a new project, called Arhcer.

[VISUAL] Arhcer logo [on "Archer"]

Arhcer is a ray tracing engine. But it's not an ordinary ray tracer. It's built to run at a decent framerate even on a potato.

[VISUAL] Bold, Italic, Double-underlined, Double quoted, distored word "DECENT" [on "decent"]
[VISUAL] A potato [on "potato" additive]

In fact, it's being built by me ON a potato PC. AND, it's being made in PYTHON.

[VISUAL] Python logo to the right of "DECENT", a plus in the middle [on "DECENT" additive]
[VISUAL] Equals sign, nuclear explosion over PC [after previous additive]

How am I going to do that? Honestly, I don't know. We'll figure it out. Feel free to follow along.

[VISUAL] Quote: "Honestly, I don't know" -me [after "that?"]

All the code and the scripts and visuals for this video are available on GitHub on a GPL v3 License.

[VISUAL] GitHub logo [on "All"]

Let's get started. First, let's look at the fundamentals of ray tracing.<br>Unless you've been living under a rock, you probably know what raytracing is.

[VISUAL] Black screen [on "Let's"]

Most games and other things use rasterization. This is the process of breaking your model into a bunch of triangles, and then mapping their vertices on a flat screen.

[VISUAL] animation of a cube breaking into triangles [on "breaking"]
[VISUAL] mapping onto a flat surface [on "mapping" additive]

Today's GPUs are optimized for this and they can handle handle scenes with millions of triangles. You can reach frame rates of hundreds and thousands of FPS!

[VISUAL] GPU sketch [on "Today's"]
[VISUAL] GPU goes to corner and fades out, cube scene again with FPS counter [on "frame rates" additive]

But, in most cases, this method does not render realistic effects. Heavy shaders are required to create realistic images.

[VISUAL] Weighing scale, glsl logo falls onto the left, then `.node_modules` falls onto the right and outweighs glsl, boom [on "Heavy" additive]

That's where raytracing comes in. It mimics the way light behaves in real life.

[VISUAL] Ray tracing scene where a single green ray emerges from a light, bounces off a sphere and reaches the camera [on "That's"]

If you think of it, doing it this way is quite inefficient. I mean, most of the rays won't even hit the camera! That's just so wasteful.

[VISUAL] Many randomly shot red rays not reaching the camera [on "hit" additive]

We only need to consider the rays that will hit the camera. Some nerds thought about this and said, "Hey, why don't we do it backwards?"

[VISUAL] Doing it backwards [on "backwards?]

This is kind of against our initial idea of mimicking the way light behaves in real life, but we're gonna run this on a potato, so let's stick to it anyway.

[VISUAL] Potato go boom [on "potato"]
