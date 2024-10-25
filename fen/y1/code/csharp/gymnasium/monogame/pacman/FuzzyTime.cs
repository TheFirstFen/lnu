using System;

using Pac.Character;
using Pac.Constants;

namespace Pac.Fuzzy
{
    public class FuzzyTime : FuzzyParameter
    {
        public static double baseTime = GameConstants.MAP_NO_OF_ROWS / 2 + GameConstants.MAP_NO_OF_COLS / 2;

        public static double pelletShort(Pacman pac)
        {
            double rate = (double)pac.pelletEatenTime;
            if (rate < (baseTime * 2 / 3))
            {
                return (1 - Math.Min(((rate - 0) / (baseTime * 2 / 3)), (((baseTime * 2 / 3) - rate) / (baseTime * 2 / 3))));
            }
            return 0;
        }

        public static double pelletMedium(Pacman pac)
        {
            double rate = (double)pac.pelletEatenTime;
            if (rate < (baseTime * 2 / 3))
            {
                return Math.Min(((rate - 0) / (baseTime * 2 / 3)), (((baseTime * 2 / 3) - rate) / (baseTime * 2 / 3)));
            }
            if (rate < (baseTime * 4 / 3))
            {
                return (1 - Math.Min(((rate - (baseTime * 2 / 3)) / (baseTime * 2 / 3)), (((baseTime * 4 / 3) - rate) / (baseTime * 2 / 3))));
            }
            return 0;
        }

        public static double pelletLong(Pacman pac)
        {
            double rate = (double)pac.pelletEatenTime;
            if (rate < (baseTime * 2 / 3)) return 0;
            if (rate < (baseTime * 4 / 3))
            {
                return Math.Min(((rate - (baseTime * 2 / 3)) / (baseTime * 2 / 3)), (((baseTime * 4 / 3) - rate) / (baseTime * 2 / 3)));
            }
            return 1;
        }

        public static double lifetimeShort(Pacman pac)
        {
            double rate = pac.lifetime;
            if (rate < (baseTime * 2 / 3))
            {
                return (1 - Math.Min(((rate - 0) / (baseTime * 3)), (((baseTime * 3) - rate) / (baseTime * 3))));
            }
            return 0;
        }

        public static double lifetimeMedium(Pacman pac)
        {
            double rate = pac.lifetime;
            if (rate < (baseTime * 2))
            {
                return Math.Min(((rate - 0) / (baseTime * 2)), (((baseTime * 2) - rate) / (baseTime * 2)));
            }
            if (rate < (baseTime * 4))
            {
                return (1 - Math.Min(((rate - (baseTime * 2)) / (baseTime * 2)), (((baseTime * 4) - rate) / (baseTime * 4))));
            }
            return 0;
        }

        public static double lifetimeLong(Pacman pac)
        {
            double rate = pac.lifetime;

            if (rate < (baseTime * 4))
            {
                return Math.Min(((rate - 0) / (baseTime * 4)), (((baseTime * 4) - rate) / (baseTime * 4)));
            }
            return 1;
        }
    }
}
