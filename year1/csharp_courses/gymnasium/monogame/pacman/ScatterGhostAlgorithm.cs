using Microsoft.Xna.Framework;

using Pac.Character;
using Pac.Constants;

namespace Pac.GhostAlgorithm
{
    public class ScatterGhostAlgorithm : GhostAlgorithmI
    {
        private static ScatterGhostAlgorithm instance = null;

        private ScatterGhostAlgorithm() { }

        public static GhostAlgorithmI getInstance()
        {
            if (instance == null)
            {
                instance = new ScatterGhostAlgorithm();
            }
            return instance;
        }

        public override void moveGhost(Ghost[] ghosts, int index, Pacman pacman)
        {
            Point pac = pacman.getPoint();
            Point toMove;
            switch (r.Next()%4)
            {
                case 0:
                    toMove = new Point(1,1);
                    break;
                case 1:
                    toMove = new Point(1, GameConstants.MAP_NO_OF_ROWS - 2);
                    break;
                case 2:
                    toMove = new Point(GameConstants.MAP_NO_OF_COLS - 2, 1);
                    break;
                case 3:
                    toMove = new Point(GameConstants.MAP_NO_OF_COLS - 2, GameConstants.MAP_NO_OF_ROWS - 2);
                    break;
                default:
                    toMove = new Point(pac.Y, pac.X);
                    break;
            }

            move(ghosts[index], toMove);
        }
    }
}
