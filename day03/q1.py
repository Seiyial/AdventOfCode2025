def solve(input_data: str) -> str | int | float:
	return sum(max_pair([int(x) for x in list(line)]) for line in input_data.splitlines())

def max_pair(line: list[int]) -> int:
	# print(line)
	# first number is highest number in the list excepting the last position (since it requires num after it)
	num_left = max(line[0:(len(line) - 1)])
	num_left_idx = line.index(num_left)
	# second number is highest number out of all the numbers after num_left_idx
	num_right = max(line[(num_left_idx + 1):])
	val = int(f"{num_left}{num_right}")
	# print(val)
	return val