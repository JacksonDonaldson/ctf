
import sys
from befunge import read_in, befunge

code = input('>>>')

if len(code) > 48:
  print('this is misc, not pwn. no buffer overflow plz')
  sys.exit(1)

START_R = 4
START_C = 6

GRID = read_in('provided_file.txt')

for i, c in enumerate(code):
  GRID[START_R + (i // 16)][START_C + (i % 16)] = c

befunge(GRID)
