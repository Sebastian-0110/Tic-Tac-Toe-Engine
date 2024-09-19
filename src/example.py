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