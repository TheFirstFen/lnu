using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace Breakout
{
    class Paddle : Sprite
    {
        public Paddle(Texture2D texture, Rectangle screen) : base (texture, screen)
        {
            speed = 5f;
            pos = StartPos();
        }

        public override void Update(GameTime gameTime)
        {
            dir = Vector2.Zero;
            InputKeyboard();
            BoundsRestrictions();

            base.Update(gameTime);
        }

        private void BoundsRestrictions()
        {
            if (pos.X <= 0)
                pos.X = 0;
            if (pos.X >= screen.Width - texture.Width)
                pos.X = screen.Width - texture.Width;
        }

        private void InputKeyboard()
        {
            if (Keyboard.GetState().IsKeyDown(Keys.Left))
                dir.X = -1;
            if (Keyboard.GetState().IsKeyDown(Keys.Right))
                dir.X = 1;
        }

        private Vector2 StartPos()
        {
            pos = new Vector2(screen.Width / 2 - texture.Width / 2, screen.Height - 2 * texture.Height);

            return pos;
        }
    }
}
