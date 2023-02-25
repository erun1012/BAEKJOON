import sys
from collections import deque

g_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D+', 'D0', 'D-', 'F']
G_deque = deque(['A', 4.0], ['B', 4.0], ['C', 4.0], ['D', 4.0], ['F', 0.0])
grade = str(sys.stdin.readline().rstrip())

