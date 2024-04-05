package com.sb224sc.rubik.model;

import javafx.scene.paint.Color;
import javafx.scene.transform.Rotate;
import javafx.geometry.Point3D;

import java.util.*;

public class FaceSystem {
    private Color topFace = Face.Faces.TOP.getColor();
    private Color bottomFace = Face.Faces.BOTTOM.getColor();
    private Color frontFace = Face.Faces.FRONT.getColor();
    private Color backFace = Face.Faces.BACK.getColor();
    private Color rightFace = Face.Faces.RIGHT.getColor();
    private Color leftFace = Face.Faces.LEFT.getColor();

    /**
     * Rotates the object around the specified axis by the given amount.
     *
     * @param amount the amount to rotate the object (in degrees)
     * @param axis   the axis around which to rotate the object
     * @throws IllegalArgumentException if the axis is invalid
     */
    public void rotate(int amount, Point3D axis) {
        if (Math.abs(axis.getX()) == Rotate.X_AXIS.getX()) {
            Color[] faces = shiftArray(new Color[] { frontFace, topFace, backFace, bottomFace },
                    amount * (int) axis.getX());
            frontFace = faces[0];
            topFace = faces[1];
            backFace = faces[2];
            bottomFace = faces[3];
        } else if (Math.abs(axis.getY()) == Rotate.Y_AXIS.getY()) {
            Color[] faces = shiftArray(new Color[] { frontFace, rightFace, backFace, leftFace },
                    amount * (int) axis.getY());
            frontFace = faces[0];
            rightFace = faces[1];
            backFace = faces[2];
            leftFace = faces[3];
        } else if (Math.abs(axis.getZ()) == Rotate.Z_AXIS.getZ()) {
            Color[] faces = shiftArray(new Color[] { topFace, rightFace, bottomFace, leftFace },
                    amount * (int) axis.getZ());
            topFace = faces[0];
            rightFace = faces[1];
            bottomFace = faces[2];
            leftFace = faces[3];
        } else {
            throw new IllegalArgumentException("Invalid axis: " + axis);
        }
    }

    /**
     * Shifts the elements of the given array by the specified amount.
     *
     * @param array  the array to be shifted
     * @param amount the number of positions the elements should be shifted
     * @return the shifted array
     */
    private static Color[] shiftArray(Color[] array, int amount) {
        List<Color> temp = Arrays.asList(array);
        Collections.rotate(temp, amount);
        return temp.toArray(new Color[array.length]);

    }

    /**
     * Returns the color of the top face of the object.
     *
     * @return the color of the top face
     */
    public Color getTopFace() {
        return this.topFace;
    }

    /**
     * Retrieves the color of the bottom face.
     *
     * @return the color of the bottom face
     */
    public Color getBottomFace() {
        return this.bottomFace;
    }

    /**
     * Retrieves the value of the frontFace property.
     *
     * @return the frontFace property
     */
    public Color getFrontFace() {
        return this.frontFace;
    }

    /**
     * Retrieves the back face color.
     *
     * @return the back face color
     */
    public Color getBackFace() {
        return this.backFace;
    }

    /**
     * Gets the color of the right face.
     *
     * @return the color of the right face
     */
    public Color getRightFace() {
        return this.rightFace;
    }

    /**
     * Retrieves the color of the left face.
     *
     * @return the color of the left face
     */
    public Color getLeftFace() {
        return this.leftFace;
    }

    /**
     * A function that takes a color and returns a string representation of the
     * color.
     *
     * @param color the color to be converted to a string
     * @return the string representation of the color, or null if the color is not
     *         recognized
     */
    public static String printColor(Color color) {
        if (color == Color.WHITE)
            return "WHITE";
        if (color == Color.ORANGE)
            return "ORANGE";
        if (color == Color.RED)
            return "RED";
        if (color == Color.GREEN)
            return "GREEN";
        if (color == Color.YELLOW)
            return "YELLOW";
        if (color == Color.BLUE)
            return "BLUE";
        else
            return null;
    }

    /**
     * Returns a string representation of the object. The string representation
     * consists of the values of the top,
     * bottom, front, right, back, and left faces of a cube, formatted as "top:
     * {color} bottom: {color} front: {color}
     * right: {color} back: {color} left: {color}". The {color} placeholder is
     * replaced with the color of the
     * respective face.
     *
     * @return a string representation of the object
     */
    @Override
    public String toString() {
        return String.format("top: %s bottom: %s front: %s right: %s back: %s left: %s", printColor(topFace),
                printColor(bottomFace), printColor(frontFace), printColor(rightFace), printColor(backFace),
                printColor(leftFace));
    }
}
