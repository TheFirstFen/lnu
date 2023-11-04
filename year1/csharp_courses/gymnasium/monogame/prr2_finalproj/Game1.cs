using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System;
using System.Collections.Generic;

namespace Breakout
{
    /// <summary>
    /// This is the main type for your game.
    /// </summary>
    public class Game1 : Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;
        Paddle paddle;
        Ball ball;
        Rectangle screen;
        List<Brick> bricks = new List<Brick>();

        int screenWidth = 410;
        int screenHeight = 600;

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
            graphics.PreferredBackBufferWidth = screenWidth;
            graphics.PreferredBackBufferHeight = screenHeight;

            screen = new Rectangle(0, 0, graphics.PreferredBackBufferWidth, graphics.PreferredBackBufferHeight);
        }

        /// <summary>
        /// Allows the game to perform any initialization it needs to before starting to run.
        /// This is where it can query for any required services and load any non-graphic
        /// related content.  Calling base.Initialize will enumerate through any components
        /// and initialize them as well.
        /// </summary>
        protected override void Initialize()
        {
            // TODO: Add your initialization logic here

            base.Initialize();
        }

        /// <summary>
        /// LoadContent will be called once per game and is the place to load
        /// all of your content.
        /// </summary>
        protected override void LoadContent()
        {
            // Create a new SpriteBatch, which can be used to draw textures.
            spriteBatch = new SpriteBatch(GraphicsDevice);

            paddle = new Paddle(Content.Load<Texture2D>("Paddle"), screen);

            ball = new Ball(Content.Load<Texture2D>("Ball"), Vector2.Zero, screen);

            Start();
        }

        private void Start()
        {
            ball.StartPos(paddle);

            for (int i = 0; i < 8; i++)
            {
                for (int j = 0; j < 5; j++)
                {
                    Texture2D brickTexture = Content.Load<Texture2D>("Brick");
                    int brickOffset = 10;

                    bricks.Add(new Brick(brickTexture, new Vector2((i * brickTexture.Width) + ((i + 1) * brickOffset), (j * brickTexture.Height) + ((j + 1) * brickOffset)), screen));
                }
            }

            ball.IsGameOver = false;
        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// game-specific content.
        /// </summary>
        protected override void UnloadContent()
        {
            
        }

        /// <summary>
        /// Allows the game to run logic such as updating the world,
        /// checking for collisions, gathering input, and playing audio.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Update(GameTime gameTime)
        {
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
                Exit();

            paddle.Update(gameTime);
            ball.Update(gameTime);
            ball.PaddleRebound(paddle);

            foreach (Brick b in bricks)
            {
                b.Update(gameTime);
            }

            for (int k = 0; k < bricks.Count; k++)
            {
                Brick b = bricks[k];

                if (ball.spriteBox.Intersects(b.spriteBox))
                {
                    bricks.RemoveAt(k);
                    ball.BrickRebound(b);
                    k--;
                }
            }

            if (ball.IsGameOver)
            {
                Start();
            }

            Console.WriteLine(bricks.Count);

            base.Update(gameTime);
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.Black);

            spriteBatch.Begin();

            paddle.Draw(spriteBatch);
            ball.Draw(spriteBatch);

            foreach (Brick b in bricks)
            {
                b.Draw(spriteBatch);
            }

            spriteBatch.End();

            base.Draw(gameTime);
        }
    }
}
