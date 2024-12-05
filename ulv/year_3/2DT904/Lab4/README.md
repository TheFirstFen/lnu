# Lab 4 - Hidden surfaces and fragment shading

In this lab you will:

1. See the effect of hidden surface removal
2. Explore various ways in which we can use maths to draw in the fragment shader

## 1. HIDDEN SURFACE REMOVAL - Code along

1. Run `1-hidden-surfaces.py` to see the problem
    * Press `space` to pause the animation to try to figure out how I can look the way it does
2. Enable `back-face culling`
3. Move the section labeled "draw cube far away" to after "draw cube near"
4. Enable checking against the z-buffer, so called `depth testing`

## 2. FRAGMENT SHADER - Code along

1. Use the files `2-fragment-shading*`
2. Examine the `setupSquare` function. Each vertex has an extra 2d-coordinate attribute. Take some minutes and try to figure out how they are layed out, and what the purpose of those coordinates are. Remember that they are vertex attributes, and will thus be interpolated for each pixel in the square.
3. Some tools for programming fragment shaders
    * `gl_FragCoord` contains screen-space coordinates for the current pixel
    * `mix()` for linear interpolation
    * `step()` and `smoothStep()`
    * We can subdivide the space by scaling the uvs and than taking the fractional part using `fract()`
4. `The book of shaders`
    * [https://thebookofshaders.com/]
    * Have a look at the section "Algorithmic drawing"

## 3. FRAGMENT SHADER - Try yourself

1. Try to draw a swedish flag
    * Change to a danish flag by changing the colors
    * Try animating between them using `mix` and some periodic function like sine or cosine
