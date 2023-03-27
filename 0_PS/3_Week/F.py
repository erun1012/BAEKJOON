import sys

def fib(n):
    global count1
    if (n == 1 or n == 2):
      return 1;  # 코드1
    else:
      count1 += 1
      return (fib(n - 1) + fib(n - 2))


def fibonacci(n):
    global count2
    val = [0, 1]
    if n >= 2:
       for i in range(2, n+1):
          count2 += 1
          val.append(val[i-1] + val[i-2])
    return val[n]

n = int(sys.stdin.readline())

count1, count2 = 0, 0
# a = fib(n)
b = fibonacci(n)
print(b, end=" ")
print(count2-1)