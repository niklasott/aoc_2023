nodes = {}

# read in transform
with open("dec8/input.txt") as f:
  lines = f.readlines()
  ix = 0
  for l in lines:
    #print(l)
    # read in LR instructions
    if ix == 0:
      instructions = l.split()[0]
      #print(instructions)
    # skip line 1 and continue with 
    if ix > 1:
      line_elements = l.split()
      nodes[line_elements[0]] = (line_elements[2][1:-1], line_elements[3][:-1])
    ix += 1

instructions_dict = {"L":0, "R":1}
instructions = [instructions_dict[i] for i in [*instructions]]

jump_count = 0
current_node = "AAA"

while current_node != "ZZZ":
  jump_count += 1
  # always get first instruction element, for "endless" instruction we keep appending the first element to the end
  single_instruction = instructions[0]
  current_node = nodes[current_node][single_instruction]
  # re appending the first element
  instructions = instructions[1:] + [single_instruction]

print(jump_count)
