from matplotlib import pyplot as plt
import numpy as np
cars =['JAGUAR', 'BMW', 'MERCEDES BENZ', 'TESLA', 'AUDI','RANGE ROVER', 'VOLVO']

data =[23,34,45,67,54,43,31]

fig= plt.figure(figsize=(10,9))
plt.pie(data,labels=cars)

plt.show()