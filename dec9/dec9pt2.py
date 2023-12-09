import numpy as np

list_of_reports = []
with open("dec9/input.txt") as f:
  for l in f.readlines():
    #temp = [int(i) for i in l.split()]
    #print(temp)
    list_of_reports.append([int(i) for i in l.split()])

def get_new_line(line):
  new_line = [line[i+1] - line[i] for i in range(len(line)-1)]
  return new_line

# didnt work with just summing it up no more
# so needed a real function
def backtrack(sequences):
  vals = []
  for i in range(len(sequences)):
    if i == 0:
      vals.append(0)
    else:
      dif = len(sequences)-1-i
      vals.append(sequences[dif][0] - vals[i-1])
  return vals[-1]

def get_prev_value(report):
  sequences = []
  sequences.append(report)
  reached_last_line = False
  # build all sequences
  while not reached_last_line:
    report = get_new_line(report)
    sequences.append(report)
    if all(x == 0 for x in report):
      reached_last_line = True
  # calc last value:
  return backtrack(sequences)


def get_answer(list_of_reports):
  answers = []
  for x in list_of_reports:
    answers.append(get_prev_value(x))
  return sum(answers)

print(get_answer(list_of_reports))