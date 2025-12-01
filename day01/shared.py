from common import aocdebug

class Knob:

	position: int
	hit_0_times: int = 0
	count_on_passing_0: bool

	def __init__(self, position: int = 50, count_on_passing_0: bool = False) -> None:
		self.position = position
		self.count_on_passing_0 = count_on_passing_0

	def add(self, delta: int) -> None:
		start_pos = 100 if self.position == 0 and delta < 0 else self.position

		starts_at_0 = self.position == 0
		ends_at_0 = ((delta + start_pos) % 100) == 0
		full_spins = (abs(delta) // 100) if self.count_on_passing_0 else 0
		effective_move = self.signed_clamp(delta)
		effective_end_pos = start_pos + effective_move
		aocdebug.print("delt {} eff {}".format(delta, effective_move))
		effective_move_does_cross = not ends_at_0 and \
			self.count_on_passing_0 and \
			(effective_end_pos > 100 or effective_end_pos < 0) # not incl. end

		if starts_at_0 and ends_at_0:
			self.position = self.normalise(effective_end_pos)
			self.hit_0_times += full_spins
			self.debugprint(delta, 0, 0, full_spins, False, False)
			return

		crosses = full_spins + \
			(1 if effective_move_does_cross else 0) + \
			(1 if ends_at_0 else 0)

		self.position = self.normalise(effective_end_pos)
		self.debugprint(delta, start_pos, effective_end_pos, full_spins,
			effective_move_does_cross, ends_at_0)
		self.hit_0_times += crosses

	def normalise(self, pos: int):
		cl = pos
		while cl < 0:
			cl += 100
		while cl >= 100:
			cl -= 100
		return cl
	
	def signed_clamp(self, val: int):
		c = val
		while c < -100:
			c += 100
		while c > 100:
			c -= 100
		return c

	def debugprint(self, delta: int, start_pos: int, end_pos: int, full_spins: int, 
		effective_move_cross: bool, ends_at_0: bool
	):
		out = f"{str(start_pos).rjust(3)} -> {str(end_pos).rjust(3)}"
		if full_spins > 0:
			out = f"{out} ({full_spins} fs)"
		if effective_move_cross:
			out = f"{out} (cross)"
		if ends_at_0:
			out = f"{out} (end)"

		if delta < 0:
			out = f"L{str(abs(delta)).rjust(3)} - {out}"
		elif delta > 0:
			out = f"R{str(abs(delta)).rjust(3)} - {out}"
		aocdebug.print(out)