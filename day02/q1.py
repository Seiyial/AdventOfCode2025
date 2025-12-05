def solve(input_data: str) -> str:
	nums = set()
	for row in input_data.split(","):
		start, end = tuple([ int(val) for val in row.split("-") ])
		for num in range(start, end + 1):
			nums.add(num) if symmetrical(num) else None
	return sum(nums)

def symmetrical(num: int):
	s = str(num)
	length = len(s)
	halflength = int(length / 2)
	return length % 2 == 0 and s[0:halflength] == s[halflength:length]
