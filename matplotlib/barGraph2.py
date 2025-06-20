import numpy as np
import matplotlib.pyplot as plt
barWidth = 0.25
fig = plt.subplots(figsize = (12,8))

IT = [20,40,30,68,60]
ECE = [13,45,65,43,65]
CSE = [22,34,54,57,60]

br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, IT ,color = 'r', width = barWidth , edgecolor = 'grey',label = 'IT')
plt.bar(br2, ECE ,color = 'b', width = barWidth , edgecolor = 'grey',label = 'ECE')
plt.bar(br3, CSE ,color = 'g', width = barWidth , edgecolor = 'grey',label = 'CSE')

plt.xlabel('Branch', fontweight ='bold',fontsize =15)
plt.ylabel('Student Passed', fontweight ='bold',fontsize =15)
plt.xticks([r + barWidth for r in br1] , ['2018','2019','2020','2021','2022'])
plt.legend()
plt.show()