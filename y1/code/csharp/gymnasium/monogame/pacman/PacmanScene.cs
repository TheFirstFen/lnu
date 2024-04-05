using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

using Pac.Character;
using Pac.Constants;
using Pac.App;
using Pac.Resources;
using Pac.GhostAlgorithm;
using Pac.Fuzzy;

namespace Pac.Scene
{
    public class PacmanScene : BaseScene
    {
        static int width = GameConstants.TEXTURE_WIDTH, height = GameConstants.TEXTURE_HEIGHT;

        public Pacman pac;
        Ghost[] ghosts = new Ghost[(int)GameConstants.SpeednScore.Max_No_Of_Ghosts];
        Texture2D pacSprite = GameTexture.pacmanOpenSprite;

        bool flag = true;
        float timeup;
        public int level = 0;

        private static PacmanScene instance;

        public static PacmanScene GetInstance()
        {
            if (instance == null)
            {
                instance = new PacmanScene();
                instance.Initialize(0);
            }
            return instance;
        }

        private static int prevSpeed;

        public void Initialize(int level)
        {
            this.level = level;
            if (level == 1) prevSpeed = (int)GameConstants.SpeednScore.Ghost_Speed - (int)GameConstants.SpeednScore.Speed_Inc;
            pac = new Pacman();
            int speed = prevSpeed + (int)GameConstants.SpeednScore.Speed_Inc;
            if (speed > pac.speed)
            {
                speed = (int)GameConstants.SpeednScore.Ghost_Speed;
                if(GameConstants.NO_OF_GHOSTS < (int)GameConstants.SpeednScore.Max_No_Of_Ghosts)
                    GameConstants.NO_OF_GHOSTS++;
            }
            prevSpeed = speed;
            for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
            {
                ghosts[i] = new Ghost(speed);
                ghosts[i].intializePosition(i);
            }

            Ghost.timeForScatter = -2;
            Game1.sound.Begin();
        }

        private PacmanScene()
        {
        }

        public static Point prev,now;

        public double scatterTime = 2;

        public override BaseScene Update(GameTime gameTime)
        {
            keyboardState = Keyboard.GetState();
            if (keyboardState.IsKeyDown(Keys.Escape))
            {
                return PauseScene.GetInstance(this);
            }

            if (pac.lives == 0 || GameConstants.pelletsLeft == 0)
            {
                pac.score += pac.lives * 100;
                BaseScene next = SummaryScene.GetInstance(pac);
                return next;
            }

            HandleKeyboardEvent();

            Ghost.timeForScatter -= gameTime.ElapsedGameTime.TotalSeconds;
            scatterTime -= gameTime.ElapsedGameTime.TotalSeconds;

            for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
            {
                if (ghosts[i].isAtIntersection())
                {
                    if (scatterTime <= 0)
                    {
                        if (pac.isPowerUpMode)
                        {
                            for (int j = 0; j < GameConstants.NO_OF_GHOSTS; j++)
                            {
                                ghosts[j].logic = ShyGhostAlgorithm.getInstance();
                                ghosts[j].logicString = "Shy";
                            }
                        }
                        else if (Ghost.timeForScatter <= 0)
                        {
                            for (int j = 0; j < GameConstants.NO_OF_GHOSTS; j++)
                            {
                                ghosts[j].logic = ScatterGhostAlgorithm.getInstance();
                                ghosts[j].logicString = "Scatter";
                            }
                            scatterTime = 1;     // Scatter for 2 seconds...
                            Ghost.timeForScatter += 4 + level + scatterTime; 
                        }
                        else
                        {
                            pac.lifetime = pac.totalTime / (GameConstants.NO_OF_LIVES - pac.lives + 1);
                            FuzzyController.getInstance().decideLogic(ghosts, i, pac);
                        }
                    }
                    ghosts[i].logic.moveGhost(ghosts, i, pac);
                }
            }

            HandleMovementAndCollision(gameTime);

            now = pac.getPoint();
            if (prev == null || (now.X != prev.X) || (now.Y != prev.Y))
            {
                pac.pelletEatenTime++;
                pac.totalTime++;
                prev = now;
            }

            if (pac.eatPellet())
            {
                for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
                {
                    // Eaten powerup
                    ghosts[i].changeDirection();
                }
            }

            return this;
        }

        private void HandleMovementAndCollision(GameTime gameTime)
        {
            Vector2 oldval;
            Vector2[] oldgval = new Vector2[GameConstants.NO_OF_GHOSTS];
            oldval = pac.bound;

            for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
            {
                oldgval[i] = ghosts[i].bound;
                ghosts[i].move(gameTime);
            }

            pac.move(gameTime);
            if (pac.isCollidingWithWall())
            {
                pac.bound = oldval;
            }
            Rectangle p = new Rectangle((int)pac.bound.X,(int) pac.bound.Y,(int) pac.width,(int) pac.height);
            for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
            {
                Rectangle r = new Rectangle((int)ghosts[i].bound.X,(int) ghosts[i].bound.Y,(int) ghosts[i].width,(int) ghosts[i].height);
                if (r.Intersects(p))
                {
                    if (pac.isPowerUpMode)
                    {
                        pac.score += (int)GameConstants.SpeednScore.Ghost_Eat_Score;
                        ghosts[i].intializePosition(i);
                        Game1.sound.Eat();
                    }
                    else
                    {
                        pac.bound = new Vector2(Pacman.init.X, Pacman.init.Y);
                        pac.speedX = pac.speedY = 0;
                        pac.lives--;
                        Game1.sound.Dead();
                        for (int j = 0; j < GameConstants.NO_OF_GHOSTS; j++)
                            ghosts[j].intializePosition(j);
                    }
                }
                if (ghosts[i].isCollidingWithWall())
                {
                    ghosts[i].bound = oldgval[i];
                }
            }
        }

        private void HandleKeyboardEvent()
        {
            if (keyboardState.IsKeyDown(Keys.Right))
            {
                pac.moveR();
            }
            else if (keyboardState.IsKeyDown(Keys.Left))
            {
                pac.moveL();
            }
            else if (keyboardState.IsKeyDown(Keys.Up))
            {
                pac.moveU();
            }
            else if (keyboardState.IsKeyDown(Keys.Down))
            {
                pac.moveD();
            }
        }

        public void HandleWrapAround()
        {
            int x1 = (int)(((pac.bound.X - 10) - 100) + 1) / GameConstants.TEXTURE_WIDTH;
            int y1 = (int)((pac.bound.Y - 9) + 1) / GameConstants.TEXTURE_HEIGHT;
            int x2 = (int)(((pac.bound.X - 10) - 100 + pac.width) + 1) / GameConstants.TEXTURE_WIDTH;

            if (pac.speedX > 0 && (x1 + 1 == 27) && y1 == 14)
            {
                pac.bound.X -= GameConstants.TEXTURE_WIDTH * 25;
            }
            if (pac.speedX < 0 && (x2 - 1 == 0) && y1 == 14)
            {
                pac.bound.X += GameConstants.TEXTURE_WIDTH * 25 - (GameConstants.TEXTURE_WIDTH - pac.width);
            }

            for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
            {
                x1 = (int)(((ghosts[i].bound.X - 10) - 100) + 1) / GameConstants.TEXTURE_WIDTH;
                y1 = (int)((ghosts[i].bound.Y - 9) + 1) / GameConstants.TEXTURE_HEIGHT;
                x2 = (int)(((ghosts[i].bound.X - 10) - 100 + ghosts[i].width) + 1) / GameConstants.TEXTURE_WIDTH;

                if (ghosts[i].speedX > 0 && (x1 + 1 == 27) && y1 == 14)
                {
                    ghosts[i].bound.X = ghosts[i].bound.X - GameConstants.TEXTURE_WIDTH * 25;
                }
                if (ghosts[i].speedX < 0 && (x2 - 1 == 0) && y1 == 14)
                {
                    ghosts[i].bound.X += GameConstants.TEXTURE_WIDTH * 25 - (GameConstants.TEXTURE_WIDTH-ghosts[i].width);
                }
            }
        }

        public override void Draw(GameTime gameTime, SpriteBatch spriteBatch)
        {
            spriteBatch.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);
            spriteBatch.Draw(GameTexture.levelBackgroundSprite, new Rectangle(ToX(0), ToY(0), ToX(800), ToY(600)), Color.White);
            DrawMap(spriteBatch);

            if (pac.powerUpTime > 0)
            {
                pac.powerUpTime -= gameTime.ElapsedGameTime.TotalSeconds;
            }
            else
            {
                pac.isPowerUpMode = false;
            }

            timeup += (float)gameTime.ElapsedGameTime.TotalSeconds;
            if (flag)
            {
                pacSprite = GameTexture.pacmanOpenSprite;
                for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
                {
                    int x = i % 4;
                    spriteBatch.Draw(GameTexture.ghostSprite, new Vector2(ToX(ghosts[i].bound.X), ToY(ghosts[i].bound.Y)), new Rectangle(0 + 21 * x * 2, 0, 21, 19), Color.White, MathHelper.ToRadians(0), new Vector2(ToX(8), ToY(10)), 1f, ghosts[i].spriteDirection, 0);
                }
            }
            else
            {
                pacSprite = GameTexture.pacmanCloseSprite;
                for (int i = 0; i < GameConstants.NO_OF_GHOSTS; i++)
                {
                    int x = i % 4;
                    if (pac.isPowerUpMode)
                        x = 4; 
                    spriteBatch.Draw(GameTexture.ghostSprite, new Vector2(ToX(ghosts[i].bound.X), ToY(ghosts[i].bound.Y)), new Rectangle(21 + 21 * 2 * x, 0,21,19), Color.White, MathHelper.ToRadians(0), new Vector2(ToX(8f), ToY(10f)),1f, ghosts[i].spriteDirection, 0);
                }
            }
            if (timeup > 0.13f)
            {
                timeup = 0;
                flag = flag ? false : true;
            }
            spriteBatch.Draw(pacSprite, new Vector2(ToX(pac.bound.X),ToY(pac.bound.Y)), new Rectangle(0, 0, 17, 19), Color.White, MathHelper.ToRadians(pac.angle),new Vector2(8f,10f), 1f, pac.spriteDirection, 0);

            spriteBatch.DrawString(GameTexture.spriteFont, "Score : " + pac.score, new Vector2(ToX(700), ToY(100)), Color.Yellow);

            spriteBatch.DrawString(GameTexture.spriteFont, "Best : ", new Vector2(ToX(700), ToY(150)), Color.Yellow);
            spriteBatch.DrawString(GameTexture.spriteFont, GameConstants.playerName + " - " +GameConstants.highScore, new Vector2(ToX(700), ToY(180)), Color.Red);

            spriteBatch.DrawString(GameTexture.spriteFont, "Pellets : " + GameConstants.pelletsLeft, new Vector2(ToX(700), ToY(300)), Color.Yellow);

            spriteBatch.DrawString(GameTexture.spriteFont, "Level - " + this.level, new Vector2(ToX(10), ToY(400)), Color.Yellow);

            spriteBatch.DrawString(GameTexture.spriteFont, "LIVES", new Vector2(ToX(710), ToY(450)), Color.Yellow);

            for (int i = 0; i < pac.lives; i++)
            {
                spriteBatch.Draw(GameTexture.pacmanOpenSprite, new Rectangle(ToX(700+i*30),ToY(500),ToX(30),ToY(30)), Color.White);
            }
            spriteBatch.End();   
        }

        private void DrawMap(SpriteBatch spriteBatch)
        {
            for (int i = 0; i < 31; i++)
            {
                for (int j = 0; j < 28; j++)
                {
                    Rectangle rect = new Rectangle(ToX(100 + j * (width)-1), ToY(0 + i * (height)-1), ToX(width+1), ToY(height+1));

                    if (GameConstants.MAP[i, j] == GameConstants.MAP_WALL)
                    {
                        spriteBatch.Draw(GameTexture.wallSprite, rect, Color.White);
                    }
                    else
                    {
                        spriteBatch.Draw(GameTexture.pathSprite, rect, Color.White);
                        if (GameConstants.MAP[i, j] == GameConstants.MAP_PELLET)
                        {
                            spriteBatch.Draw(GameTexture.pelletSprite, rect, Color.White);
                        }
                        else if (GameConstants.MAP[i, j] == GameConstants.MAP_POWERUP)
                        {
                            spriteBatch.Draw(GameTexture.powerupSprite, rect, Color.White);
                        }
                    }
                }
            }
        }
    }
}
