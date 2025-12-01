import os
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
	from _typeshed import SupportsWrite

def debugging():
	return os.environ.get("AOC_DEBUG") == "on"

orig_print = print

def print(
	*values: object,
	sep: str | None = " ",
	end: str | None = "\n",
	# file: SupportsWrite[str] | None = None,
	flush: Literal[False] = False
):
	if debugging():
		orig_print(*values, sep, end, flush)