from collections import Counter

def solve(input_data: str) -> str | int | float:
	
	aoa = AOA([ list(rowstr) for rowstr in input_data.splitlines() ])
	num_removed = 0
	while True:
		num_removed_this_round = 0
		for y, row in enumerate(aoa.data):
			for x, cell in enumerate(row):
				if cell != "@": continue
				# print(f"{x}, {y}")
				if Counter([
					aoa.get(y-1, x-1), aoa.get(y-1, x), aoa.get(y-1, x+1),
					aoa.get(y, x-1),                      aoa.get(y, x+1),
					aoa.get(y+1, x-1), aoa.get(y+1, x), aoa.get(y+1, x+1)
				]).get("@", 0) < 4:
					num_removed_this_round += aoa.remove(y, x)
		
		if num_removed_this_round > 0: num_removed += num_removed_this_round
		else: break
	return num_removed

class AOA:

	data: list[list[str]]
	max_y: int
	max_x: int
	def __init__(self, data: list[list[str]]):
		self.max_y = len(data) - 1
		self.max_x = len(data[0]) - 1
		self.data = data

	def get(self, y_idx: int, x_idx: int) -> str | None:
		if y_idx < 0 or x_idx < 0: return None
		if y_idx > self.max_y or x_idx > self.max_x: return None
		return self.data[y_idx][x_idx]
		
	def remove(self, y_idx: int, x_idx: int) -> int:
		if y_idx < 0 or x_idx < 0: return None
		if y_idx > self.max_y or x_idx > self.max_x: return None
		self.data[y_idx][x_idx] = "x"
		return 1
