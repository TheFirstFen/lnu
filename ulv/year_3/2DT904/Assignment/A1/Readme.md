# Assignment 1 2DT904

## Emil Ulvagården (<eu222dq@student.lnu.se>)

### Task 1a

$$ p = \begin{bmatrix}
10\\
15\\
2\\
1\\
\end{bmatrix}
$$

$$ T(1,2,3) = \begin{bmatrix}
1 & 0 & 0 & 1\\
0 & 1 & 0 & 2\\
0 & 0 & 1 & 3\\
0 & 0 & 0 & 1\\
\end{bmatrix} $$

$$ pt =T(1,2,3)p = \begin{bmatrix}
1 & 0 & 0 & 1\\
0 & 1 & 0 & 2\\
0 & 0 & 1 & 3\\
0 & 0 & 0 & 1\\
\end{bmatrix}

\begin{bmatrix}
10\\
15\\
2\\
1\\
\end{bmatrix}
$$

$$ pt = \begin{bmatrix}
1*10 + 0*15 + 0*2 + 1*1\\
0*10 + 1*15 + 0*2 + 2*1\\
0*10 + 0*15 + 1*2 + 3*1\\
0*10 + 0*15 + 0*2 + 1*1\\
\end{bmatrix}

= \begin{bmatrix}
11\\
17\\
5\\
1\\
\end{bmatrix}
$$

$$ pt = \begin{bmatrix}
11\\
17\\
5\\
1\\
\end{bmatrix}
$$

### Task 1b

$$ R(30^\circ) = \begin{bmatrix}
cosθ & 0 & sinθ & 0\\
0 & ​1 & 0 & 0\\
-sinθ & 0 & cosθ & 0\\
​0 & 0& 0 & 1​\\
\end{bmatrix}
$$

$$ cos(30^\circ) = \sqrt{3}/2 $$
$$ sin(30^\circ) = 1/2 $$

$$ Pr =R(30^\circ)p = \begin{bmatrix}
\sqrt{3}/2 & 0 & 1/2 & 0\\
0 & ​1 & 0 & 0\\
-1/2 & 0 & \sqrt{3}/2 & 0\\
​0 & 0 & 0 & 1​\\
\end{bmatrix}

\begin{bmatrix}
10\\
15\\
2\\
1\\
\end{bmatrix}
$$

$$ Pr = \begin{bmatrix}
((\sqrt{3}/2) * 10) + 0*15 + (1/2)*2 + 0*1\\
0*10 + 1*15 + 0*2 + 0*1\\
(-1/2)*10 + 0*15 + (\sqrt{3}/2)*2 + 0*1\\
0*10 + 0*15 + 0*2 + 1*1\\
\end{bmatrix}
$$

$$ Pr = \begin{bmatrix}
5\sqrt{3} + 1\\
15\\
\sqrt{3} + 5\\
1\\
\end{bmatrix}
$$

### Task 1c

The transformation is devided in three different steps.

Step one is to move the object to the point $T(-10,0,-10)$

Step two is to rotate the object 90 degrees with $R(90^\circ)$

The last step is to translate the object with the matrix $T(10,0,10)$

### Task 2

![picture of translation and rotation](./Task2.png)

### Task 3a

For each triangle in the mesh there must be a set of data that correspondes to that triangle, more data storage is requierd. Each triangle is treated individualy so the data needs to be indexed.

### Task 3b

The data that needs to be uploaded to the GPU will be increased and the fragment shader might use the data directly.

### Task 4a

The Z-buffer works by comparing depth values stored in a buffer and if the new data is closer to the camera it replaces the existing pixel. The Z-buffer is implemented in the fragment shader during rasterization. The algorithm works on the depth values of the pixels. Limitations for the Z-buffer are when working with transparent objects as it automatically assumes that closer objects obscure objects farther away.

### Task 4b

Frustum culling works by determining if an object is within the cameras viewing. Objects outside the view are considered invisible and not processed further. Frustum culling is implemented at the application level or before sending data to the GPU. The algorithm opperates on the bounding region for a set of objects. Limitation for the frustum culling is that it does not account for objects hidden behind other objects.

### Task 4c

Backface culling works by determening the orientaion of the face and if its determined to face away from the camera its considered invisible and not rendered. Backface culling is implemented in the geometry pipeline before rasterization. The data the algorithm operates on is the orientation of the face and the camera position. Limitation for the backface culling are that it does not work with transparent backfases or objects that needs to be rendered.

### Task 5a

The two crutial transformation are view - and projection transformation.

#### part 5b

View transformation works by first placing a camera in the 3D space at some coordinates with a given direction. Then converting all object from a global coordinate system to a local one with the camera as origo.

Projection transformation mapps 3D coordinates to a 2D plane and to create a sense of depth in the 2D plane a projection matrix is used.
