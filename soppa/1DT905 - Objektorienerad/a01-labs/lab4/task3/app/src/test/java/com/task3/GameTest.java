package com.task3;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class GameTest {

    @Test
    public void testToJsonAndFromJson() {
        // Create a Game object with specific values for testing
        Game originalGame = new Game();
        originalGame.getRobot().SetNewPos(4, 4);
        originalGame.getWolf().SetNewPos(5, 5);
        originalGame.getHome().SetNewPos(9, 9);
        originalGame.getStrawberry().SetNewPos(3, 3);
        originalGame.getSoup().SetNewPos(7, 7);

        // Convert the Game object to JSON
        String json = originalGame.toJson();

        // Parse the JSON back into a JsonObject for verification
        JsonObject jsonObject = JsonParser.parseString(json).getAsJsonObject();

        // Verify the content of the JSON representation
        assertEquals(originalGame.getRound(), jsonObject.get("round").getAsInt());
        assertEquals(originalGame.getRobot().getCurrentRow(), jsonObject.getAsJsonObject("robot").get("currentRow").getAsInt());
        assertEquals(originalGame.getRobot().getCurrentColumn(), jsonObject.getAsJsonObject("robot").get("currentColumn").getAsInt());
        assertEquals(originalGame.getWolf().getCurrentRow(), jsonObject.getAsJsonObject("wolf").get("currentRow").getAsInt());
        assertEquals(originalGame.getWolf().getCurrentColumn(), jsonObject.getAsJsonObject("wolf").get("currentColumn").getAsInt());
        assertEquals(originalGame.getHome().getCurrentRow(), jsonObject.getAsJsonObject("home").get("currentRow").getAsInt());
        assertEquals(originalGame.getHome().getCurrentColumn(), jsonObject.getAsJsonObject("home").get("currentColumn").getAsInt());
        assertEquals(originalGame.getStrawberry().getCurrentRow(), jsonObject.getAsJsonObject("strawberry").get("currentRow").getAsInt());
        assertEquals(originalGame.getStrawberry().getCurrentColumn(), jsonObject.getAsJsonObject("strawberry").get("currentColumn").getAsInt());
        assertEquals(originalGame.getSoup().getCurrentRow(), jsonObject.getAsJsonObject("soup").get("currentRow").getAsInt());
        assertEquals(originalGame.getSoup().getCurrentColumn(), jsonObject.getAsJsonObject("soup").get("currentColumn").getAsInt());

        // Convert the JSON back to a Game object
        Game parsedGame = new Gson().fromJson(json, Game.class);

        // Verify that the deserialized object is equal to the original one
        assertEquals(originalGame.getRound(), parsedGame.getRound());
        assertEquals(originalGame.getRobot().getCurrentRow(), parsedGame.getRobot().getCurrentRow());
        assertEquals(originalGame.getRobot().getCurrentColumn(), parsedGame.getRobot().getCurrentColumn());
        assertEquals(originalGame.getWolf().getCurrentRow(), parsedGame.getWolf().getCurrentRow());
        assertEquals(originalGame.getWolf().getCurrentColumn(), parsedGame.getWolf().getCurrentColumn());
        assertEquals(originalGame.getHome().getCurrentRow(), parsedGame.getHome().getCurrentRow());
        assertEquals(originalGame.getHome().getCurrentColumn(), parsedGame.getHome().getCurrentColumn());
        assertEquals(originalGame.getStrawberry().getCurrentRow(), parsedGame.getStrawberry().getCurrentRow());
        assertEquals(originalGame.getStrawberry().getCurrentColumn(), parsedGame.getStrawberry().getCurrentColumn());
        assertEquals(originalGame.getSoup().getCurrentRow(), parsedGame.getSoup().getCurrentRow());
        assertEquals(originalGame.getSoup().getCurrentColumn(), parsedGame.getSoup().getCurrentColumn());
    }
}
