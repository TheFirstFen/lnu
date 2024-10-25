using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

using Pac.Constants;
using Pac.Resources;
using Pac.App;

namespace Pac.Scene
{ 
    public class MenuScene : BaseScene
    {
        private static MenuScene instance;
        private double timeUp = 0;

        private static int index = 0;
        private static bool flag;

        public static MenuScene GetInstance()
        {
            if (instance == null)
            {
                instance = new MenuScene();
            }
            return instance;
        }

        private MenuScene()
        {
            Game1.sound.Begin();
        }

        KeyboardState prev;
        bool up = false;

        public override BaseScene Update(GameTime gameTime)
        {
            keyboardState = Keyboard.GetState();

            if(keyboardState.IsKeyUp(Keys.Enter))
                up = true;

            if(up&&keyboardState.IsKeyDown(Keys.Enter))
            {
                up = false;
                if (index == 0)
                {
                    if (GameConstants.isIndexed)
                    {
                        GameConstants.initMap();
                        PacmanScene.GetInstance().Initialize(1);
                        return PacmanScene.GetInstance();
                    }
                    return LoadingScene.GetInstance();
                }
                else
                    return null;
            }

            if(keyboardState.IsKeyDown(Keys.Down) && (prev==null || prev.IsKeyUp(Keys.Down)))
            {
                index = (index + 1) % 4;
            }
            else if (keyboardState.IsKeyDown(Keys.Up) && (prev == null || prev.IsKeyUp(Keys.Up)))
            {
                index = index - 1;
                if(index == -1)
                    index = 3;
            }
            prev = keyboardState;
            return this;
        }

        Texture2D pacSprite = GameTexture.pacmanOpenSprite;

        public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
        {
            spriteBatch.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);
            spriteBatch.Draw(GameTexture.levelBackgroundSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);

            spriteBatch.Draw(GameTexture.menuSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);

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
            spriteBatch.Draw(pacSprite, new Vector2(ToX(280), ToY(index * 65 + 290)), new Rectangle(0, 0, 17, 19), Color.White, 0, new Vector2(ToX(8), ToY(10)), 1f, SpriteEffects.None, 0);
            spriteBatch.Draw(pacSprite, new Vector2(ToX(540), ToY(index * 65 + 290)), new Rectangle(0, 0, 17, 19), Color.White, 0, new Vector2(ToX(8), ToY(10)), 1f, SpriteEffects.FlipHorizontally, 0);
            
            spriteBatch.End();
        }
    }
}
