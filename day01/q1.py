from .shared import Knob

def solve(input_data: str) -> None:
	lines: list[str] = input_data.splitlines()

	knob = Knob()
	for line in lines:
		direction = line[0:1]
		distance = line[1:]
		movement = int(distance) if direction == "R" else -int(distance)
		knob.add(movement)

	return knob.hit_0_times
