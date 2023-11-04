using System;
using System.Linq;

using Pac.Character;
using Pac.Constants;
using Pac.Index;

namespace Pac.Fuzzy
{
    public class FuzzyDistance : FuzzyParameter
    {
        public static int levelSize = GameConstants.MAP_NO_OF_ROWS + GameConstants.MAP_NO_OF_COLS - 2;

        public static int findDistance(GameCharacter char1, GameCharacter char2)
        {
            int g_x1 = (int)((char1.bound.X - 100) / GameConstants.TEXTURE_WIDTH);
            int g_y1 = (int)((char1.bound.Y) / GameConstants.TEXTURE_HEIGHT);
            int p_x1 = (int)((char2.bound.X - 100) / GameConstants.TEXTURE_WIDTH);
            int p_y1 = (int)((char2.bound.Y) / GameConstants.TEXTURE_HEIGHT);
            BestPath bp = null;

            for (int i = 0; i < PathIndexer.allPaths.Count; i++)
            {
                bp = PathIndexer.allPaths.ElementAt(i);
                if (bp.x == g_y1 && bp.y == g_x1) break;
            }
            int dist = bp.shortestPath[p_y1, p_x1];
            return dist;
        }

        public static double distanceNear(GameCharacter char1, GameCharacter char2)
        {
            int dist = findDistance(char1, char2);

            if (dist > levelSize / 3) return 0;

            return (1.0 - Math.Min(((dist - 0) / ((double)levelSize / 3 - 0)), (((double)levelSize / 3 - dist) / ((double)levelSize / 3 - 0))));
        }

        public static double distanceMedium(GameCharacter char1, GameCharacter char2)
        {
            int dist = findDistance(char1, char2);

            if (dist > levelSize * 2 / 3) return 0;

            if (dist > levelSize / 3)
                return (1.0 - Math.Min(((dist - (double)levelSize / 3) / ((double)levelSize / 3)), (((double)levelSize * 2 / 3 - dist) / ((double)levelSize / 3))));

            return Math.Min(((dist - 0) / ((double)levelSize / 3)), (((double)levelSize / 3 - dist) / ((double)levelSize / 3)));
        }

        public static double distanceFar(GameCharacter char1, GameCharacter char2)
        {
            int dist = findDistance(char1, char2);

            if (dist > levelSize * 2 / 3) return 1;

            if (dist > levelSize / 3)
                return Math.Min(((dist - (double)levelSize / 3) / ((double)levelSize / 3)), (((double)levelSize * 2 / 3 - dist) / ((double)levelSize / 3)));

            return 0;
        }

        public static double ghostDistanceNear(Ghost[] ghosts, int index)
        {
            double dist = 0;
            for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
            {
                if (i != index)
                {
                    dist = Math.Min(dist,distanceNear(ghosts[i],ghosts[index]));
                }
            }

            if (dist > levelSize / 3) return 0;

            return (1.0 - Math.Min(((dist - 0) / ((double)levelSize / 3 - 0)), (((double)levelSize / 3 - dist) / ((double)levelSize / 3 - 0))));
        }

        public static double ghostDistanceMedium(Ghost[] ghosts, int index)
        {
            double dist = 0;
            for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
            {
                if (i != index)
                {
                    dist = Math.Min(dist, distanceMedium(ghosts[i], ghosts[index]));
                }
            }

            if (dist > levelSize * 2 / 3) return 0;

            if (dist > levelSize / 3)
                return (1.0 - Math.Min(((dist - (double)levelSize / 3) / ((double)levelSize / 3)), (((double)levelSize * 2 / 3 - dist) / ((double)levelSize / 3))));

            return Math.Min(((dist - 0) / ((double)levelSize / 3)), (((double)levelSize / 3 - dist) / ((double)levelSize / 3)));
        }

        public static double ghostDistanceFar(Ghost[] ghosts, int index)
        {
            double dist = 0;
            for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
            {
                if (i != index)
                {
                    dist = Math.Min(dist, distanceFar(ghosts[i], ghosts[index]));
                }
            }

            if (dist > levelSize * 2 / 3) return 1;

            if (dist > levelSize / 3)
                return Math.Min(((dist - (double)levelSize / 3) / ((double)levelSize / 3)), (((double)levelSize * 2 / 3 - dist) / ((double)levelSize / 3)));

            return 0;
        }
    }
}
