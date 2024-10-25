using System;
using System.Linq;
using Microsoft.Xna.Framework;

using Pac.Character;
using Pac.Constants;
using Pac.Index;

namespace Pac.GhostAlgorithm
{
    public abstract class GhostAlgorithmI
    {
        public abstract void moveGhost(Ghost[] ghosts, int index, Pacman pacman);

        protected static Random r = new Random();

        public String getRandomDirection(int x1, int y1, String closest_dir)
        {
            int k = 0;
            String[] dirAvl = new String[4];
            // Check available directions
            if (GameConstants.MAP[y1, x1 + 1] != GameConstants.MAP_WALL && closest_dir != "R")
            {
                dirAvl[k++] = "R";
            }
            else if (GameConstants.MAP[y1, x1 - 1] != GameConstants.MAP_WALL && closest_dir != "L")
            {
                dirAvl[k++] = "L";
            }
            else if (GameConstants.MAP[y1 + 1, x1] != GameConstants.MAP_WALL && closest_dir != "D")
            {
                dirAvl[k++] = "D";
            }
            else if (GameConstants.MAP[y1 - 1, x1] != GameConstants.MAP_WALL && closest_dir != "U")
            {
                dirAvl[k++] = "U";
            }

            int x = r.Next(0, k);
            return dirAvl[x];
        }

        public void move(Ghost ghost, Point toMove)
        {
            Point gPos = ghost.getPoint();

            for (int i = 0; i < PathIndexer.allPaths.Count; i++)
            {
                BestPath bp = PathIndexer.allPaths.ElementAt(i);
                if (bp.x == gPos.Y && bp.y == gPos.X)
                {
                    String dir = bp.dirs[toMove.Y, toMove.X];
                    if (dir != null)
                    {
                        if (dir.Equals("L"))
                            ghost.moveL();
                        else if (dir.Equals("R"))
                            ghost.moveR();
                        else if (dir.Equals("U"))
                            ghost.moveU();
                        else if (dir.Equals("D"))
                            ghost.moveD();
                    }
                }
            }
        }
    }
}
