package com.task3.interfaces;

public interface IFCharacter {
    public Integer health = 10;
    public Boolean isAlive = true;

    public Integer getCurrentRow();
    public Integer getCurrentColumn();
    public void SetNewPos(Integer row, Integer column);




}
