# system.py
#
# Explore variables the system knows
# Usage:
#      % python system.py arguments
#
# Jeff Parker, June 2013

import sys

print(f"Arguments:, {sys.argv}\n")

print(f"Platform: {sys.platform}\n")

print("Path:")
# Print each component in the path
for p in sys.path:
    print(p)