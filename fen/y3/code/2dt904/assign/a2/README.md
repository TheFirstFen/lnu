# 2DT904 : Assignment 2 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

## Rasterization

$$
x_{\text{clip}} = 2 \cdot \left( \frac{x_{\text{viewport}}}{\text{width}} \right) - 1, \quad y_{\text{clip}} = 1 - 2 \cdot \left( \frac{y_{\text{viewport}}}{\text{height}} \right)
$$

$$
x_{\text{clip}} = 2 \cdot \left( \frac{2}{8} \right) - 1 = -0.5, \quad y_{\text{clip}} = 1 - 2 \cdot \left( \frac{5}{8} \right) = 1 - 1.25 = -0.25
$$

$$
E(x, y) = (y_2 - y_1)(x - x_1) - (x_2 - x_1)(y - y_1)
$$

$$
E_{12} = (0.6 - 1)(-0.5 - (-0.8)) - (0.9 - (-0.8))(-0.25 - 1) = (-0.4)(0.3) - (1.7)(-1.25) = -0.12 + 2.125 = 2.005
$$

$$
E_{23} = (-1 - 0.6)(-0.5 - 0.9) - (-0.2 - 0.9)(-0.25 - 0.6) = (-1.6)(-1.4) - (-1.1)(-0.85) = 2.24 - 0.935 = 1.305
$$

$$
E_{31} = (1 - (-1))(-0.5 - (-0.2)) - (-0.8 - (-0.2))(-0.25 - (-1)) = (2)(-0.3) - (-0.6)(0.75) = -0.6 + 0.45 = -0.15
$$

$$
E_{12} = 2.005 \quad (\text{positive}), \quad E_{23} = 1.305 \quad (\text{positive}), \quad E_{31} = -0.15 \quad (\text{negative})
$$

$$
\quad \text{Since} \quad E_{31} \quad \text{is negative, the pixel} \quad (−0.5,−0.25) \quad \text{lies **outside** the triangle.}
$$

## Interpolation

$$
x_{\text{clip}} = 2 \cdot \left( \frac{x_{\text{viewport}}}{\text{width}} \right) - 1, \quad y_{\text{clip}} = 1 - 2 \cdot \left( \frac{y_{\text{viewport}}}{\text{height}} \right)
$$

For \( (x_{\text{viewport}}, y_{\text{viewport}}) = (2, 5) \), we get:
$$
x_{\text{clip}} = 2 \cdot \left( \frac{2}{8} \right) - 1 = -0.5, \quad y_{\text{clip}} = 1 - 2 \cdot \left( \frac{5}{8} \right) = 1 - 1.25 = -0.25
$$
Thus, the pixel’s center in clip space is \( (-0.5, -0.25) \).

$$
A_{\text{total}} = \frac{1}{2} \left| x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \right|
$$

For \( V_1 = (-0.8, 1), V_2 = (0.9, 0.6), V_3 = (-0.2, -1) \):
$$
A_{\text{total}} = \frac{1}{2} \left| (-0.8)(0.6 - (-1)) + 0.9((-1) - 1) + (-0.2)(1 - 0.6) \right|
$$
Simplify:
$$
A_{\text{total}} = \frac{1}{2} \left| (-0.8)(1.6) + 0.9(-2) + (-0.2)(0.4) \right|
$$
$$
A_{\text{total}} = \frac{1}{2} \left| -1.28 - 1.8 - 0.08 \right| = \frac{1}{2} \left| -3.16 \right| = 1.58
$$
$$
A_{P, V_2, V_3} = \frac{1}{2} \left| (-0.5)(0.6 - (-1)) + 0.9((-1) - (-0.25)) + (-0.2)((-0.25) - 0.6) \right|
$$
Simplify:
$$
A_{P, V_2, V_3} = \frac{1}{2} \left| (-0.5)(1.6) + 0.9(-0.75) + (-0.2)(-0.85) \right|
$$
$$
A_{P, V_2, V_3} = \frac{1}{2} \left| -0.8 - 0.675 + 0.17 \right| = \frac{1}{2} \left| -1.305 \right| = 0.6525
$$
Thus:
$$
\alpha = \frac{A_{P, V_2, V_3}}{A_{\text{total}}} = \frac{0.6525}{1.58} \approx 0.41
$$
$$
A_{V_1, P, V_3} = \frac{1}{2} \left| (-0.8)((-0.25) - (-1)) + (-0.5)((-1) - 1) + (-0.2)(1 - (-0.25)) \right|
$$
Simplify:
$$
A_{V_1, P, V_3} = \frac{1}{2} \left| (-0.8)(0.75) + (-0.5)(-2) + (-0.2)(0.4) \right|
$$
$$
A_{V_1, P, V_3} = \frac{1}{2} \left| -0.6 + 1.0 - 0.25 \right| = \frac{1}{2} \left| 0.15 \right| = 0.075
$$
Thus:
$$
\beta = \frac{A_{V_1, P, V_3}}{A_{\text{total}}} = \frac{0.075}{1.58} \approx 0.05
$$
$$
A_{V_1, V_2, P} = \frac{1}{2} \left| (-0.8)(0.6 - (-0.25)) + 0.9((-0.25) - 1) + (-0.5)(1 - 0.6) \right|
$$
Simplify:
$$
A_{V_1, V_2, P} = \frac{1}{2} \left| (-0.8)(0.85) + 0.9(-1.25) + (-0.5)(0.4) \right|
$$
$$
A_{V_1, V_2, P} = \frac{1}{2} \left| -0.68 - 1.125 - 0.2 \right| = \frac{1}{2} \left| -2.005 \right| = 1.0025
$$
Thus:
$$
\gamma = \frac{A_{V_1, V_2, P}}{A_{\text{total}}} = \frac{1.0025}{1.58} \approx 0.63
$$
$$
C = \alpha C_1 + \beta C_2 + \gamma C_3
$$

Substitute the vertex colors:
$$
C = 0.41 (1, 1, 1) + 0.05 (0, 0, 0) + 0.63 (0.3, 0.3, 1.0)
$$
Simplify each component:
$$
C_x = 0.41(1) + 0.05(0) + 0.63(0.3) = 0.41 + 0 + 0.189 = 0.60
$$
$$
C_y = 0.41(1) + 0.05(0) + 0.63(0.3) = 0.41 + 0 + 0.189 = 0.60
$$
$$
C_z = 0.41(1) + 0.05(0) + 0.63(1.0) = 0.41 + 0 + 0.63 = 1.04 \approx 1.0
$$

Thus, the interpolated color is:
$$
C = (0.60, 0.60, 1.0)
$$


