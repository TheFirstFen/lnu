# 2DT904 : Lab 3 : [Samuel Berg(sb224sc)](mailto:sb224sc.student.lnu.se)

# Lab 3 - Vertex transformations
In this lab you will:
1. Pass in transformation matrices to the vertex shader.
2. Learn how to apply transformations to vertices in the vertex shader
3. Perform time-based animations. Both in the vertex shader and by setting the model matrix
4. Draw multiple instances of a single object
5. Introduce some randomness to the vertex transformations

## 1. TRANSFORMATIONS - Code along
1. Get familiar with the boilerplate
    * The Matrix-class
    * The Program-class
    * Separate files for the shaders   
    * The app that now takes two function parameters. An `init` function, and an `update` function
2. Test various model matrices
3. Setup the projection-view matrix, simulating a camera

## 2. ANIMATION - Code along
1. Update the mModel matrix on each update
2. Add a call to `glClear` to clear the framebuffer between draws
2. Pass the time directly to the vertex shader for "procedural" animation

## 3. INSTANCING - Code along
1. Replace the `glDrawArrays` call with `glDrawArraysInstanced`
2. Use the special variable `gl_InstanceID` to get different values for different instances in the vertex shader
    * We will at least have to separate them spatially, so that they instance at separate locations
3. Use a pseudo-random generator to introduce variations
    ```glsl
    float rand(vec2 co)
    {
        return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
    }
    ```
4. Change the color

## 4. PARTICLE SYSTEM - Try yourself

**Things to try to tweak**
1. Add a lot of instances
2. Apply random rotation to each instance
    * For this, you need to perform the rotation-transformation in the vertex-shader
    * You need to create your own rotation matrixes. Here is one example:
        ```glsl
        mat3 rotZ(float angle) {
          float s = sin(angle);
          float c = cos(angle);

          return mat3(
            c, 0.0, -s,
            0.0, 1.0, 0.0,
            s, 0.0, c
          );
        }
        ```
3. Have the instances move with time in a certain trajectory
4. Have the color change with time. Maybe dim the colors so that they "dissappear" after some time
4. Apply some randomness to the speed that they move
5. Try to get some variation to their trajectories

**Things to try to create**
* Make the particles fall like rain in the same general direction (down)
* Have the particles shoot out radially
  * In a plane
  * I a sphere
  * In a half-sphere
* Have the particles first shoot up, then fall down as if affected by gravity.
* User your own imagination
