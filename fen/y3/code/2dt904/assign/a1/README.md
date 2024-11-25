# 2DT904 : Assignment 1 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

### **Question 1: Transformations I**

**Given:**
- \( R_y \): 4x4 homogeneous rotation matrix around the Y-axis.  
- \( T(x, y, z) \): 4x4 homogeneous translation matrix.  
- \( p = \begin{bmatrix} 10 \\ 15 \\ 2 \\ 1 \end{bmatrix} \): Homogeneous 3D point.

#### **a. Calculate \( p_t = T(1, 2, 3)p \).**
Using the translation matrix \( T(x, y, z) \):
\[
T(1, 2, 3) = \begin{bmatrix}
1 & 0 & 0 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 3 \\
0 & 0 & 0 & 1
\end{bmatrix}
\]

Calculate \( p_t \):
\[
p_t = T(1, 2, 3) \cdot p = 
\begin{bmatrix}
1 & 0 & 0 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 3 \\
0 & 0 & 0 & 1
\end{bmatrix}
\cdot 
\begin{bmatrix}
10 \\ 15 \\ 2 \\ 1
\end{bmatrix}
= 
\begin{bmatrix}
11 \\ 17 \\ 5 \\ 1
\end{bmatrix}
\]

**Answer: \( p_t = \begin{bmatrix} 11 \\ 17 \\ 5 \\ 1 \end{bmatrix} \)**

#### **b. Calculate \( p_r = R_y(30^\circ)p \).**
The rotation matrix \( R_y(\theta) \):
\[
R_y(30^\circ) = 
\begin{bmatrix}
\cos(30^\circ) & 0 & \sin(30^\circ) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(30^\circ) & 0 & \cos(30^\circ) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
= 
\begin{bmatrix}
\sqrt{3}/2 & 0 & 1/2 & 0 \\
0 & 1 & 0 & 0 \\
-1/2 & 0 & \sqrt{3}/2 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\]

Calculate \( p_r \):
\[
p_r = R_y(30^\circ) \cdot p = 
\begin{bmatrix}
\sqrt{3}/2 & 0 & 1/2 & 0 \\
0 & 1 & 0 & 0 \\
-1/2 & 0 & \sqrt{3}/2 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\cdot 
\begin{bmatrix}
10 \\ 15 \\ 2 \\ 1
\end{bmatrix}
= 
\begin{bmatrix}
5\sqrt{3} + 1 \\ 15 \\ -5 + 2\sqrt{3} \\ 1
\end{bmatrix}
\]

**Answer:**  
\( p_r = \begin{bmatrix} 5\sqrt{3} + 1 \\ 15 \\ -5 + 2\sqrt{3} \\ 1 \end{bmatrix} \)

#### **c. Effect of \( T(10, 0, 10)R_y(90^\circ)T(-10, 0, -10) \)**
1. **Translation \( T(-10, 0, -10) \):** Moves the object to position \((-10, 0, -10)\).
2. **Rotation \( R_y(90^\circ) \):** Rotates the object 90° around the Y-axis.
3. **Translation \( T(10, 0, 10) \):** Moves the object back to position \((10, 0, 10)\).

**Effect:**  
The transformation applies a 90° rotation around the Y-axis about the point \((10, 0, 10)\).

---

### **Question 2: Transformations II**

**Apply \( R(45^\circ)T(3, 1) \) on the house drawing.**  

- **Translation \( T(3, 1) \):** Moves the house 3 units right and 1 unit up.
- **Rotation \( R(45^\circ) \):** Rotates the house 45° counterclockwise around the origin.

**Drawing:** *(Upload a sketch showing the transformed house.)*

---

### **Question 3: Per-triangle data**

#### **a. Implications for the host data structure of the mesh:**
- Data must explicitly store triangles instead of shared vertices.  
- Each triangle may duplicate vertex information, increasing memory usage.

#### **b. Data to upload to the GPU:**
- The GPU requires all vertex data for each triangle, including normals and texture coordinates.  
- This increases bandwidth requirements compared to per-vertex data.

---

### **Question 4: Visibility determination**

#### **a. Z-buffer**
- **How it works:** Tracks depth for each pixel in a frame buffer. A pixel is updated only if the new fragment is closer.  
- **Pipeline location:** Rasterization stage.  
- **Data:** Depth values.  
- **Limitations:** Doesn’t resolve transparency.

#### **b. Frustum culling**
- **How it works:** Discards objects outside the camera’s view frustum.  
- **Pipeline location:** Before rasterization.  
- **Data:** Bounding boxes.  
- **Limitations:** May cull objects partially visible.

#### **c. Backface culling**
- **How it works:** Removes triangles facing away from the camera by checking normal direction.  
- **Pipeline location:** Before fragment shading.  
- **Data:** Triangle normals.  
- **Limitations:** Doesn’t work for transparent objects.

---

### **Question 5: Mapping to pixels**

#### **a. Two crucial transformations:**
1. **View transformation**  
2. **Projection transformation**

#### **b. Explanation of transformations:**
1. **View transformation:** Aligns the 3D world to the camera’s coordinate system.  
2. **Projection transformation:** Maps 3D points to a 2D plane, converting depth into a scalar value.

---

