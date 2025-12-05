import sys
import os
import time

if len(sys.argv) != 4 and len(sys.argv) != 5:
	print("Usage: python ./scripts/day.py <day> <part> <input> [debug]")
	print("  day: 1-12")
	print("  part: 1 or 2 or custom")
	print("  input: i or ii")
	print("  debug: (optional) p or d or debug")
	sys.exit(1)

try:
	day = int(sys.argv[1])
	if not 1 <= day <= 12:
		raise ValueError("Day must be between 1 and 12")
except ValueError as e:
	print(f"Error: {e}")
	sys.exit(1)

custom_file = None
try:
	part = sys.argv[2]
	if part not in ["1", "2"]:
		part = sys.argv[2]
		custom_file = f"day{day:02d}/{part}.py"
		if not os.path.exists(custom_file):
			raise ValueError(f"Part must be 1, 2, or a valid custom file name ('{custom_file}' not found)")
except ValueError as e:
	print(f"Error: {e}")
	sys.exit(1)

input_type = sys.argv[3]
if input_type not in ['i', 'ii']:
	print("Error: Input must be 'i' or 'ii'")
	sys.exit(1)

should_debug = len(sys.argv) == 5 and (sys.argv[4] in ("d", "p", "debug", "print"))
if should_debug:
	os.environ["AOC_DEBUG"] = "on"

print(f"\nDay {day} | Qn {part} | Input {input_type.upper()}")

# read input file and report if missing
input_file_path = f"day{day:02d}/__input-{input_type}.txt"
f = open(input_file_path, 'r')
input_data = f.read().strip()
f.close()
if not input_data:
	print(f"Error: Input file {input_file_path} is empty or missing.")
	sys.exit(1)

module_name = f"day{day:02d}.{part}" if custom_file is not None else f"day{day:02d}.q{part}"
try:
	day_module = __import__(module_name, fromlist=[''])
	solve_function = getattr(day_module, "solve")
	timestart = time.perf_counter_ns()
	result = solve_function(input_data)
	print(f"\nResult: {result}")
	timend = time.perf_counter_ns()
	print(f"Time taken: {(timend - timestart) / 1e6} ms")

except ImportError as e:
	print(f"Error importing module {module_name}: {e}. Make sure to bind pythonpath.")
	sys.exit(1)
