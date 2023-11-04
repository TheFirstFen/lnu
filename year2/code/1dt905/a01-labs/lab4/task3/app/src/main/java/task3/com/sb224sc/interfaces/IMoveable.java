package task3.com.sb224sc.interfaces;

import task3.com.sb224sc.classes.*;

public interface IMoveable {
    public boolean isMoveable();

    public void moveAbsolute(Position pos);

    public void moveRelative(Position pos);
}
