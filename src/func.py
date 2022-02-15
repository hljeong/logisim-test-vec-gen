num_inputs = 4 # number of inputs
num_outputs = 1 # number of outputs
header_str = "A 4 B 4 C 4 E 1 M 4" # <var1> <bitwidth> <var2> <bitwidth> ...
gen_mode = 0 # -1: custom inputs, 0: exhaustive binary inputs, positive: (gen_mode) random inputs 
custom_inputs = []

# implement desired combinational logic
# input: list of length num_inputs of ints
# output: list of length num_outputs of ints
def func(x): 
  if x[3] == 0: 
    return [-1]
  else: 
    return [sorted(x[:3])[1]]