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

We're gonna be dipping our toes into the vast sea of raytracing today. We will render a solid sphere on a solid skybox, and perhaps deal with multiple spheres too.
We will do this in a way completely different to rasterization. We will shoot rays out of our camera for every pixel on the screen, and see if they hit the sphere. 
If they do, the color of that pixel is the color of the sphere. Else, its color is that of the skybox.

[VISUAL] The old python scene being all wavy

Let's get on with the code, shall we?

[VISUAL] do the code scenes from this line

First, let's create a basic Ray class, as it is the most important part of our engine.
Let's name this file vectors.py, as there will be more useful definitions made here.
First, let's define some 2d and 3d vector datatypes. Then, we define the ray class.
The ray has an origin and a direction. Let's also create a color class. It stores RGB color values.
Finally, we need some way to easily normalize a 3d vector. Let's create a function for that.

Now, let's create the hittable class for the object we want to render.
In the models directory, let's create sphere.py, which contains the intersection code for the humble sphere.
The sphere has a center, a radius and a color. 
The color parameter is temporary, and will be removed in later versions in favour of materials.
For the intersection function, we first need to calculate some parameters for the quadratic equation.
Then, we calculate the discriminant of the quadratic equation.
Then, if the ray hits the sphere, return the solution to the equation. Else return -1.
I've written non-branching code, because I want to squeeze every last drop of optimization I can out of my code.
The code, however, is heavily commented and easy to read, so even newbies can follow along.

Next, we need to create a camera class which handles the camera position, rotation, and provides a function to
easily get the rays for a particular pixel on the screen.
The camera has a resolution, position, rotation, field of view, and dither.

(off-screen far-away voice) What's dither?

Wait for it, we'll get to it in a moment. For now, dithering adds a bit of randomness so that each ray for the
same pixel does not go through the same path.
The get_ray function takes pixel coordinates and returns the ray for that pixel.
First, we calculate the aspect ratio and normalized screen coordinates.
Then, we calculate the screen coordinates, calculate the direction vector,
add the dither or randomness to the direction, calculate the rotation matrix,
apply the rotation to the direction, normalize the direction, and return the ray. Phew!

Now that we have made the 3 major parts of the engine, let's put it all together in scene.py
