# 2DT904 : Lab 2 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

# Lab 2 - Providing data to the graphics pipeline
In this lab you will:
1. Learn how to feed vertex data describing an object into the graphics pipeline.
2. Declare inputs and outputs for the vertex and fragment shader
3. Provide runtime constants, a.k.a. `uniforms` to shaders.

## 1. TRIANGLE. Code along - Providing vertex position data to opengl
1. Define the data
2. Describe and provide the data to opengl
3. Create the shader program
3. Declare the input to the vertex shader
4. Tie the data to the vertex shader input
5. Render

## 2. UNIFORM. Code along - Poviding `uniform` data to shaders
1. Continue from the previous exercise.
2. Add a uniform input to the vertex shader
3. Assign a value to the uniform

## 3. COLOR. Try yourself - Provide additional vertex data
1. Continue from the previous exercise
2. Declare an additional input to the vertex shader of type `vec3` called `vertexColor` 
2. Add the following color data for the vertices in the python code
  ```python
    colors = [1.0, 0.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 0.0, 1.0]
  ```
3. Make the data available to the shader following the same pattern as in exercise 1.
4. Make the vertex shader pass the color data on to the fragment shader:
    1. declare an output in the vertex shader like this
    ```glsl
    out vec3 color;
    ```
    1. Assign `vertexColor` to the `color` output variable in the vertex shader main function.
    1. declare a corresponding input in the fragment shader
    ```glsl
    in vec3 color;
    ```
    1. Update the fragment shader to use the `color` input when setting the `fragColor` value.
    ```glsl
    fragColor = vec4(color, 1.0);
    ```

## 4. UNIFORM VECTOR. Try yourself - Provide additional uniform data
1. Continue from the previous exercise
2. Update the `offset` uniform to be of type `vec3` in the vertex shader
3. Update the vertex shader to apply the offset as a vector operation on `position` rather than on the x-coordinate.
4. Update the python code to provide a 3d offset to the uniform instead of a single value
