using System;
using Microsoft.Xna.Framework;

using Pac.GhostAlgorithm;
using Pac.Constants;

namespace Pac.Character
{
    public class Ghost : GameCharacter
    {
        public GhostAlgorithmI logic = ScatterGhostAlgorithm.getInstance();
        public String logicString = "Scatter";

        private static Random r = new Random();

        public static double timeForScatter;
        public static bool isScattered;

        public Ghost(int speed)
        {
            this.speed = speed;
        }

        public void intializePosition(int i)
        {
            int rand = r.Next();
            if (rand%2 == 0)
                bound = new Vector2(100 + 10 + GameConstants.TEXTURE_WIDTH * 12, 0 + 9 + GameConstants.TEXTURE_HEIGHT * 14);
            else
                bound = new Vector2(100 + 10 + GameConstants.TEXTURE_WIDTH * 15, 0 + 9 + GameConstants.TEXTURE_HEIGHT * 14);

            timeForScatter = -1.0;
        }

        public bool isAtIntersection()
        {
            int x1 = (int)(((this.bound.X - 10) - 100) + 1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((this.bound.Y - 9) + 1) / GameConstants.TEXTURE_HEIGHT;
            int x2 = (int)(((this.bound.X - 10 + GameConstants.TEXTURE_WIDTH) - 100) - 1) / GameConstants.TEXTURE_WIDTH;
            int y2 = (int)((this.bound.Y - 9 + GameConstants.TEXTURE_HEIGHT) - 1) / GameConstants.TEXTURE_HEIGHT;
            if (((GameConstants.MAP[y1, x1 - 1] != GameConstants.MAP_WALL && GameConstants.MAP[y2, x1 - 1] != GameConstants.MAP_WALL)
                || (GameConstants.MAP[y1, x1 + 1] != GameConstants.MAP_WALL && GameConstants.MAP[y2, x1 + 1] != GameConstants.MAP_WALL))
                && ((GameConstants.MAP[y1 - 1, x1] != GameConstants.MAP_WALL && GameConstants.MAP[y1 - 1, x2] != GameConstants.MAP_WALL)
                || (GameConstants.MAP[y1 + 1, x1] != GameConstants.MAP_WALL && GameConstants.MAP[y1 + 1, x2] != GameConstants.MAP_WALL)))
            {
                return true;
            }
            return false;
        }
    }
}
