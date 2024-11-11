package a02.project.com.GUI;

import java.util.List;
import java.util.ArrayList;

import javafx.scene.Group;

public class CubePositions {
    public static void fixPositionsSameColumn(Boolean isPrime, List<GraphicCubePart> partsToMove) {
        Integer n1;
        Integer n3;
        if (isPrime) {
            n1 = 3;
            n3 = 1;
        } else {
            n1 = 1;
            n3 = 3;
        }
        
        List<Group> tempList = new ArrayList<>();
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());

        for (GraphicCubePart part : partsToMove) {
            if (part.getRow() == 1 && part.getLayer() == 1) {
                tempList.set(0, part.getPart());
            } else if (part.getRow() == 2 && part.getLayer() == 1) {
                tempList.set(1, part.getPart());
            } else if (part.getRow() == 3 && part.getLayer() == 1) {
                tempList.set(2, part.getPart());
            } else if (part.getRow() == 1 && part.getLayer() == 2) {
                tempList.set(3, part.getPart());
            } else if (part.getRow() == 2 && part.getLayer() == 2) {
                tempList.set(4, part.getPart());
            } else if (part.getRow() == 3 && part.getLayer() == 2) {
                tempList.set(5, part.getPart());
            } else if (part.getRow() == 1 && part.getLayer() == 3) {
                tempList.set(6, part.getPart());
            } else if (part.getRow() == 2 && part.getLayer() == 3) {
                tempList.set(7, part.getPart());
            } else if (part.getRow() == 3 && part.getLayer() == 3) {
                tempList.set(8, part.getPart());
            }
        }

    

        for (GraphicCubePart part : partsToMove) {
            if (part.getRow() == n1 && part.getLayer() == n1) {
                part.setPart(tempList.get(2));
            } else if (part.getRow() == 2 && part.getLayer() == n1) {
                part.setPart(tempList.get(5));
            } else if (part.getRow() == n3 && part.getLayer() == n1) {
                part.setPart(tempList.get(8));
            } else if (part.getRow() == n1 && part.getLayer() == 2) {
                part.setPart(tempList.get(1));
            } else if (part.getRow() == 2 && part.getLayer() == 2) {
                continue;
            } else if (part.getRow() == n3 && part.getLayer() == 2) {
                part.setPart(tempList.get(7));
            } else if (part.getRow() == n1 && part.getLayer() == n3) {
                part.setPart(tempList.get(0));
            } else if (part.getRow() == 2 && part.getLayer() == n3) {
                part.setPart(tempList.get(3));
            } else if (part.getRow() == n3 && part.getLayer() == n3) {
                part.setPart(tempList.get(6));
            }
            
         }
        
    }
    
    public static void fixPositionsSameRow(Boolean isPrime, List<GraphicCubePart> partsToMove) {
        Integer n1;
        Integer n3;
        if (isPrime) {
            n1 = 3;
            n3 = 1;
        } else {
            n1 = 1;
            n3 = 3;
        }
        List<Group> tempList = new ArrayList<>();
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());
        tempList.add(new Group());

        for (GraphicCubePart part : partsToMove) {
            if (part.getColumn() == 1 && part.getLayer() == 1) {
                tempList.set(0, part.getPart());
            } else if (part.getColumn() == 2 && part.getLayer() == 1) {
                tempList.set(1, part.getPart());
            } else if (part.getColumn() == 3 && part.getLayer() == 1) {
                tempList.set(2, part.getPart());
            } else if (part.getColumn() == 1 && part.getLayer() == 2) {
                tempList.set(3, part.getPart());
            } else if (part.getColumn() == 2 && part.getLayer() == 2) {
                tempList.set(4, part.getPart());
            } else if (part.getColumn() == 3 && part.getLayer() == 2) {
                tempList.set(5, part.getPart());
            } else if (part.getColumn() == 1 && part.getLayer() == 3) {
                tempList.set(6, part.getPart());
            } else if (part.getColumn() == 2 && part.getLayer() == 3) {
                tempList.set(7, part.getPart());
            } else if (part.getColumn() == 3 && part.getLayer() == 3) {
                tempList.set(8, part.getPart());
            }
        }

        for (GraphicCubePart part : partsToMove) {
            if (part.getColumn() == n3 && part.getLayer() == n3) {
                part.setPart(tempList.get(2));
            } else if (part.getColumn() == 2 && part.getLayer() == n3) {
                part.setPart(tempList.get(5));
            } else if (part.getColumn() == n1 && part.getLayer() == n3) {
                part.setPart(tempList.get(8));
            } else if (part.getColumn() == n3 && part.getLayer() == 2) {
                part.setPart(tempList.get(1));
            } else if (part.getColumn() == 2 && part.getLayer() == 2) {
                continue;
            } else if (part.getColumn() == n1 && part.getLayer() == 2) {
                part.setPart(tempList.get(7));
            } else if (part.getColumn() == n3 && part.getLayer() == n1) {
                part.setPart(tempList.get(0));
            } else if (part.getColumn() == 2 && part.getLayer() == n1) {
                part.setPart(tempList.get(3));
            } else if (part.getColumn() == n1 && part.getLayer() == n1) {
                part.setPart(tempList.get(6));
            }
         }
    }
    
    public static void fixPositionWholeCube(Boolean isPrime, List<GraphicCubePart> partsToMove, String choice) {
        Integer n1;
        Integer n3;
        if (isPrime) {
            n1 = 3;
            n3 = 1;
        } else {
            n1 = 1;
            n3 = 3;
        }
        switch (choice) {
            case "y":
                for (GraphicCubePart cubePart : partsToMove) {
                    cubePart.setTempColumn(cubePart.getColumn());
                    if (cubePart.getRow() == 1){
                        cubePart.setColumn(n3);
                    } else if (cubePart.getRow() == 2) {
                        cubePart.setColumn(2);
                    } else if (cubePart.getRow() == 3) {
                        cubePart.setColumn(n1);
                    } 
                    if (cubePart.getTempColumn() == 1) {
                        cubePart.setRow(n1);
                    } else if (cubePart.getTempColumn() == 2) {
                        cubePart.setRow(2);
                    } else if (cubePart.getTempColumn() == 3) {
                        cubePart.setRow(n3);
                    }

                    
                }
                break;
            //case "x":
            //    System.out.println("Nej");
            //    for (GraphicCubePart cubePart : GraphicCube.getCubeParts()) {
            //        cubePart.setTempRow(cubePart.getRow());
            //        if (cubePart.getLayer() == 1){
            //            cubePart.setRow(n3);
            //        } else if (cubePart.getLayer() == 2) {
            //            cubePart.setRow(2);
            //        } else if (cubePart.getLayer() == 3) {
            //            cubePart.setRow(n1);
            //        } 
            //        if (cubePart.getTempRow() == 1) {
            //            cubePart.setLayer(n1);
            //        } else if (cubePart.getTempRow() == 2) {
            //            cubePart.setLayer(2);
            //        } else if (cubePart.getTempRow() == 3) {
            //            cubePart.setLayer(n3);
            //        }
            //    }
            //    break;
    }
}
}

