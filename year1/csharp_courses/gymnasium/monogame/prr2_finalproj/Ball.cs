using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace Breakout
{
    class Ball : Sprite
    {
        public bool IsGameOver { get; set; }
        public bool IsShoot { get; set; }

        public Ball(Texture2D texture, Vector2 pos, Rectangle screen) : base (texture, pos, screen)
        {
            speed = 4f;
            IsGameOver = false;
            IsShoot = true;
        }

        public override void Update(GameTime gameTime)
        {
            BoundsMovement();

            if (pos.Y > screen.Height)
                IsGameOver = true;

            if (Keyboard.GetState().IsKeyDown(Keys.Space))
                IsShoot = true;

            base.Update(gameTime);
        }

        private void BoundsMovement()
        {
            if (pos.X <= 0 || pos.X >= screen.Width - texture.Width)
                dir.X *= -1;
            if (pos.Y <= 0)
                dir.Y *= -1;
        }

        public void StartPos(Paddle paddle)
        {
            pos.X = paddle.spriteBox.X + paddle.spriteBox.Width / 2 - texture.Width / 2;

            pos.Y = paddle.spriteBox.Y - texture.Height - 1;

            dir = new Vector2(1, -1);
        }

        public void PaddleRebound(Paddle paddle)
        {
            if (this.spriteBox.Intersects(paddle.spriteBox))
                dir.Y *= -1;
        }

        public void BrickRebound(Brick brick)
        {
            if (this.spriteBox.Intersects(brick.spriteBox))
                dir.Y *= -1;
        }
    }
}
