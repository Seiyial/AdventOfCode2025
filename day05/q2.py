def solve(input_data: str) -> str | int | float:
	ranges = list(
		tuple(map(int, row.split("-"))) for row in \
		input_data.split("\n\n")[0].splitlines()
	)
	valid_ranges = []
	print(ranges)
	i = 0
	while True:
		if i >= len(ranges): break
		start, end = ranges[i]
		print(f"att {start}~{end}")
		cur_start = start
		cur_end = end
		drop = False
		for comp_start, comp_end in valid_ranges:
			if cur_end < comp_start: continue # comp is fully outside on right
			elif cur_start > comp_end: continue # comp is fully outside on left
			elif cur_start >= comp_start and cur_end <= comp_end: drop = True # comp is fully surrounding
			elif cur_start >= comp_start:
				cur_start = comp_end + 1 # comp takes out left chunk only
				print(f"  against {comp_start}~{comp_end}: removeleft, start from {cur_start} instead")
			elif cur_end <= comp_end:
				cur_end = comp_start - 1 # still usable botside
				print(f"  against {comp_start}~{comp_end}: removeright, end at {cur_end} instead")
			else:
				right_chunk_start = comp_end + 1
				right_chunk_end = cur_end
				print(f"  against {comp_start}~{comp_end}: split open into {cur_start}~{comp_start - 1} and (new) {right_chunk_start}~{right_chunk_end}")
				ranges.append((comp_end + 1, cur_end))
				cur_end = comp_start - 1
			if drop:
				print(f"  against {comp_start}~{comp_end}: gone")
				break
		if not drop:
			print(f" ok {cur_start}~{cur_end}")
			valid_ranges.append((cur_start, cur_end))
		i += 1
	return sum(b - a + 1 for a, b in valid_ranges)
