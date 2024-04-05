using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

using Pac.Resources;

namespace Pac.Scene
{
    public class PauseScene : BaseScene
    {
        private static PauseScene instance;
        private double timeUp = 0;

        private int index = 0;
        private static bool flag;

        private BaseScene prevScene;

        public static PauseScene GetInstance(BaseScene prev)
        {
            if (instance == null)
            {
                instance = new PauseScene();
            }
            instance.prevScene = prev;
            instance.index = 0;
            return instance;
        }

        private PauseScene()
        {
        }

        KeyboardState prev;

        public override BaseScene Update(GameTime gameTime)
        {
            keyboardState = Keyboard.GetState();

            if(keyboardState.IsKeyDown(Keys.Enter))
            {
                if(index == 0)
                    return PacmanScene.GetInstance();
                else if (index == 1)
                    return InstructionScene.GetInstance(this);
                else
                    return MenuScene.GetInstance();
            }

            if(keyboardState.IsKeyDown(Keys.Down)&&(prev==null||prev.IsKeyUp(Keys.Down)))
            {
                index = (index + 1) % 3;
            }
            else if (keyboardState.IsKeyDown(Keys.Up) && (prev == null || prev.IsKeyUp(Keys.Up)))
            {
                index = index - 1;
                if(index == -1)
                    index = 2;
            }
            prev = keyboardState;
            return this;
        }

        Texture2D pacSprite = GameTexture.pacmanOpenSprite;

        public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
        {
            spriteBatch.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);
            spriteBatch.Draw(GameTexture.levelBackgroundSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);

            spriteBatch.Draw(GameTexture.pauseSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);

            timeUp += gameTime.ElapsedGameTime.TotalSeconds;

            if (timeUp > 0.13f)
            {
                timeUp = 0;
                flag = flag ? false : true;
            }

            if (flag)
            {
                pacSprite = GameTexture.pacmanOpenSprite;
            }
            else
            {
                pacSprite = GameTexture.pacmanCloseSprite;
            }
            spriteBatch.Draw(pacSprite, new Vector2(ToX(270), ToY(index * 70 + 270)), new Rectangle(0, 0, 17, 19), Color.White, 0, new Vector2(ToX(8), ToY(10)), 1f, SpriteEffects.None, 0);
            spriteBatch.Draw(pacSprite, new Vector2(ToX(550), ToY(index * 70 + 270)), new Rectangle(0, 0, 17, 19), Color.White, 0, new Vector2(ToX(8), ToY(10)), 1f, SpriteEffects.FlipHorizontally, 0);
            
            spriteBatch.End();
        }
    }
}
