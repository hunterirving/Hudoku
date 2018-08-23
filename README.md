# Hudoku
It's not every day that a puzzle game comes along and changes the world forever.

And unless something else just dropped, today isn't one of those days.

But here's Hudoku to tide you over until then.

## You are Here

Each Hudoku board is a 21 x 21 grid filled with the numbers 1 through 4.

<img src="">

Your goal is to travel from the upper-left corner to the bottom-right corner, moving in any of the four orthagonal directions (up, down, left, right) in increments equal to the number at your feet.

<img src="">

_"Now that's fun."_ - Hunter Irving, Hudoku Enthusiast

## Bet I Could Automate That

Say you're the Editor in Chief for a struggling local newspaper, and you've determined the cause of your waning viewership to be "Sudoku Fatigue".

You can use __HudokuGen.py__ to randomly generate "easy", "medium", and "hard" Hudoku boards and find their shortest possible solution using a breadth-first search algorithm.

<img src="">

Boards with no solutions are automatically thrown out, but you might consider saving one to print in your April Fool's Day issue.

<img src="">

## BIG DATA

> _What percentage of randomly generated Hudokus have at least one solution?_

> _What is the average length of a randomly generated Hudoku's shortest solution?_

> _What is the theoretical "longest shortest solution" a Hudoku could possess?_

Scholars have debated these topics for years, but until now we just had to wonder.

Use __HudokuTest.py__ to generate a number of boards that suits your fancy and/or available time.

<img src="https://github.com/hunterirving/Hudoku/blob/master/testresults.png">

On a dual-core craptop, 5000 trials took me just a few minutes.

## Final Thoughts

- Any path that travels from the start square to the end square is "a" solution
- ...But a board's _shortest_ solution is its "best" solution
- There can be multiple "best" solutions for a given board (if multiple solutions of the same (shortest) length exist)
- "Best" solutions are more likely to contain moves to the right and down and less likely to contain moves to the left and up (as these moves take you further from your final destination)
- The theoretical "longest possible shortest solution" would involve a board of all 1's (if any higher numbers were present they would save steps and be sought out by the algorithm)
- The chances of such a board occuring randomly are smaller than your chances of winning the lottery

- The future of Hudoku is 3D (cubic) Hudoku
