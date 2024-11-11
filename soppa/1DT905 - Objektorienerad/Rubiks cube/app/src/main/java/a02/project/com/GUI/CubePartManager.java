package a02.project.com.GUI;
import java.util.List;
import java.util.ArrayList;

public class CubePartManager {
    private static CubePartManager instance;
    private List<GraphicCubePart> cubeParts = new ArrayList<>();
    private List<GraphicCubePart> fakeCubeParts = new ArrayList<>();

    private CubePartManager() {
    }

    public static CubePartManager getInstance() {
        if (instance == null) {
            instance = new CubePartManager();
        }
        return instance;
    }

    public List<GraphicCubePart> getCubeParts() {
        return cubeParts;
    }
    public List<GraphicCubePart> getFakeCubeParts() {
        return fakeCubeParts;
    }

    public void setCubeParts(List<GraphicCubePart> parts) {
        cubeParts = parts;
    }
    public void setFakeCubeParts(List<GraphicCubePart> parts) {
        fakeCubeParts = parts;
    }
}
