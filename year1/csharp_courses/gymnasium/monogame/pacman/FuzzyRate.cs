using System;

using Pac.Character;

namespace Pac.Fuzzy
{
    public class FuzzyRate : FuzzyParameter
    {
        public static double pelletRateBad(Pacman pac)
        {
            double rate = (double)pac.pelletsEaten / pac.totalTime;
            if (rate < 1)
            {
                return (1 - Math.Min(rate, 1 - rate));
            }
            return 0;
        }
        
        public static double pelletRateMedium(Pacman pac)
        {
            double rate = (double)pac.pelletsEaten / pac.totalTime;
            if (rate < 0.5)
            {
                return Math.Min((rate / 0.5), ((0.5 - rate) / 0.5));
            }
            if (rate < 1)
            {
                return (1-Math.Min(((rate-0.5) / 0.5), ((1 - rate) / 0.5)));
            }
            return 0;
        }
        
        public static double pelletRateGood(Pacman pac)
        {
            return (1 - pelletRateBad(pac));
        }
    }
}
