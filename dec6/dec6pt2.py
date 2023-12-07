# read in inputs
with open("dec6/dec6_input.txt") as f:
  times = f.readline().split()[1:]
  distances = f.readline().split()[1:]
  times = int(''.join(times))
  distances = int(''.join(distances))

# 940200 = held * (71530 - held)
# 0 = 71530*held - 1held^2  - 940200 | -1
# 0 = held^2 - 71530*held + 940200
# x1 = 
# x2 = 

import math

x1 = 71530/2 + math.sqrt(((71530/2)**2)-940200)
x2 = 71530/2 - math.sqrt(((71530/2)**2)-940200)
#print(int(abs(x1-x2)))

def find_possible_ways(times, distances):
  x1 = times/2 + math.sqrt(((times/2)**2)-distances)
  x2 = times/2 - math.sqrt(((times/2)**2)-distances)
  return int(abs(x1-x2))

print(find_possible_ways(times, distances))