using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

using Pac.Constants;

namespace Pac.Character
{
    public class GameCharacter
    {
        public Vector2 bound;
        public int width = 16;
        public int height = 14;
        public int speed, speedX, speedY;
        public SpriteEffects spriteDirection = SpriteEffects.None;
        public int angle = 0;

        public void moveL()
        {
            int x1 = (int)(((this.bound.X - 10) - 100)+1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((this.bound.Y - 9)+1) / GameConstants.TEXTURE_HEIGHT;
            int y2 = (int)((this.bound.Y - 9 + GameConstants.TEXTURE_HEIGHT)-1) / GameConstants.TEXTURE_HEIGHT;

            if (GameConstants.MAP[y1, x1 - 1] != GameConstants.MAP_WALL && GameConstants.MAP[y2, x1 - 1] != GameConstants.MAP_WALL)
            {
                speedX = -speed;
                speedY = 0;
                spriteDirection = SpriteEffects.FlipHorizontally;
                angle = 0;
            }
        }

        public void moveR()
        {
            int x1 = (int)(((this.bound.X - 10 ) - 100)+1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((this.bound.Y - 9)+1) / GameConstants.TEXTURE_HEIGHT;
            int y2 = (int)((this.bound.Y - 9 + GameConstants.TEXTURE_HEIGHT)-1) / GameConstants.TEXTURE_HEIGHT;
            if (GameConstants.MAP[y1, x1 + 1] != GameConstants.MAP_WALL && GameConstants.MAP[y2, x1 + 1] != GameConstants.MAP_WALL)
            {
                speedX = speed;
                speedY = 0;
                spriteDirection = SpriteEffects.None;
                angle = 0;
            }
        }

        public void moveU()
        {
            int x1 = (int)(((this.bound.X - 10) - 100)+1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((this.bound.Y - 9)+1) / GameConstants.TEXTURE_HEIGHT;
            int x2 = (int)(((this.bound.X - 10 + GameConstants.TEXTURE_WIDTH) - 100)-1) / GameConstants.TEXTURE_WIDTH;
            if (GameConstants.MAP[y1 - 1, x1] != GameConstants.MAP_WALL && GameConstants.MAP[y1 - 1, x2] != GameConstants.MAP_WALL)
            {
                speedX = 0;
                speedY = -speed;
                spriteDirection = SpriteEffects.None;
                angle = -90;
            }
        }

        public void moveD()
        {
            int x1 = (int)(((this.bound.X - 10) - 100) + 1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((this.bound.Y - 9) + 1) / GameConstants.TEXTURE_HEIGHT;
            int x2 = (int)(((this.bound.X - 10 + GameConstants.TEXTURE_WIDTH) - 100) - 1) / GameConstants.TEXTURE_WIDTH;
            if (GameConstants.MAP[y1 + 1, x1] != GameConstants.MAP_WALL && GameConstants.MAP[y1 + 1, x2] != GameConstants.MAP_WALL)
            {
                speedX = 0;
                speedY = speed;
                spriteDirection = SpriteEffects.None;
                angle = 90;
            }
        }

        public void changeDirection()
        {
            if (speedX != 0)
            {
                speedX = -speedX;
                spriteDirection = spriteDirection.Equals(SpriteEffects.None) ? SpriteEffects.FlipHorizontally : SpriteEffects.None;
                angle = 0;
            }
            else
            {
                speedY = -speedY;
                angle = -angle;
            }
        }

        public virtual void move(GameTime gameTime)
        {
            bound.X += (float)gameTime.ElapsedGameTime.TotalSeconds * speedX;
            bound.Y += (float)gameTime.ElapsedGameTime.TotalSeconds * speedY;
        }

        public bool isCollidingWithWall()
        {
            int x1 = (int)(((this.bound.X - 10) - 100) + 1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((this.bound.Y - 9) + 1) / GameConstants.TEXTURE_HEIGHT;
            int x2 = (int)(((this.bound.X - 10 + GameConstants.TEXTURE_WIDTH) - 100) - 1) / GameConstants.TEXTURE_WIDTH;
            int y2 = (int)((this.bound.Y - 9 + GameConstants.TEXTURE_HEIGHT) - 1) / GameConstants.TEXTURE_HEIGHT;

            if (GameConstants.MAP[y1, x1] == GameConstants.MAP_WALL || GameConstants.MAP[y2, x2] == GameConstants.MAP_WALL
                || GameConstants.MAP[y1, x2] == GameConstants.MAP_WALL || GameConstants.MAP[y2, x1] == GameConstants.MAP_WALL)
            {
                return true;
            }
            return false;
        }

        public Point getPoint()
        {
            int x1 = (int)(((this.bound.X - 10) - 100 + GameConstants.TEXTURE_WIDTH / 2) + 1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((this.bound.Y - 9) + 1 + GameConstants.TEXTURE_HEIGHT / 2) / GameConstants.TEXTURE_HEIGHT;
            return new Point(x1, y1);
        }
    }
}
