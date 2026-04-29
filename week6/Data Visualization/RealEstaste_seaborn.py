import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
  
df=pd.read_csv('week6\RealEstate-USA.csv',delimiter=',')
print(df.head())

sns.lineplot(x='bed',y='bath',data=df,hue='state',palette="spring",)
plt.show()

sns.histplot(x='bed',data=df,color='magenta',discrete=True)
plt.show()

sns.barplot(x='bath',y='bed',hue='state',data=df,palette='spring',ci=False)
plt.show()

sns.scatterplot(x='bed',y='bath',data=df,hue='state',palette='GnBu',size='bath')
plt.show()

data=np.random.randint(low=1,high=100,size=(10,10))
print(data)

sns.heatmap(data=data,cmap='GnBu',alpha=0.5,linecolor='blue',linewidths='2',annot=True,xticklabels=False)
plt.show()

sns.heatmap(df.corr(numeric_only=True),cmap='spring',linecolor='yellow',linewidths=3,annot=True)
plt.show()

sns.countplot(x='bed',data=df,hue='state',facecolor=[0,0,0,0],linewidth=4,edgecolor="black")
plt.show()

sns.violinplot(x='bath',y='acre_lot',data=df)
plt.show()

sns.violinplot(df['bed'],color='pink')
plt.show()

sns.boxplot(x='bed',data=df)
plt.show()

sns.pairplot(data=df,height=1.5)
plt.show()

sns.catplot(x='bed',y='bed',data=df ,kind='bar')
plt.show()

sns.stripplot(x='bed',y='bath',data=df,dodge=True,palette='viridis',marker="*",size=10,alpha=0.2,jitter=0.5)
plt.show()

sns.kdeplot(x='bed',data=df,fill=True,shade=True,color='pink')
plt.show()

sns.kdeplot(x='bed',y='bath',data=df,fill=True,shade=True,cmap='spring')
plt.show()

sns.swarmplot(x='bed',y='bath',data=df,size=10)
plt.show()