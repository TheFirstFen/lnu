using System.Collections.Generic;

using Pac.Constants;

namespace Pac.Index
{
    public class PathIndexer
    {
        public static List<BestPath> allPaths = new List<BestPath>();

        public static void StartIndexing()
        {
            GameConstants.pelletsLeft = 0;
            for (int i = 0; i < GameConstants.MAP_NO_OF_ROWS; i++)
            {
                for (int j = 0; j < GameConstants.MAP_NO_OF_COLS; j++)
                {
                    if (GameConstants.MAP[i, j] > 0)
                    {
                        if (IsIntersection(i, j))
                        {
                            BestPath path = new BestPath();
                            path.x = i;
                            path.y = j;
                            path.FindShortestPaths();
                            allPaths.Add(path);
                        }
                    }

                }
            }
        }

        public static bool IsIntersection(int j, int i)
        {
            if (((GameConstants.MAP[j, i - 1] != GameConstants.MAP_WALL) || (GameConstants.MAP[j, i + 1] != GameConstants.MAP_WALL))
                && ((GameConstants.MAP[j - 1, i] != GameConstants.MAP_WALL) || (GameConstants.MAP[j + 1, i] != GameConstants.MAP_WALL)))
            {
                return true;
            }
            return false;
        }
    }
}
