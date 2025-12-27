import matplotlib.pyplot as plt
x_values =[1,2,3,4,5]
y_values =[2,4,6,8,10]
plt.plot(x_values,y_values,label='Line  Chart',marker ='o',linestyle='-')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Chart Example')
plt.grid(True)
plt.legend()
plt.show()