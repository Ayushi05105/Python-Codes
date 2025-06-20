import numpy as np
import matplotlib.pyplot as plt

fruits = ['Apple', 'Mango', 'Grapes', 'Banana']
prices = [400, 300, 200, 150]
plt.bar(fruits, prices, color = 'green')

plt.xlabel('Fruits')
plt.ylabel('Prices')
plt.title( 'Fruits Prices')
plt.show()

