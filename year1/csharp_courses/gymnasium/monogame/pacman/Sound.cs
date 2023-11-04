using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;

namespace Pac.Resources
{
    /// <summary>
    /// TODO:
    /// If sounds not allowed to use change them to blank sounds
    /// </summary>
    public class Sound
    {
        public SoundEffect soundE_pacdead, soundE_paceat, soundE_begin;
        public SoundBank soundBank;

        public Sound(Game game)
        {
            soundE_paceat = game.Content.Load<SoundEffect>("Sound/paceat");
            soundE_pacdead = game.Content.Load<SoundEffect>("Sound/pacdead");
            soundE_begin = game.Content.Load<SoundEffect>("Sound/pacbegin");
        }

        public void Dead()
        {
            soundE_pacdead.Play();
        }

        public void Eat()
        {
            soundE_paceat.Play();
        }

        public void Begin()
        {
            soundE_begin.Play();
        }

        public void Ghostmove()
        {
            soundBank.GetCue("Sound/pacghost").Play();
        }
    }
}
