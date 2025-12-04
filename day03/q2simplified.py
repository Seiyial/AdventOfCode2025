def solve_03_2(input_data: str) -> str | int | float:
	lines = input_data.split("\n")
	sum = 0
	for line in lines:
		list_of_ints = [ int(x) for x in line ]
		sum += max_twelveplet(list_of_ints)
	return sum

def max_twelveplet(line: list[int]) -> int:

	# [ 6 9 5 9 2 6 7 2 2 2 6 4 ]
	# picking first digit: we pick the first instance of the highest digit where there is enough on the right.
	# Why? because 9111 > 8999. First digit being highest always wins no matter what digit comes later.
	# As long as we pick the highest digit and there is enough we are correct.
	# Same principles apply for every subsequent number:
	# ie. 2911 > 2899. So at every successive digit we pick the highest possible as long as there is enough digits for the rest.
	# Therefore on picking digit 2 of 4:
	# [ x Y a a a a a a a a a N N ]
	# we need to omit N digits on the right for the choice
	# and we omit everything on the left of the last chosen digit (Y).
	# everything else (a) is fair play. Even the last (a), if it is highest, is the correct answer,
	# because if the last (a) is a 9, 2911 > 2899. It doesn't matter what the rest of the digits are.
	
	i = 12
	last_idx = 0
	numlist = ""
	while i > 0:
		# idx of first (a)
		look_from_idx = last_idx + 1
		# idx of first (N). in python, if we use this below, first N is excluded, therefore the sublist is only all the (a)s
		look_until_idx = len(line) - (i-1)
		avail_range = line[look_from_idx:look_until_idx] # this is a python slice fn that extracts look_from_idx till Not including look_until_idx
		val = max(avail_range)

		# set the new left bound
		last_idx = avail_range.index(val) + last_idx
		numlist += str(val)
		i -= 1
	
	return int(numlist)

