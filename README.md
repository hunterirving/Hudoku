# Hudoku
It's not every day that a puzzle game comes along and changes the world forever.

And unless something else just dropped, today isn't one of those days.

But here's Hudoku to tide you over until then.

## You are Here

Each Hudoku board is a 21 x 21 grid filled with the numbers 1 through 4.

<img src="https://github.com/hunterirving/Hudoku/blob/master/hudokuboard.png">

Your goal is to travel from the upper-left corner to the bottom-right corner, moving in any of the four orthagonal directions (up, down, left, right) in increments equal to the number at your feet.

<img src="">

_"Now that's fun."_ - Hunter Irving, Hudoku Enthusiast

## Bet I Could Automate That

Say you're the Editor in Chief for a struggling local newspaper, and you've determined the cause of your waning viewership to be "Sudoku Fatigue".

You can use __HudokuGen.py__ to randomly generate "easy", "medium", and "hard" Hudoku boards and find their shortest possible solution using a breadth-first search algorithm.

<img src="https://github.com/hunterirving/Hudoku/blob/master/hudokusolution.png">

Boards with no solutions are automatically thrown out, but you might consider saving one to print in your April Fool's Day issue.

<img src="">

## BIG DATA

> _What percentage of randomly generated Hudokus have at least one solution?_

> _What is the average length of the shortest solution to a randomly generated Hudoku?_

> _What is the theoretical "longest shortest solution" a Hudoku could possess?_

Scholars have debated these topics for years, but until now we just had to wonder.

Use __HudokuTest.py__ to generate a number of boards that suits your fancy and/or available time.

<img src="https://github.com/hunterirving/Hudoku/blob/master/testresults.png">

On a dual-core craptop, 5000 trials took me just a few minutes.

## Final Thoughts

- Any path that travels from the start square to the end square is "a" solution
- ...but a board's "best" solution is its _shortest_ solution
- There may be multiple "best" solutions for a given board (if multiple solutions of the same (shortest) length exist)
- "Best" solutions are more likely to contain moves to the right and down (as these moves bring you closer to your final destination), but occasionally it is advantageous to move left or up (usually to land on a 3 or 4)
- The theoretical "shortest possible shortest solution" would be of length 10, and would be a path comprised entirely of 4's
- The theoretical "longest possible shortest solution"  would be of length 40, and would be a path comprised entirely of 1's (if any higher numbers were present they would save steps and be sought out by __HudokuGen__'s algorithm)
- The chances of such a board occuring randomly are smaller than your chances of winning the lottery



- The future of Hudoku is 3D (cubic) Hudoku
