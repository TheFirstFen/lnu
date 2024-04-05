using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

using Pac.Resources;

namespace Pac.Scene
{
    /// <summary>
    /// Not working. Might not implement it.
    /// </summary>
    
    public class InstructionScene : BaseScene
    {
        private static InstructionScene instance;

        private BaseScene prevScene;

        public static InstructionScene GetInstance(BaseScene prev)
        {
            if (instance == null)
            {
                instance = new InstructionScene();
            }
            instance.prevScene = prev;
            return instance;
        }

        private InstructionScene()
        {
        }

        public override BaseScene Update(GameTime gameTime)
        {
            keyboardState = Keyboard.GetState();

            if (keyboardState.IsKeyDown(Keys.Escape))
            {
                return prevScene;
            }
            if(keyboardState.IsKeyDown(Keys.Space))
            {
                return prevScene;
            }

            return this;
        }

        public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
        {
            spriteBatch.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);
            spriteBatch.Draw(GameTexture.levelBackgroundSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);

            spriteBatch.Draw(GameTexture.instructionSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);

            spriteBatch.DrawString(GameTexture.spriteFont, "Press Space to Go back...", new Vector2(ToX(350),ToY(550)), Color.Yellow);

            spriteBatch.End();
        }
    }
}
