using System;

using Pac.Character;
using Pac.Scene;
using Pac.Constants;
using Pac.GhostAlgorithm;

namespace Pac.Fuzzy
{
    public class FuzzyController
    {
        private static FuzzyController instance = null;

        private FuzzyController() { }

        public static FuzzyController getInstance()
        {
            if (instance == null)
                instance = new FuzzyController();
            return instance;
        }

        public void decideLogic(Ghost[] ghosts, int index, Pacman pac)
        {
            double forecast_weight;
            double hunter_weight;
            double shy_weight = 1 + PacmanScene.GetInstance().level/2;
            double random_weight = 1.5 + PacmanScene.GetInstance().level;
            if (pac.pelletsEaten > GameConstants.pelletsLeft)
            {
                forecast_weight = 4 + PacmanScene.GetInstance().level;
                hunter_weight = 4 + PacmanScene.GetInstance().level;
            }
            else
            {
                forecast_weight = 3 + PacmanScene.GetInstance().level;
                 hunter_weight = 3 + PacmanScene.GetInstance().level;
            }
            double hunter = getDefuzzifiedHunter(ghosts[index],pac) * hunter_weight;
            double shy = getDefuzzifiedShy(ghosts, index, pac) * shy_weight;
            double random = getDefuzzifiedRandom(ghosts, index, pac) * random_weight;            
            double forecast = getDefuzzifiedForecast(ghosts[index],pac)*forecast_weight;

            if (hunter >= shy && hunter >= random && hunter >= forecast)
            {
                ghosts[index].logic = HunterGhostAlgorithm.getInstance();
                ghosts[index].logicString = "Hunter";
            }
            else if (shy >= random && shy >= forecast)
            {
                ghosts[index].logic = ShyGhostAlgorithm.getInstance();
                ghosts[index].logicString = "Shy";
            }
            else if (random >= forecast)
            {
                ghosts[index].logic = RandomGhostAlgorithm.getInstance();
                ghosts[index].logicString = "Random";
            }
            else
            {
                ghosts[index].logic = ForecastGhostAlgorithm.getInstance();
                ghosts[index].logicString = "Forecast";
            }
            
        }

        public double getDefuzzifiedHunter(Ghost ghost,Pacman pac)
        {
            double ret = Math.Min(FuzzyDistance.distanceNear(ghost, pac), FuzzySkill.skillGood(pac));
            ret = Math.Max(ret,Math.Min(Math.Min(FuzzyDistance.distanceNear(ghost, pac), FuzzySkill.skillMedium(pac)), FuzzyTime.pelletMedium(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceNear(ghost, pac), FuzzySkill.skillMedium(pac)), FuzzyTime.pelletLong(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceMedium(ghost, pac), FuzzySkill.skillGood(pac)), FuzzyTime.pelletMedium(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceMedium(ghost, pac), FuzzySkill.skillMedium(pac)), FuzzyTime.pelletLong(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceFar(ghost, pac), FuzzySkill.skillGood(pac)), FuzzyTime.pelletLong(pac)));
            ret=Math.Max(ret,Math.Min(Math.Min(FuzzyDistance.distanceNear(ghost,pac),FuzzySkill.skillGood(pac)),FuzzyTime.pelletShort(pac)));
            ret=Math.Max(ret,Math.Min(Math.Min(FuzzyDistance.distanceNear(ghost,pac),FuzzySkill.skillMedium(pac)),FuzzyTime.pelletMedium(pac)));
            return ret;
        }

        public double getDefuzzifiedForecast(Ghost ghost, Pacman pac)
        {
            double ret = Math.Min(FuzzyDistance.distanceNear(ghost, pac), FuzzySkill.skillGood(pac));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceNear(ghost, pac), FuzzySkill.skillMedium(pac)), FuzzyTime.pelletShort(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceNear(ghost, pac), FuzzySkill.skillGood(pac)), FuzzyTime.pelletLong(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceNear(ghost, pac), FuzzySkill.skillBad(pac)), FuzzyTime.pelletLong(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceMedium(ghost, pac), FuzzySkill.skillGood(pac)), FuzzyTime.pelletLong(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceMedium(ghost, pac), FuzzySkill.skillMedium(pac)), FuzzyTime.pelletMedium(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(FuzzyDistance.distanceFar(ghost, pac), FuzzySkill.skillBad(pac)), FuzzyTime.pelletShort(pac)));
            
            return ret;
        }

        public double getDefuzzifiedShy(Ghost[] ghosts,int index, Pacman pac)
        {
            double ret = Math.Min(Math.Min(Math.Min(FuzzyDistance.distanceFar(ghosts[index], pac), FuzzySkill.skillBad(pac)), FuzzyDistance.ghostDistanceNear(ghosts, index)), FuzzyTime.pelletShort(pac));
            ret = Math.Max(ret,Math.Min(Math.Min(Math.Min(FuzzyDistance.distanceFar(ghosts[index], pac), FuzzySkill.skillBad(pac)), FuzzyDistance.ghostDistanceNear(ghosts, index)), FuzzyTime.pelletMedium(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(Math.Min(FuzzyDistance.distanceFar(ghosts[index], pac), FuzzySkill.skillBad(pac)), FuzzyDistance.ghostDistanceMedium(ghosts, index)), FuzzyTime.pelletShort(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(Math.Min(FuzzyDistance.distanceFar(ghosts[index], pac), FuzzySkill.skillBad(pac)), FuzzyDistance.ghostDistanceMedium(ghosts, index)), FuzzyTime.pelletMedium(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(Math.Min(FuzzyDistance.distanceFar(ghosts[index], pac), FuzzySkill.skillMedium(pac)), FuzzyDistance.ghostDistanceNear(ghosts, index)), FuzzyTime.pelletShort(pac)));
            ret = Math.Max(ret, Math.Min(Math.Min(Math.Min(FuzzyDistance.distanceMedium(ghosts[index], pac), FuzzySkill.skillBad(pac)), FuzzyDistance.ghostDistanceNear(ghosts, index)), FuzzyTime.pelletShort(pac)));
            return ret;
        }

        public double getDefuzzifiedRandom(Ghost[] ghosts, int index, Pacman pac)
        {
            double ret = Math.Min(1 - getDefuzzifiedHunter(ghosts[index], pac), 1 - getDefuzzifiedShy(ghosts, index, pac));
            ret = Math.Min(ret, 1 - getDefuzzifiedForecast(ghosts[index], pac));
            return ret;
        }
    }
}
