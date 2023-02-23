import sys

mod_list = [0] * 8001

N = int(sys.stdin.readline().rstrip())
N_list = [0]*N
for i in range(0, N):
  n = int(sys.stdin.readline().rstrip())
  N_list[i] = n
  mod_list[n+4000] += 1

N_list.sort()

avg = round(sum(N_list)/len(N_list))
med = N_list[int(round(len(N_list))/2)]
ran = N_list[-1] - N_list[0]

mod = 0
count = 0
mod_max = []
for j in range(0, len(mod_list)):
  if mod_list[j] > mod:
    mod = mod_list[j]
    count = j
    mod_max = [count]
  elif mod_list[j] == mod and mod != 0:
    mod_max.append(j)

mod_max.sort()

if len(mod_max) > 1:
  mod = (mod_max[1]-4000)
else:
  mod = (mod_max[0]-4000)

print(avg)
print(med)
print(mod)
print(ran)