# findLibrary.py
#
# Where is a Python Library defined
# Usage:
#      % python findLibrary turtle.py
#
# Jeff Parker, Sept 2019
#
# Bugs: this looks for the target as a prefix of filename

import os
import sys

from typing import Any


def traverse(dir: str, target: str) -> Any:
    "Is the command in this directory?"
    N = len(target)
    result = []
    try:
        # Loop over all files in this directory
        for w in os.listdir(dir):

            # Is it a match?
            if (target == w[:N]):
                result.append(os.path.join(dir, w))
    except IOError:
        return None

    return result


def which(target: str) -> str:
    "Get Python's path, and check each element in turn"

    path = sys.path

    # Look at each element
    for w in path:
        # Is the target there?
        res = traverse(w, target)
        if (res):
            return res

    return None


if (len(sys.argv) == 1):
    print("Usage: python which.py <command>")
else:
    res = which(sys.argv[1])
    if (res):
        for path in res:
            print(path)
