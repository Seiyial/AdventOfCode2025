def solve(input_data: str) -> str | int | float:
	ranges = list(
		tuple(map(int, row.split("-"))) for row in \
		input_data.split("\n\n")[0].splitlines()
	)
	print(ranges)
	merged_ranges: list[tuple[int, int]] = []
	i = 0
	did_merge = False
	while True:
		while i < len(ranges):
			start, end = ranges[i]
			j = 0
			add_own = True
			while j < len(merged_ranges):
				cmp_start, cmp_end = merged_ranges[j]
				if cmp_start < end or start > cmp_end:
					j += 1
					continue
				add_own = False
				did_merge = True
				merged_ranges[j] = min(cmp_start, start), max(cmp_end, end)
				break
			if add_own:
				merged_ranges.append((start, end))
			i += 1
		if not did_merge:
			ranges = merged_ranges
			merged_ranges = []
		else: break # keep merging until no need to
	return sum(b - a + 1 for a, b in merged_ranges)
