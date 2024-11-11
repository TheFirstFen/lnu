package a02.project.com.GUI;

import javafx.scene.Group;

public class GraphicCubePart {
    private Group part3D;
    private Integer row;
    private Integer column;
    private Integer layer;
    private Integer tempColumn;
    private Integer tempRow;
    private String StartName;

    public GraphicCubePart(Group cubePart, Integer column, Integer row, Integer layer) {
        this.part3D = cubePart;
        this.row = row;
        this.column = column;
        this.layer = layer;
        this.StartName = Integer.toString(column) + Integer.toString(row) + Integer.toString(layer);
    }


    public String getName() {
        return this.StartName;
    }
    public Group getPart() {
        return this.part3D;
    }
    public Integer getRow() {
        return this.row;
    }
    public Integer getColumn() {
        return this.column;
    }
    public Integer getLayer() {
        return this.layer;
    }
    public Integer getTempColumn() {
        return this.tempColumn;
    }
    public void setTempColumn(Integer column) {
        this.tempColumn = column;
    }
    public Integer getTempRow() {
        return this.tempRow;
    }
    public void setTempRow(Integer row) {
        this.tempRow = row;
    }
    public void setRow(Integer n) {
        this.row = n;
    }
    public void setColumn(Integer n) {
        this.column = n;
    }
    public void setLayer(Integer n) {
        this.layer = n;
    }    
    public void setPart(Group part) {
        this.part3D = part;
    }
}

