# quickHull.py
#
# Author: Samuel Berg
# Date: 10-Sep-2019

from math import sqrt

def quickHull(v):
    """
    Calculate the convex hull of a set of vertices v that

    :param v: set of coordinates (x, y) where x and y are floats

    :return: set of coordinates (x, y) that are the nodes of the convex hull
    """
    if len(v) <= 2:
        return v
    
    convex_hull = []

    # find the maximum and minimum points on the x-axis
    sort = sorted(v, key = lambda x: x[0])
    p1 = sort[0]
    p2 = sort[-1]

    convex_hull = convex_hull + [p1, p2]

    # remove from the list as they are now in the convex hull
    sort.pop(0)
    sort.pop(-1)

    # determine points above and below the line
    above, below = create_segment(p1, p2, sort)
    convex_hull = convex_hull + quickHull2(p1, p2, above, "above")
    convex_hull = convex_hull + quickHull2(p1, p2, below, "below")

    return convex_hull

def quickHull2(p1, p2, segment, flag):
    """..."""
    # exit case for the recursion
    if segment == [] or p1 is None or p2 in None:
        return []

    convex_hull = []

    # calculate the distance of every point from the line to find the farthest point
    farthest_distance = -1
    farthest_point = None
    for point in segment:
        distance = find_distance(p1, p2, point)
        if distance > farthest_distance:
            farthest_distance = distance
            farthest_point = point

    convex_hull = convex_hull + [farthest_point]

    # point is now in the convex hull so remove it from segment
    segment.remove(farthest_point)

    # determine the segments formed from the two lines p1-farthest_point and p2-farthest_point
    point1above, point1below = create_segment(p1, farthest_point, segment)
    point2above, point2below = create_segment(p2, farthest_point, segment)

    # only use the segments in the same direction, the opposite direction is contained in the convex hull
    if flag == "above":
        convex_hull = convex_hull + quickHull2(p1, farthest_point, point1above, "above")
        convex_hull = convex_hull + quickHull2(farthest_point, p2, point2above, "above")
    else:
        convex_hull = convex_hull + quickHull2(p1, farthest_point, point1below, "below")
        convex_hull = convex_hull + quickHull2(farthest_point, p2, point2below, "below")

    return convex_hull

def create_segment(p1, p2, v):
    """
    Segment a set of coordinates to be below a line p1-p2

    :param p1: first coordinate on the line
    :param p2: second coordinate on the line
    :param v: list of coordinates represented by tuples (x, y)

    :return: list of coordinates above the line, list of coordinates below the line
    """

    above = []
    below = []

    # list vertical so there are no points above or below it
    if p2[0] - p1[0] == 0:
        return above, below

    # calculate m and c from y = mx + c
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = - m * p1[0] + p1[1]

    # loop through each coordinate and place it into the correct list
    for coordinate in v:
        # y > mx + c means it is above the line
        if coordinate[1] > m * (coordinate[0]) + c:
            above.append(coordinate)
        # y < mx + c means it is below the line
        elif coordinate[1] < m * (coordinate[0]) + c:
            below.append(coordinate)
        
    return above, below

def find_distance(p1, p2, p3):
    """
    Find the distance between a line p1-p2 and a point p3

    :param p1: the first coordinate on the line
    :param p2: the second coordinate on the line
    :param p3: the point to mesure the distance from

    :return: the distance between the line and the point
    """

    # using the formula ax + by + c = 0
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = p1[0] * p2[1] - p2[0] * p1[1]

    # using dot product to find distance between a line and a point
    return abs(a * p3[0] + b * p3[1] + c) / sqrt(a * a + b * b)
