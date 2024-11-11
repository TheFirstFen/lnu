package com.task3;

import com.task3.interfaces.IFObject;

public class Object implements IFObject {
    private Integer currentRow = 0;
    private Integer currentColumn = 0;
    private Boolean timeToSpawn = true;
    private Boolean timeToRemove = false;


    public Integer getCurrentRow() {
        return currentRow;
    }

    public Integer getCurrentColumn() {
        return currentColumn;
    }

    public Boolean getTimeToSpawn() {
        return timeToSpawn;
    }

    public Boolean getTimeToRemove() {
        return timeToRemove;
    }

    public void setTimeToSpawn(Boolean bool) {
        timeToSpawn = bool;
    }

    public void setTimeToremove(Boolean bool) {
        timeToRemove = bool;
    }

    public void SetNewPos(Integer row, Integer column) {
        currentRow = row;
        currentColumn = column;
    }
    }
    

