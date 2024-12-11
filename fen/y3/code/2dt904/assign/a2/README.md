# 2DT904 : Assignment 2 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

## 1. Rasterization

We use the edge function to determine if the pixel at viewport coordinate \( (2, 5) \) lies inside the triangle formed by vertices \( V_1, V_2, V_3 \) in clip space.

### Step 1: Convert Viewport to Clip Space

The viewport size is \( 8 \times 8 \), and the conversion to clip space is:
\[
x_{\text{clip}} = 2 \cdot \left( \frac{x_{\text{vp}}}{\text{width}} \right) - 1, \quad y_{\text{clip}} = 1 - 2 \cdot \left( \frac{y_{\text{vp}}}{\text{height}} \right)
\]
Substitute \( (x_{\text{vp}}, y_{\text{vp}}) = (2, 5) \):
\[
x_{\text{clip}} = 2 \cdot \left( \frac{2}{8} \right) - 1 = -0.5, \quad y_{\text{clip}} = 1 - 2 \cdot \left( \frac{5}{8} \right) = -0.25
\]
Thus, the pixel center in clip space is \( (-0.5, -0.25) \).

### Step 2: Edge Function

The edge function between two points \( (x_1, y_1) \) and \( (x_2, y_2) \) for a test point \( (x, y) \) is:
\[
E(x, y) = (y_2 - y_1)(x - x_1) - (x_2 - x_1)(y - y_1)
\]

#### Edge \( V_1 \to V_2 \)
\[
V_1 = (-0.8, 1), \quad V_2 = (0.9, 0.6), \quad P = (-0.5, -0.25)
\]
\[
E_{12} = (0.6 - 1)(-0.5 - (-0.8)) - (0.9 - (-0.8))(-0.25 - 1)
\]
Simplify:
\[
E_{12} = (-0.4)(0.3) - (1.7)(-1.25) = -0.12 + 2.125 = 2.005
\]

#### Edge \( V_2 \to V_3 \)
\[
V_2 = (0.9, 0.6), \quad V_3 = (-0.2, -1), \quad P = (-0.5, -0.25)
\]
\[
E_{23} = (-1 - 0.6)(-0.5 - 0.9) - (-0.2 - 0.9)(-0.25 - 0.6)
\]
Simplify:
\[
E_{23} = (-1.6)(-1.4) - (-1.1)(-0.85) = 2.24 - 0.935 = 1.305
\]

#### Edge \( V_3 \to V_1 \)
\[
V_3 = (-0.2, -1), \quad V_1 = (-0.8, 1), \quad P = (-0.5, -0.25)
\]
\[
E_{31} = (1 - (-1))(-0.5 - (-0.2)) - (-0.8 - (-0.2))(-0.25 - (-1))
\]
Simplify:
\[
E_{31} = (2)(-0.3) - (-0.6)(0.75) = -0.6 + 0.45 = -0.15
\]

### Step 3: Inside Check

The pixel \( (-0.5, -0.25) \) is inside the triangle if all edge functions are non-negative:
\[
E_{12} = 2.005 > 0, \quad E_{23} = 1.305 > 0, \quad E_{31} = -0.15 < 0
\]
Since \( E_{31} < 0 \), the pixel lies **outside** the triangle and will not be processed for shading.

