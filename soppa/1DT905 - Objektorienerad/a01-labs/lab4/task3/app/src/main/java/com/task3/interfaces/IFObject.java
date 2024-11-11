package com.task3.interfaces;

public interface IFObject {

    public Integer getCurrentRow();
    public Integer getCurrentColumn();
    public Boolean getTimeToSpawn();
    public Boolean getTimeToRemove();
    public void setTimeToSpawn(Boolean bool);
    public void setTimeToremove(Boolean bool);
    public void SetNewPos(Integer row, Integer column);

}
