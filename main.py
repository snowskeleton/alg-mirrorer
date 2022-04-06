#!/usr/bin/env python3

import sys
from funcs import invert

for line in sys.stdin:
	answer = invert(line)
	print(answer, file = sys.stdout)
