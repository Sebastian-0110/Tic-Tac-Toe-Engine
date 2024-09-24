
# Tic Tac Toe Engine

![Image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![Image](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![Image](https://badgen.net/pypi/v/tic-tac-toe-engine)


Implementation of the rules of the game "Tic tac toe".

This project can be use as:
- An engine for a game (Both CLI and paired with a game library like Pygame).
- A tool for AI training.

This project implements all the logic needed to play the tic tac toe game.

Example usage (a CLI implementation):

```python
from engine import Engine
from typing import Union


def print_board(board: list[Union[str, None]]) -> None:
	""" Print the board """	

	rows = []

	for i in range(0, 9, 3):
		for j in range(i, i + 3):
			

	rows = [
		" | ".join(board[i] for i in range(j, j + 3))
		for j in range(0, 9, 3)
	]



engine = Engine()

while True:
	print_board(engine.board)
	print(f"\n{engine.current_player} moves.")
	move = int(input("Enter your move (0 - 8): "))

	engine.play_move(move)

	if engine.is_over():
		if engine.is_tie():
			print("It's a tie")

		else:
			print(f"{engine.winner} wins!")

		print_board(engine.board) # Print again to reflect the winning case
		break

```
