using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace Breakout
{
    class Sprite
    {
        protected Texture2D texture;
        protected Vector2 pos;
        protected Vector2 dir;
        protected Rectangle screen;
        protected float speed;

        public Rectangle spriteBox
        {
            get { return new Rectangle((int)pos.X, (int)pos.Y, texture.Width, texture.Height); }
        }

        public Sprite(Texture2D texture, Vector2 pos, Rectangle screen)
        {
            this.texture = texture;
            this.pos = pos;
            this.screen = screen;
        }

        public Sprite(Texture2D texture, Rectangle screen)
        {
            this.texture = texture;
            this.screen = screen;
        }

        public virtual void Update(GameTime gameTime)
        {
            pos += dir * speed;
        }

        public virtual void Draw(SpriteBatch spriteBatch)
        {
            spriteBatch.Draw(texture, pos, Color.White);
        }
    }
}
