using System;

using Pac.Character;

namespace Pac.Fuzzy
{
    public class FuzzySkill : FuzzyParameter
    {
        public static double skillBad(Pacman pac)
        {
            return Math.Max(FuzzyTime.lifetimeShort(pac), FuzzyRate.pelletRateBad(pac));
        }

        public static double skillMedium(Pacman pac)
        {
            return Math.Max(FuzzyTime.lifetimeMedium(pac), FuzzyRate.pelletRateMedium(pac));
        }

        public static double skillGood(Pacman pac)
        {
            return Math.Max(FuzzyTime.lifetimeLong(pac), FuzzyRate.pelletRateGood(pac));
        }
    }
}
