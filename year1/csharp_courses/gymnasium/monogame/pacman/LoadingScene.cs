using System.Threading;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

using Pac.Constants;
using Pac.Index;
using Pac.Resources;

namespace Pac.Scene
{
    public class InitThread
    {
        public void Init()
        {
            GameConstants.initMap();
            PathIndexer.StartIndexing();
        }
    }

    public class LoadingScene : BaseScene
    {
        public static bool flag = false;
        Thread oThread;
        float timeup = 0;
        bool show = false;

        private static LoadingScene instance = null;

        private LoadingScene() { }

        public static LoadingScene GetInstance()
        {
            if (instance == null)
                instance = new LoadingScene();
            return instance;
        }

        public override BaseScene Update(GameTime gameTime)
        {
            keyboardState = Keyboard.GetState();
            if (!flag)
            {
                oThread = new Thread(new ThreadStart(new InitThread().Init));
                oThread.Start();
                flag = true;
                while(!oThread.IsAlive);
            }
            if(!oThread.IsAlive)
            {
                if (keyboardState.IsKeyDown(Keys.Space))
                {
                    GameConstants.isIndexed = true;
                    GameConstants.initMap();
                    PacmanScene.GetInstance().Initialize(1);
                    return PacmanScene.GetInstance();
                }
            }
            return this;
        }

        public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
        {
            timeup += (float)gameTime.ElapsedGameTime.TotalSeconds;
            spriteBatch.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);
            spriteBatch.Draw(GameTexture.levelBackgroundSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);
            spriteBatch.Draw(GameTexture.startScreenSprite, new Rectangle(ToX(250), ToY(150), ToX(300), ToY(300)), Color.White);
            if (timeup > 0.5f)
            {
                timeup = 0;
                show = show?false:true;
            }
            if (show)
            {
                if (oThread != null && oThread.IsAlive)
                {
                    spriteBatch.DrawString(GameTexture.spriteFont, "Loading...", new Vector2(ToX(370), ToY(500)), Color.Yellow);
                }
                else
                {
                    spriteBatch.DrawString(GameTexture.spriteFont, "Press Space to start...", new Vector2(ToX(350), ToY(500)), Color.Yellow);
                }
            }
            spriteBatch.End();   
        }

    }
}
