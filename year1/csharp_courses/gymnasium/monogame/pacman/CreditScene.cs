using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

using Pac.Resources;

namespace Pac.Scene
{
    /// <summary>
    /// Not working. Might not implement it.
    /// </summary>

    public class CreditScene : BaseScene
    {
        private static CreditScene instance;

        private BaseScene prevScene;

        public static CreditScene GetInstance(BaseScene prev)
        {
            if (instance == null)
            {
                instance = new CreditScene();
            }
            instance.prevScene = prev;
            return instance;
        }

        private CreditScene()
        {
        }

        public override BaseScene Update(GameTime gameTime)
        {
            keyboardState = Keyboard.GetState();

            if (keyboardState.IsKeyDown(Keys.Escape))
            {
                return prevScene;
            }

            return this;
        }

        public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
        {
            spriteBatch.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);
            spriteBatch.Draw(GameTexture.levelBackgroundSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);

            spriteBatch.Draw(GameTexture.creditsSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);

            spriteBatch.End();
        }
    }
}
