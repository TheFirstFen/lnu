using Microsoft.Xna.Framework;

using Pac.Character;

namespace Pac.GhostAlgorithm
{
    public class HunterGhostAlgorithm : GhostAlgorithmI
    {
        private static HunterGhostAlgorithm instance = null;

        private HunterGhostAlgorithm() { }

        public static GhostAlgorithmI getInstance()
        {
            if (instance == null)
            {
                instance = new HunterGhostAlgorithm();
            }
            return instance;
        }

        public override void moveGhost(Ghost[] ghosts, int index, Pacman pacman)
        {
            Point toMove = pacman.getPoint();

            move(ghosts[index], toMove);
        }
    }
}
