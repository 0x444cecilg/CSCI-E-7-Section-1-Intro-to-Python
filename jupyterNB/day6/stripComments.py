# stripComments.py
#
# Remove (some) comments from a file
# Usage:
#      $ python stripComments.py old new
#
# Based on sample from Downey, Think Python
#
# Revised, Jeff Parker, July 2018

import sys


def filterFile(oldFile: str, newFile: str):
    """Take lines from old file and write to new:
       Don't copy lines that start with '#'"""

    with open(oldFile, 'r') as old:
        with open(newFile, 'w') as new:

            # For each line of the old file
            for text in old:

                # If it isn't a comment, copy to new file
                if text[0] != '#':
                    new.write(text)


# Check the command line parameters
if (len(sys.argv) != 3):
    print(f'Usage: python {sys.argv[0]} <old> <new>')
else:
    # Filter old to make new
    filterFile(sys.argv[1], sys.argv[2])
