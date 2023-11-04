using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System.IO;

using Pac.Character;
using Pac.Constants;
using Pac.Resources;
using Pac.App;

namespace Pac.Scene 
{
    public class SummaryScene : BaseScene
    {
        Pacman pac;
        bool saved = false;
        string playerName = "";

        KeyboardState prevState;

        private static SummaryScene instance;

        public static SummaryScene GetInstance(Pacman pac)
        {
            if (instance == null)
            {
                instance = new SummaryScene();
            }
            instance.pac = pac;
            return instance;
        }

        private SummaryScene()
        {
        }

        public override BaseScene Update(GameTime gameTime)
        {
            prevState = keyboardState;
            keyboardState = Keyboard.GetState();
            if (!saved && pac.score > GameConstants.highScore)
            {
                foreach (Keys k in keyboardState.GetPressedKeys())
                {
                    if (prevState.IsKeyUp(k))
                    {
                        if (k.Equals(Keys.Enter))
                        {
                            GameConstants.highScore = pac.score;
                            GameConstants.playerName = playerName;
                            SaveHighScore();
                            saved = true;
                        }
                        else if (k.Equals(Keys.Space) && playerName.Length < 3)
                        {
                            playerName = playerName.Insert(playerName.Length, " ");
                        }
                        else if (k.Equals(Keys.Back) && playerName.Length > 0)
                        {
                            playerName = playerName.Remove(playerName.Length - 1, 1);
                        }
                        else
                        {
                            if(playerName.Length + k.ToString().Length <= 3 )
                                playerName += k.ToString();
                        }
                    }
                }
            }
            else if (keyboardState.IsKeyDown(Keys.Space))
            {
                int lvl = 0;
                saved = false;
                lvl = PacmanScene.GetInstance().level;
                if (pac.lives > 0)
                {
                    lvl++;
                    GameConstants.initMap();
                    PacmanScene.GetInstance().Initialize(lvl);
                    PacmanScene.GetInstance().pac.score = pac.score;
                    return PacmanScene.GetInstance();
                }
                else
                {
                    return MenuScene.GetInstance();
                }
            }
            else if (keyboardState.IsKeyDown(Keys.Escape))
            {
                return MenuScene.GetInstance();
            }
            return this;
        }

        private void SaveHighScore()
        {
            StreamWriter w = null;
            try
            {
                w = new StreamWriter("temp");
                w.Write(GameConstants.playerName+","+GameConstants.highScore + "");
                w.Close();
                FileSecurity.EncryptFile("temp", GameConstants.SAVE_FILE);
            }
            catch (FileNotFoundException e)
            {
            }
        }

        public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
        {
            spriteBatch.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);
            spriteBatch.Draw(GameTexture.levelBackgroundSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);
            if (!saved && pac.score > GameConstants.highScore)
            {
                spriteBatch.DrawString(GameTexture.spriteFont, "NEW HIGHSCORE !!", new Vector2(ToX(310), ToY(200)), Color.YellowGreen);
                spriteBatch.DrawString(GameTexture.spriteFont, "Enter your name :", new Vector2(ToX(350), ToY(300)), Color.YellowGreen);
                spriteBatch.DrawString(GameTexture.spriteFont, playerName, new Vector2(ToX(350), ToY(370)), Color.Red);
            }
            else if (pac.lives == 0)
            {
                spriteBatch.Draw(GameTexture.gameOverSprite, new Rectangle(ToX(250), ToY(200), ToX(300), ToY(100)), Color.White);
                spriteBatch.DrawString(GameTexture.spriteFont, "Press Space to go to main menu...", new Vector2(ToX(310), ToY(400)), Color.YellowGreen);
            }
            else
            {
                spriteBatch.Draw(GameTexture.levelCompleteSprite, new Rectangle(ToX(250), ToY(200), ToX(300), ToY(100)), Color.White);
                spriteBatch.DrawString(GameTexture.spriteFont, "Press Space to start next level...", new Vector2(ToX(300), ToY(400)), Color.YellowGreen);
            }
            spriteBatch.DrawString(GameTexture.spriteFont,"Score : "+pac.score,new Vector2(ToX(350),ToY(100)),Color.Yellow);
            spriteBatch.End();   
        }
    }
}
