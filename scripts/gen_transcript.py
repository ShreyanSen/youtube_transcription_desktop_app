


import argparse
import webvtt
from pathlib import Path

parser = argparse.ArgumentParser(description='Argument Parser Example')
parser.add_argument('-i', '--input', help='Input file or directory', required=True)
parser.add_argument('-o', '--output', help='Output file or directory', required=True)
args = parser.parse_args()

vtt = webvtt.read(args.input)
transcript = ""

lines = []
for line in vtt:
    # Strip the newlines from the end of the text.
    # Split the string if it has a newline in the middle
    # Add the lines to an array
    lines.extend(line.text.strip().splitlines())

# Remove repeated lines
previous = None
for line in lines:
    if line == previous:
       continue
    transcript += "\n" + line
    previous = line

# print(transcript)
Path(args.output).write_text(transcript)
