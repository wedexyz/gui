#open and read the file after the appending:
import pandas as pd
import numpy as np
f = open("Output.txt", "r")
print(np.array(f.read()))


