using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;

using Pac.Constants;

namespace Pac.Index
{
    /// <summary>
    /// BestPath is used to store the indexed paths in the Map. For given any two positions
    /// it stores the direction of the shortest path from the first position to the
    /// second.It also gives the distance in terms of number of steps between the points.
    /// Generally it stores all paths from intersections to all other possible positions.
    /// </summary>
    public class BestPath
    {
        public int x;
        public int y;
        public int[,] shortestPath = new int[GameConstants.MAP_NO_OF_ROWS, GameConstants.MAP_NO_OF_COLS];
        public String[,] dirs = new String[GameConstants.MAP_NO_OF_ROWS, GameConstants.MAP_NO_OF_COLS];
        public bool[,] visited = new bool[GameConstants.MAP_NO_OF_ROWS, GameConstants.MAP_NO_OF_COLS];

        public struct Position
        {
            public int weight;
            public String dir;
            public Point p;
        }

        public LinkedList<Position> waitingList = new LinkedList<Position>();  

        public void FindShortestPaths()
        {
            for (int i = 0; i < GameConstants.MAP_NO_OF_ROWS; i++)
            {
                for (int j = 0; j < GameConstants.MAP_NO_OF_COLS; j++)
                {
                    if (GameConstants.MAP[i, j] > 0)
                    {
                        shortestPath[i, j] = GameConstants.MAP_NO_OF_ROWS * GameConstants.MAP_NO_OF_COLS;
                    }
                }
            }
            
            shortestPath[x, y] = 0;
            FindShortest(x, y);
        }
        
         /// <summary>
         /// Method used to compute the shortest paths between given position represented by i and j
         /// to all other possible valid positions using Djikstra's algorithm. This method populates 
         /// the shortestPath member with the shortest direction to take to reach other point.
         /// </summary>
         /// <param name="i"></param>
         /// <param name="j"></param>
    private void FindShortest(int i, int j)
        {
            Position pos = new Position();
            pos.weight = 0;
            pos.dir = "";
            pos.p = new Point(i,j);
            waitingList.AddFirst(pos);

            bool first = true;
            while(waitingList.Count!=0)
            {
                Position min = waitingList.First.Value;
                for (int k = 0; k < waitingList.Count; k++)
                {
                    Position p1 = waitingList.ElementAt(k);
                    if (min.weight > p1.weight)
                    {
                        min = p1;
                    }
                }
                waitingList.Remove(min);
                if (visited[min.p.X, min.p.Y] == false && GameConstants.MAP[min.p.X, min.p.Y] > 0)
                {
                    if (shortestPath[min.p.X, min.p.Y] > min.weight)
                    {
                        shortestPath[min.p.X, min.p.Y] = min.weight;
                        dirs[min.p.X, min.p.Y] = min.dir;
                    }
                    visited[min.p.X, min.p.Y] = true;

                    Position p1 = new Position();
                    if (first)
                        p1.dir = "D";
                    else
                        p1.dir = min.dir;
                    p1.p = new Point(min.p.X + 1, min.p.Y);
                    p1.weight = shortestPath[min.p.X, min.p.Y] + 1;
                    waitingList.AddFirst(p1);

                    p1 = new Position();
                    if(first)
                        p1.dir = "U";
                    else
                        p1.dir = min.dir;
                    p1.p = new Point(min.p.X - 1, min.p.Y);
                    p1.weight = shortestPath[min.p.X, min.p.Y] + 1;
                    waitingList.AddFirst(p1);

                    p1 = new Position();
                    if(first)
                        p1.dir = "R";
                    else
                        p1.dir = min.dir;
                    p1.p = new Point(min.p.X, min.p.Y + 1);
                    p1.weight = shortestPath[min.p.X, min.p.Y] + 1;
                    waitingList.AddFirst(p1);

                    p1 = new Position();
                    if(first)
                        p1.dir = "L";
                    else
                        p1.dir = min.dir;
                    p1.p = new Point(min.p.X, min.p.Y - 1);
                    p1.weight = shortestPath[min.p.X, min.p.Y] + 1;
                    waitingList.AddFirst(p1);

                    first = false;
                }
            }
        }

    }
}
