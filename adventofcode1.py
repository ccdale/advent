#!/usr/bin/env python3

import math
import sys

if len(sys.argv) > 1:
    fip = sys.argv[1]
else:
    print("{} requires a file".format(sys.argv[0]))
    sys.exit(1)

with open(fip, "r") as ifn:
    lines = ifn.readlines()

vals = []
for line in lines:
    val = int(line.strip())
    fuel = (math.floor(val / 3)) - 2
    print("{}: {}".format(val, fuel))
    vals.append(fuel)

print(sum(vals))
