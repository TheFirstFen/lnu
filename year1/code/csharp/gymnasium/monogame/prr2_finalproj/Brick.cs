using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace Breakout
{
    class Brick : Sprite
    {
        public Brick(Texture2D texture, Vector2 pos, Rectangle screen) : base (texture, pos, screen)
        {
            speed = 0f;
        }
    }
}
