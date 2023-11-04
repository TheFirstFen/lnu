using System;
using System.Linq;
using Microsoft.Xna.Framework;

using Pac.Character;
using Pac.Constants;
using Pac.Index;

namespace Pac.GhostAlgorithm
{
    public class ForecastGhostAlgorithm : GhostAlgorithmI
    {
        private static ForecastGhostAlgorithm instance = null;

        private ForecastGhostAlgorithm() { }

        public static GhostAlgorithmI getInstance()
        {
            if (instance == null)
            {
                instance = new ForecastGhostAlgorithm();
            }
            return instance;
        }

        bool dontForecast = false;

        public override void moveGhost(Ghost[] ghosts, int index, Pacman pacman)
        {
            Point gPos = ghosts[index].getPoint();
            Point pac = pacman.getPoint();
            Point toMove = pacman.getPoint();

            if (Math.Abs(gPos.X - pac.X) + Math.Abs(gPos.Y - gPos.Y) <= 3)
            {
                dontForecast = true;
            }

            int spX = pacman.speedX == 0 ? 0 : pacman.speedX / Math.Abs(pacman.speedX);
            int spY = pacman.speedY == 0 ? 0 : pacman.speedY / Math.Abs(pacman.speedY);

            while (!PathIndexer.IsIntersection(toMove.Y, toMove.X)&&!dontForecast)
            {
                if (pacman.speedX == 0 && pacman.speedY == 0)
                    break;
                toMove.X += spX;
                toMove.Y += spY;

                if (toMove.X == 0 || toMove.Y == 0 || toMove.X == GameConstants.MAP_NO_OF_COLS || toMove.Y == GameConstants.MAP_NO_OF_ROWS)
                {
                    if (toMove.X == 0) toMove.X++;
                    if (toMove.Y == 0) toMove.Y++;
                    if (toMove.X == GameConstants.MAP_NO_OF_COLS) toMove.X--;
                    if (toMove.Y == GameConstants.MAP_NO_OF_ROWS) toMove.Y--;
                    break;
                }

                if (PathIndexer.IsIntersection(toMove.Y, toMove.X) && ((Math.Abs(toMove.X - pac.X) + Math.Abs(toMove.Y - pac.Y)) <= 3))
                {
                    String dir = pacman.speedX == 0 ? pacman.speedY / Math.Abs(pacman.speedY) > 0 ? "D" : "U" : pacman.speedX / Math.Abs(pacman.speedX) > 0 ? "R" : "L";
                    String next = getRandomDirection(toMove.X, toMove.Y,dir);

                    if (next.Equals("L")) { toMove.X--; spX = -1; spY = 0; }
                    else if (next.Equals("R")) { toMove.X++; spX = 1; spY = 0; }
                    else if (next.Equals("U")) { toMove.Y--; spX = 0; spY = -1; }
                    else if (next.Equals("D")) { toMove.Y++; spX = 0; spY = 1; }
                }
            }

            move(ghosts[index], toMove);
        }
    }
}
