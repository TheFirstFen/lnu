package com.sb224sc.rubik.model;

import javafx.scene.shape.Box;
import javafx.scene.Group;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.paint.Color;
import javafx.scene.transform.Rotate;
import javafx.geometry.Point3D;

import java.util.*;

public class InnerCube {
    private static int identity = 0;

    public static class ViewCoords {
        private Cube cube;
        private double viewX;
        private double viewY;
        private double viewZ;

        public ViewCoords(Cube cube, double x, double y, double z) {
            this.cube = cube;
            this.viewX = x;
            this.viewY = y;
            this.viewZ = z;
        }

        /**
         * Sets up the view for the 3D graphics.
         */
        public void setup() {
            double rx = Math.toRadians(0);
            double ry = Math.toRadians(cube.posY * 90.0);
            double rz = Math.toRadians(0);

            viewX -= 1;
            viewY -= 1;
            viewZ -= 1;

            // Rotate along x axis
            double x1;
            double y1;
            double z1;

            x1 = viewX;
            y1 = viewY * Math.cos(rx) - viewZ * Math.sin(rx);
            z1 = viewY * Math.sin(rx) + viewZ * Math.cos(rx);

            // Rotate along y axis
            double x2;
            double y2;
            double z2;

            x2 = x1 * Math.cos(ry) + z1 * Math.sin(ry);
            y2 = y1;
            z2 = z1 * Math.cos(ry) - x1 * Math.sin(ry);

            // Rotate along z axis
            double x3;
            double y3;
            double z3;

            x3 = x2 * Math.cos(rz) - y2 * Math.sin(rz);
            y3 = x2 * Math.sin(rz) + y2 * Math.cos(rz);
            z3 = z2;

            this.viewX = x3 + 1;
            this.viewY = y3 + 1;
            this.viewZ = z3 + 1;
        }

        /**
         * Retrieves the value of X.
         *
         * @return the rounded value of viewX as an integer
         */
        public int getX() {
            return (int) Math.round(this.viewX);
        }

        /**
         * Returns the rounded value of the viewY variable as an integer.
         *
         * @return the rounded value of the viewY variable as an integer
         */
        public int getY() {
            return (int) Math.round(this.viewY);
        }

        /**
         * Get the value of Z.
         *
         * @return the rounded value of the viewZ variable as an integer
         */
        public int getZ() {
            return (int) Math.round(this.viewZ);
        }

        /**
         * Returns a string representation of the object.
         *
         * @return a string representation of the object
         */
        @Override
        public String toString() {
            return "View coords: " + getX() + " " + getY() + " " + getZ();
        }
    }

    public int x;
    public int y;
    public int z;
    private int startX;
    private int startY;
    private int startZ;
    public Double relX;
    public Double relY;
    private Face[] faces = new Face[6];
    private List<Face.Faces> invisibleFaces = new ArrayList<>();
    private Group model;
    private int id;
    public Point3D xAxis = new Point3D(1, 0, 0);
    public Point3D yAxis = new Point3D(0, 1, 0);
    public Point3D zAxis = new Point3D(0, 0, 1);
    private FaceSystem faceSystem = new FaceSystem();

    public InnerCube(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.startX = x * 100;
        this.startY = y * 100;
        this.startZ = z * 100;
        this.id = InnerCube.identity++;
        for (int i = 0; i < 6; i++) {
            this.faces[i] = new Face(Face.Faces.values()[i]);
        }
    }

    /**
     * Returns the startX value.
     *
     * @return the startX value
     */
    public int getStartX() {
        return this.startX;
    }

    /**
     * Retrieves the value of the startY variable.
     *
     * @return the value of the startY variable
     */
    public int getStartY() {
        return this.startY;
    }

    /**
     * Retrieves the value of the startZ variable.
     *
     * @return the value of the startZ variable
     */
    public int getStartZ() {
        return this.startZ;
    }

    /**
     * Retrieves the FaceSystem object.
     *
     * @return the FaceSystem object
     */
    public FaceSystem getFaceSystem() {
        return this.faceSystem;
    }

    /**
     * Generates the ViewCoords object for the given Cube object.
     *
     * @param cube the Cube object for which to generate the ViewCoords
     * @return the generated ViewCoords object
     */
    public ViewCoords getViewCoords(Cube cube) {
        ViewCoords vc = new ViewCoords(cube, this.x, this.y, this.z);
        vc.setup();
        return vc;
    }

    /**
     * Returns a list of visible faces.
     *
     * @return a list of visible faces
     */
    public List<Face.Faces> getVisibleFaces() {
        List<Face.Faces> visible = new ArrayList<>();
        for (Face.Faces f : Face.Faces.values()) {
            visible.add(f);
        }
        for (Face.Faces f : this.invisibleFaces) {
            visible.remove(f);
        }
        return visible;
    }

    /**
     * Retrieves the list of visible colors in the current context.
     *
     * @return A list of Color objects representing the visible colors.
     */
    public List<Color> getVisibleColors() {
        List<Color> colors = new ArrayList<>();
        for (Face.Faces f : getVisibleFaces()) {
            colors.add(f.getColor());
        }
        return colors;
    }

    /**
     * Check if the given color is present in the list of visible colors.
     *
     * @param color the color to check
     * @return true if the color is present, false otherwise
     */
    public boolean hasColor(Color color) {
        return getVisibleColors().contains(color);
    }

    /**
     * Checks if the given cube is in the correct place.
     *
     * @param cube the cube to be checked
     * @return true if the cube is in the correct place, false otherwise
     */
    public boolean isInCorrectPlace(Cube cube) {
        return getFaceSystem().getTopFace().equals(cube.getFaces().getTopFace()) &&
                getFaceSystem().getRightFace().equals(cube.getFaces().getRightFace()) &&
                getFaceSystem().getLeftFace().equals(cube.getFaces().getLeftFace()) &&
                getFaceSystem().getFrontFace().equals(cube.getFaces().getFrontFace()) &&
                getFaceSystem().getBackFace().equals(cube.getFaces().getBackFace()) &&
                getFaceSystem().getBottomFace().equals(cube.getFaces().getBottomFace());
    }

    /**
     * Returns the model for the current Group.
     *
     * @return the model for the current Group
     */
    public Group getModel() {
        if (model != null)
            return model;
        Box[] boxes = new Box[6 + 12];
        for (int i = 0; i < 6; i++) {
            Color color = null;
            switch (this.faces[i].getFace()) {
                case TOP:
                    if (this.y != 0) {
                        color = Color.BLACK;
                        invisibleFaces.add(Face.Faces.TOP);
                    }
                    break;
                case BOTTOM:
                    if (this.y != Cube.cubeSize - 1) {
                        color = Color.BLACK;
                        invisibleFaces.add(Face.Faces.BOTTOM);
                    }
                    break;
                case RIGHT:
                    if (this.x != Cube.cubeSize - 1) {
                        color = Color.BLACK;
                        invisibleFaces.add(Face.Faces.RIGHT);
                    }
                    break;
                case LEFT:
                    if (this.x != 0) {
                        color = Color.BLACK;
                        invisibleFaces.add(Face.Faces.LEFT);
                    }
                    break;
                case FRONT:
                    if (this.z != 0) {
                        color = Color.BLACK;
                        invisibleFaces.add(Face.Faces.FRONT);
                    }
                    break;
                case BACK:
                    if (this.z != Cube.cubeSize - 1) {
                        color = Color.BLACK;
                        invisibleFaces.add(Face.Faces.BACK);
                    }
                    break;
            }
            boxes[i] = this.faces[i].getModel(color);
        }
        for (int i = 0; i < 12; i++) {
            boxes[6 + i] = getBorders()[i];
        }
        Group group = new Group(boxes);
        group.setTranslateX((double) this.x * Cube.INNER_CUBE_WIDTH);
        group.setTranslateY((double) this.y * Cube.INNER_CUBE_WIDTH);
        group.setTranslateZ((double) this.z * Cube.INNER_CUBE_WIDTH);
        group.getTransforms().add(new Rotate(0));
        this.model = group;
        return group;
    }

    /**
     * Returns an array of Box objects representing the borders of a cube.
     *
     * @return an array of Box objects representing the cube borders
     */
    private Box[] getBorders() {
        Box[] borders = new Box[12];
        int counter = 0;
        for (int i = 0; i < 4; i++) {
            Box border = new Box(Cube.INNER_CUBE_WIDTH, 2, 2);
            int boxY = -Cube.INNER_CUBE_WIDTH / 2;
            if (i >= 2)
                boxY = Cube.INNER_CUBE_WIDTH / 2;
            border.setTranslateY(boxY);
            border.setTranslateZ(i % 2 == 0 ? -Cube.INNER_CUBE_WIDTH / 2 : Cube.INNER_CUBE_WIDTH / 2);
            border.setMaterial(new PhongMaterial(Color.BLACK));
            borders[counter] = border;
            counter++;
        }
        for (int i = 0; i < 4; i++) {
            Box border = new Box(2, Cube.INNER_CUBE_WIDTH, 2);
            int boxZ = -Cube.INNER_CUBE_WIDTH / 2;
            if (i >= 2)
                boxZ = Cube.INNER_CUBE_WIDTH / 2;
            border.setTranslateX(i % 2 == 0 ? -Cube.INNER_CUBE_WIDTH / 2 : Cube.INNER_CUBE_WIDTH / 2);
            border.setTranslateZ(boxZ);
            border.setMaterial(new PhongMaterial(Color.BLACK));
            borders[counter] = border;
            counter++;
        }
        for (int i = 0; i < 4; i++) {
            Box border = new Box(2, 2, Cube.INNER_CUBE_WIDTH);
            int boxX = -Cube.INNER_CUBE_WIDTH / 2;
            if (i >= 2)
                boxX = Cube.INNER_CUBE_WIDTH / 2;
            border.setTranslateX(boxX);
            border.setTranslateY(i % 2 == 0 ? -Cube.INNER_CUBE_WIDTH / 2 : Cube.INNER_CUBE_WIDTH / 2);
            border.setMaterial(new PhongMaterial(Color.BLACK));
            borders[counter] = border;
            counter++;
        }
        return borders;
    }

    /**
     * Retrieves the ID of the object.
     *
     * @return the ID of the object
     */
    public int getID() {
        return this.id;
    }

    /**
     * Returns a string representation of the Cube object.
     *
     * @return a string containing the cube's ID, coordinates, and the number of
     *         visible faces
     */
    @Override
    public String toString() {
        return "Cube " + this.id + " at " + String.format("%s %s %s", this.x, this.y, this.z) + " with "
                + getVisibleFaces().size() + " faces";
    }
}
