def solve(input_data: str) -> None:
	nums = set()
	for row in input_data.split(","):
		start, end = tuple([ int(val) for val in row.split("-") ])
		for num in range(start, end + 1):
			nums.add(num) if repetitive(num) else None
	return sum(nums)

def repetitive(num: int):
	s = str(num)
	length = len(s)
	
	for i in range(1, int(length / 2) + 1):

		if length % i != 0:
			continue

		first = s[0:i]
		ok = True

		for j in range(1, int(length / i)):
			cur = s[(j * i):((j + 1) * i)]
			ok = cur == first
			if not ok:
				break

		if ok:
			return True
		
	return False

