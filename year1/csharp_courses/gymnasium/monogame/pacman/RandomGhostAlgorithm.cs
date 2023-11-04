using System;

using Pac.Character;
using Pac.Constants;

namespace Pac.GhostAlgorithm
{
    public class RandomGhostAlgorithm : GhostAlgorithmI
    {
        private static RandomGhostAlgorithm instance = null;

        private RandomGhostAlgorithm() { }

        public static GhostAlgorithmI getInstance()
        {
            if (instance == null)
            {
                instance = new RandomGhostAlgorithm();
            }
            return instance;
        }

        public override void moveGhost(Ghost[] ghosts, int index, Pacman pacman)
        {
            String[] dirAvl = new String[4];
            int x1 = (int)(((ghosts[index].bound.X - 10) - 100) + 1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((ghosts[index].bound.Y - 9) + 1) / GameConstants.TEXTURE_HEIGHT;
            int x2 = (int)(((ghosts[index].bound.X - 10 + GameConstants.TEXTURE_WIDTH) - 100) - 1) / GameConstants.TEXTURE_WIDTH;
            int y2 = (int)((ghosts[index].bound.Y - 9 + GameConstants.TEXTURE_HEIGHT) - 1) / GameConstants.TEXTURE_HEIGHT;
            int i = 0;

            if (GameConstants.MAP[y1, x1 - 1] != GameConstants.MAP_WALL && GameConstants.MAP[y2, x1 - 1] != GameConstants.MAP_WALL)
            {
                dirAvl[i++] = "L";
            }
            if (GameConstants.MAP[y1, x1 + 1] != GameConstants.MAP_WALL && GameConstants.MAP[y2, x1 + 1] != GameConstants.MAP_WALL)
            {
                dirAvl[i++] = "R";
            }
            if (GameConstants.MAP[y1 - 1, x1] != GameConstants.MAP_WALL && GameConstants.MAP[y1 - 1, x2] != GameConstants.MAP_WALL)
            {
                dirAvl[i++] = "U";
            }
            if (GameConstants.MAP[y1 + 1, x1] != GameConstants.MAP_WALL && GameConstants.MAP[y1 + 1, x2] != GameConstants.MAP_WALL)
            {
                dirAvl[i++] = "D";
            }
      
            int x = r.Next(0, i);
            if (dirAvl[x].Equals("L"))
            {
                ghosts[index].moveL();
            }
            if (dirAvl[x].Equals("R"))
            {
                ghosts[index].moveR();
            }
            if (dirAvl[x].Equals("U"))
            {
                ghosts[index].moveU();
            }
            if (dirAvl[x].Equals("D"))
            {
                ghosts[index].moveD();
            }
        
        }
    }
}
