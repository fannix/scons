"""
Utility for preprocessing data
"""

import sys

def preprocess_lines(raw_lines):
    """
    Preprocessraw data files.


    Parameters
    ----------
    raw_lines: original lines

    Returns
    -------
    Processed line
    """
    processed_lines = []
    lines = raw_lines[9:]
    for e in lines:
        li = e.split()
        _, _, mean, _ = li[:4]
        sentence = " ".join(li[4:])
        if float(mean) < -0.05:
            processed_lines.append(str(-1)+"\t"+sentence)
        elif float(mean) > 0.05:
            processed_lines.append(str(1)+"\t"+sentence)

    return processed_lines

if __name__ == "__main__":
    lines = []
    for e in sys.stdin:
        lines.append(e)
    print preprocess_lines(lines)
