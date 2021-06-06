# 2048

2048 Game built using tkinter. The game comes with integrated AI which uses the **Monte Carlo Tree Search** algorithm to find the best possible move at any given step.

![2048](https://user-images.githubusercontent.com/78139798/120931638-20e1b880-c710-11eb-9650-6c2d065b9b35.gif)


## How to play:
- Make sure you have tkinter module.
  ```sh
    pip install tk
  ```
- Clone this repository.
  ```sh
    git clone https://github.com/akshat-rawat/2048.git
  ```
- Start the game and use “a”, “w”, “s” and “d” keys to move tiles left, up, down and right respectively.
  ```sh
    python main.py
  ```
- Get to 2048 and you win.
- However, you can also fire up the AI to solve the game for you.
- Just click the “i” key and the AI will start right up.

## File description
  * `constants.py` initializes required constants.
  * `ai_logic.py` implements MCTS for AI.
  * `logic.py` contains the functionality of the game.
  * `main.py` compiles of all the module and frontend for the game.
