import sys
from pathlib import Path
import os

if len(sys.argv) != 2:
	print("Usage: python ./scripts/create_day.py <day_number> || pyx create-day <day_number>")
	sys.exit(1)

day_number = sys.argv[1]
try:
	day_int = int(day_number)
	if day_int < 1 or day_int > 25:
		raise ValueError()
except ValueError:
	print("Day number must be an integer between 1 and 25.")
	sys.exit(1)

day_int = int(day_number)
day_dir = f"day{day_int:02d}"

project_dir = Path(__file__).parent.parent
day_dir_full = project_dir / day_dir

# ensure day_dir is created
os.makedirs(day_dir_full, exist_ok=True)

# create __init__.py
init_file = day_dir_full / "__init__.py"
if not init_file.exists():
	init_file.touch()

# Create input placeholder files
for input_type in ["i", "ii"]:
	input_file = day_dir_full / f"__input-{input_type}.txt"
	if not input_file.exists():
		input_file.touch()

# create solution file
for part in [1, 2]:
	solution_file = day_dir_full / f"q{part}.py"
	if not solution_file.exists():
		with open(solution_file, 'w') as f:
			f.write(f"""def solve(input_data: str) -> str | int | float:
	pass
""")