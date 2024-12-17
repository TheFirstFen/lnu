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

```Python

import numpy as np
import matplotlib.pyplot as plt

def rotate(point, angle):
    radians = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(radians), -np.sin(radians)],
        [np.sin(radians), np.cos(radians)]
    ])
    return np.dot(rotation_matrix, point)
    
house = np.array([
    [2, 1],
    [2, 2],
    [2.5, 2.5],
    [3, 2],
    [3, 1],
    [2, 1],
    [2, 2],
    [3, 2]
])

rotation_angle = 45 
translation_vector = np.array([3, 1])

transformed_house = []

for point in house:
    translated = point + translation_vector
    rotated = rotate(translated, rotation_angle)
    transformed_house.append(rotated)
    print(f"Original Point: {point}, Translated Point: {translated}, Rotated Point: {rotated}")

transformed_house = np.array(transformed_house)

plt.figure(figsize=(8, 8))
plt.axis('equal')

plt.plot(house[:, 0], house[:, 1], label="Original House", linestyle='--', marker='o')

plt.plot(transformed_house[:, 0], transformed_house[:, 1], label="Transformed House", marker='o')

plt.title("House Transformation: Translation + Rotation")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.grid()
plt.show()


```

![picture of translation and rotation](./Task2.png)

### Task 3a

For each triangle in the mesh there must be a set of data that correspondes to that triangle, more data storage is requierd. Each triangle is treated individualy so the data needs to be indexed.

### Task 3b

The data that needs to be uploaded to the GPU will be increased and the fragment shader might use the data directly.

### Task 4a

### Task 4b

### Task 4c

### Task 5a

The two crutial transformation are view - and projection transformation.

#### part 5b

View transformation works by first placing a camera in the 3D space at some coordinates with a given direction. Then converting all object from a global coordinate system to a local one with the camera as origo.

Projection transformation mapps 3D coordinates to a 2D plane and to create a sense of depth in the 2D plane a projection matrix is used.
