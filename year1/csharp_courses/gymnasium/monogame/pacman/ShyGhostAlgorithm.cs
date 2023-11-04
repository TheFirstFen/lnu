using System;
using System.Linq;

using Pac.Character;
using Pac.Constants;
using Pac.Index;

namespace Pac.GhostAlgorithm
{
    public class ShyGhostAlgorithm : GhostAlgorithmI
    {
        private static ShyGhostAlgorithm instance = null;

        private ShyGhostAlgorithm() { }

        public static GhostAlgorithmI getInstance()
        {
            if (instance == null)
            {
                instance = new ShyGhostAlgorithm();
            }
            return instance;
        }

        public override void moveGhost(Ghost[] ghosts, int index, Pacman pacman)
        {
            int x1 = (int)(ghosts[index].bound.X - 100 + GameConstants.TEXTURE_WIDTH / 2) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)(ghosts[index].bound.Y + GameConstants.TEXTURE_HEIGHT / 2) / GameConstants.TEXTURE_HEIGHT;

            String closest_dir = "L";
            BestPath bp = null ;

            for (int j = 0; j < PathIndexer.allPaths.Count; j++)
            {
                bp = PathIndexer.allPaths.ElementAt(j);
                if (bp.x == y1 && bp.y == x1)
                {
                    break;
                }
            }

            if (pacman.isPowerUpMode)
            {
                int pac_x1 = (int)(pacman.bound.X - 100) / GameConstants.TEXTURE_WIDTH;
                int pac_y1 = (int)(pacman.bound.Y) / GameConstants.TEXTURE_HEIGHT;
                closest_dir = bp.dirs[pac_y1, pac_x1];
            }
            else
            {
                int min_dist = GameConstants.MAP_NO_OF_ROWS * GameConstants.MAP_NO_OF_COLS;
                for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
                {
                    if (i != index)
                    {
                        int ghost_x1 = (int)(ghosts[i].bound.X - 100) / GameConstants.TEXTURE_WIDTH;
                        int ghost_y1 = (int)(ghosts[i].bound.Y) / GameConstants.TEXTURE_HEIGHT;
                        if (bp.shortestPath[ghost_y1, ghost_x1] < min_dist && bp.shortestPath[ghost_y1, ghost_x1] > 0)
                        {
                            min_dist = bp.shortestPath[ghost_y1, ghost_x1];
                            closest_dir = bp.dirs[ghost_y1, ghost_x1];
                        }
                    }
                }
            }

            String dirAvl = getRandomDirection(x1, y1, closest_dir);

            if (dirAvl.Equals("L"))
            {
                ghosts[index].moveL();
            }
            if (dirAvl.Equals("R"))
            {
                ghosts[index].moveR();
            }
            if (dirAvl.Equals("U"))
            {
                ghosts[index].moveU();
            }
            if (dirAvl.Equals("D"))
            {
                ghosts[index].moveD();
            }
        }

    }
}
