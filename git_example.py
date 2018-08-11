```
This python file si a goood starting pouint.
Activation Funstions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + numpy.exp(-x)))

def tanh(x):
  # enter code below
  return ((numpy.exp(x)-numpy.exp(-x))/(numpy.exp(x)+numpy.exp(-x)))
def relu(x):
  # entr code below
  return max(0,x)
  
