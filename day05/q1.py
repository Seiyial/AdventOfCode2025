
def solve(input_data: str) -> str | int | float:
	top, bottom = tuple(input_data.split('\n\n'))
	fresh_ranges = [
		(int(a), (int(b)))
		for a, b in map(lambda ln: tuple(ln.split("-")), top.splitlines())
	]
	return sum([
		1 if any(ing_id >= a and ing_id <= b for a, b in fresh_ranges) else 0
		for ing_id in map(lambda x: int(x), bottom.splitlines())
	])
