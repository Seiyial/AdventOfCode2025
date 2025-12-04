def solve_03_2(input_data: str) -> str | int | float:
	return sum(max_twelveplet([int(x) for x in list(line)]) for line in input_data.splitlines())

def max_twelveplet(line: list[int]) -> int:
	
	i = 12
	last_idx = 0
	numlist = ""
	while i > 0:
		avail_range = line[last_idx:(len(line) - (i - 1))] # we must reserve i-1 more spaces
		val = max(avail_range)
		last_idx = avail_range.index(val) + 1 + last_idx
		numlist += str(val)
		i -= 1
	
	return int(numlist)

