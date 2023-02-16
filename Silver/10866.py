from collections import deque
import sys

N_deque = deque()

def push_front(x):
  N_deque.appendleft(x)

def push_back(x):
  N_deque.append(x)

def pop_front():
  if len(N_deque) == 0:
    print(-1)
  else:
    print(N_deque.popleft())

def pop_back():
  if len(N_deque) == 0:
    print(-1)
  else:
    print(N_deque.pop())

def size():
  print(len(N_deque))

def empty():
  if len(N_deque) == 0:
    print(1)
  else:
    print(0)

def front():
  if len(N_deque) == 0:
    print(-1)
  else:
    print(N_deque[0])

def back():
  if len(N_deque) == 0:
    print(-1)
  else:
    print(N_deque[-1])

N = int(sys.stdin.readline().rstrip())
c_deque = deque()

for i in range(N):
  c = deque(map(str, sys.stdin.readline().rstrip().split()))
  if c[0] == 'push_front':
    push_front(int(c[1]))
  elif c[0] == 'push_back':
    push_back(int(c[1]))
  elif c[0] == 'pop_front':
    pop_front()
  elif c[0] == 'pop_back':
    pop_back()
  elif c[0] == 'size':
    size()
  elif c[0] == 'empty':
    empty()
  elif c[0] == 'front':
    front()
  elif c[0] == 'back':
    back()