import sys

G_list = [['A', 4.0], ['B', 3.0], ['C', 2.0], ['D', 1.0], [0], ['F', 0.0]]
grade = str(sys.stdin.readline().rstrip())

point = G_list[ord(grade[0])-65][1]

if grade[-1] == "+":
  point += 0.3
elif grade[-1] == "-":
  point -= 0.3

print(point)