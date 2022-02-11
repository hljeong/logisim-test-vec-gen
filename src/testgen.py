from func import *
import random

def onehot(x): 
  return 1 << x

def bitstr(x, n): 
  return  ("0" * n + "{0:b}".format(x))[-n:]

def gen_next(x, header): 
  for i in range(len(x) - 1, -1, -1): 
    x[i] = (x[i] + 1) % (1 << header[i][1])
    if x[i] != 0: 
      break
  return x

def write_line(f, inputs, outputs, header, n): 
  for i in range(len(inputs)): 
    f.write("%s " % bitstr(inputs[i], header[i][1]))
  for i in range(len(outputs)): 
    f.write("%s " % bitstr(outputs[i], header[n + i][1]))
  f.write('\n')

def gen(): 
  header_elems = header_str.split()
  header = []
  for i in range(num_inputs + num_outputs): 
    header.append((header_elems[2 * i], int(header_elems[2 * i + 1])))
    
  with open('../generated/test.txt', 'w') as f:
    for col in header: 
      f.write("%s[%d] " % col)
    f.write('\n')
    
    if gen_mode == -1: 
      for inputs in custom_inputs: 
        write_line(f, inputs, func(inputs), header, num_inputs)

    elif gen_mode == 0: 
      inputs = [0] * num_inputs
      while True: 
        write_line(f, inputs, func(inputs), header, num_inputs)
        
        inputs = gen_next(inputs, header)
        if all([x == 0 for x in inputs]): 
          break

    else: 
      for t in range(gen_mode): 
        inputs = [random.randint(0, (1 << header[j][1]) - 1) for j in range(num_inputs)]
        write_line(f, inputs, func(inputs), header, num_inputs)