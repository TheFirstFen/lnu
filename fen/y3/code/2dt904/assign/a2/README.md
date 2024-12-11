# 2DT904 : Assignment 2 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

## Rasterization

$$
x_{\text{clip}} = 2 \cdot \left( \frac{x_{\text{vp}}}{\text{width}} \right) - 1, \quad y_{\text{clip}} = 1 - 2 \cdot \left( \frac{y_{\text{vp}}}{\text{height}} \right)
$$

$$
x_{\text{clip}} = 2 \cdot \left( \frac{2}{8} \right) - 1 = -0.5, \quad y_{\text{clip}} = 1 - 2 \cdot \left( \frac{5}{8} \right) = 1 - 1.25 = -0.25
$$

$$
E(x, y) = (y_2 - y_1)(x - x_1) - (x_2 - x_1)(y - y_1)
$$

$$
E_{12} = (0.6 - 1)(-0.5 - (-0.8)) - (0.9 - (-0.8))(-0.25 - 1)
$$

$$
E_{12} = (-0.4)(0.3) - (1.7)(-1.25) \\
E_{12} = -0.12 + 2.125 = 2.005
$$

$$
E_{23} = (-1 - 0.6)(-0.5 - 0.9) - (-0.2 - 0.9)(-0.25 - 0.6)
$$

$$
E_{23} = (-1.6)(-1.4) - (-1.1)(-0.85) \\
E_{23} = 2.24 - 0.935 = 1.305
$$

$$
E_{31} = (1 - (-1))(-0.5 - (-0.2)) - (-0.8 - (-0.2))(-0.25 - (-1))
$$

$$
E_{31} = (2)(-0.3) - (-0.6)(0.75) \\
E_{31} = -0.6 + 0.45 = -0.15
$$

$$
E_{12} = 2.005 \quad (\text{positive}), \quad E_{23} = 1.305 \quad (\text{positive}), \quad E_{31} = -0.15 \quad (\text{negative})
$$

$$
\quad \text{Since} \quad E_{31} \quad \text{is negative, the pixel} \quad (−0.5,−0.25) \quad \text{lies **outside** the triangle.}
$$
