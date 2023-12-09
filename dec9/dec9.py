list_of_reports = []
with open("dec9/input.txt") as f:
  for l in f.readlines():
    #temp = [int(i) for i in l.split()]
    #print(temp)
    list_of_reports.append([int(i) for i in l.split()])

def get_new_line(line):
  new_line = [line[i+1] - line[i] for i in range(len(line)-1)]
  return new_line

def get_next_value(report):
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
  stack_to_sum = []
  for s in sequences:
    stack_to_sum.append(s[-1])
  return sum(stack_to_sum)


def get_answer(list_of_reports):
  answers = []
  for x in list_of_reports:
    answers.append(get_next_value(x))
  return sum(answers)

print(get_answer(list_of_reports))