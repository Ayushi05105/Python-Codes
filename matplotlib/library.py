import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("iris")

def plot():
     sns.lineplot(x="sepal_length", y="sepal_width", data = data)
plt.title('Title using Matplotlib function')
plt.xlim(5)
sns.set_style("ticks")

#setting color palette
sns.set_palette('vlag')
plt.subplot(211)
plot()

sns.set_palette('Accent')
plt.subplot(212)
plot()



plt.show()
