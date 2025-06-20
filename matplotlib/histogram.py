import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

data = np.random.randn(2000)
plt.hist(data,bins = 30 , color='red' , edgecolor='black')


plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()