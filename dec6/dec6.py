# read in inputs
with open("dec6_input.txt") as f:
  times = f.readline().split()[1:]
  distances = f.readline().split()[1:]
  times = [int(t) for t in times]
  distances = [int(d) for d in distances ]


total_answers = 1
# loop over element
for i in range(len(times)):
  answer_counter = 0
  # loop over time
  for t in range(times[i]+1):
    reached_distance = t*(times[i]-t)
    # higher than record
    if reached_distance > distances[i]:
      answer_counter += 1
  # multiply each elements possibilities
  total_answers *= answer_counter

print(total_answers)