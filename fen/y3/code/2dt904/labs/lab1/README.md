# 2DT904 : Lab 1 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

## Tasks

# Lab 1 - Setting the stage
In this lab you will:
1. Setup the development environment.
2. Familiar yourself with `PyOpenGL` and `pygame`
3. Create a minimal application that renders an image using openGL


## 1. Setup the development environment
Follow the instructions in the book. Section `1.3 Setting up a development environment`.

### Notes
- Feel free to use `conda`, `venv` or similar to manage your python environment and packages
- If you encounter problems while installing `PyOpenGL_accelerate` you can just ignore that package for now.

## 2. Create a window using `pygame`
Pygame is a package that abstracts away platform specific details related to graphics- and game development. Such as:
  * creating a window
  * setting up the OpenGL context
  * user input

1. Use the code in section 2.1 of the book as a reference, but don't bother about their abstractions. Focus on the minimal code to get the objective done. That is, to display a window using the `pygame` package. 

### Notes
- When you initialize a pygame display with the OPENGL flag, it will automatically create an OpenGL context tied to that window.
- You will need to create a simple event loop in order to keep the application running until the window is closed.

## 3. Render a point with OpenGL
OpenGL is a low level graphics API that allows us to interface with graphics processing units (GPUs) on the local computer and control the `graphics pipeline`. Nearly all of the OpenGL API is about setting up state that affect this pipeline. Once all state is in place, you trigger the entire pipeline by invoking one of the `glDraw*` functions.

`PyOpenGL` is the OpenGL bindings for python. Once you have initialized an opengl window using pygame, all calls to OpenGL functions will affect the OpenGL context tied to that window.

1. Use the code in section 2.2 of the book as a reference to:
  1. Create and compile a vertex shader
  1. Create and compile a fragment shader
  1. Create, link and activate a `program` using the two shaders
  1. Create and bind a so called `vertex array object`
  1. Set the point size
  1. Trigger the entire pipeline by invoking `glDrawArrays`

### Notes
- Since we're not animating anything yet, we only need to draw our image once. That is, triggering the pipeline using `glDrawArrays`. I mention this because the book puts the draw call in a loop. That will only be neccessary once we want to animate stuff.

## 4. Experiment on your own
These are some examples of things you might want continue experimenting with:

* Change the values that are assigned to `gl_Position` and `fragColor` to get an idea of what they do and the valid ranges.
* Investigate how one can use `uniforms` to pass in constant data to the shader at runtime instead of hardcoding them in the shader source (page 65-67 in the book).
  * Once you can pass uniforms to your shaders, you can move the draw call (`glDrawArrays`) to a loop (as in the book) and update the value of the uniform in each iteration to create a simple animation.


