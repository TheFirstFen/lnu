# Assignment 2 2DT904

## Emil Ulvagården (<eu222dq@student.lnu.se>)

### Task 1

My point is (4,5) witch gives the following

$$
Xp = 4.5 \\
Yp = 5.5
$$

When converging the points v1, v2 and v3 to the (0,0) -> (8,8) coordinate system they gain the new points.

$$
v1 =(0.8, 0)\\
v2 = (7.2, 1.6)\\
v3 = (3.2, 8)
$$

Using the following formulas to calculate the clip space coordinates:

$$
Xc = \frac{2Xp}{W} - 1\\
Yc = 1 - \frac{2Yp}{h}
$$

The edge function is:

$$
E{ij} = (yj-yi)(x-xi) - (xj-xi)(y-yi)
$$

$$
E_{12} = (1.6-0)(4.5-0.8) - (7.2-0.8)(5.5-0) = \\
1.6\cdot3.7 - 6.4 =\\
5.92

$$
