import numpy as  np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("week6/Data Visualization/startup_growth_investment_data (1).csv",delimiter=',')
print(df.head())

sns.set_theme(style="darkgrid")

sns.lineplot(x='Funding Rounds',y='Number of Investors',data=df,palette='spring')
plt.show()

sns.histplot(x='Funding Rounds',data=df,palette='GnBu')
plt.show()
sns.set_theme(style='ticks')
sns.barplot(x='Industry',y='Funding Rounds',data=df,)
plt.show()

sns.scatterplot(x="Investment Amount (USD)",y='Valuation (USD)',data=df,palette='spring')
plt.show()

data=np.random.randint(low=1,high=100,size=(10,10))
print(data)

sns.heatmap(data=data,linecolor='yellow',linewidths=2,annot=True,cmap='pink')
plt.show()


sns.countplot(x='Industry',data=df,facecolor=[0,0,0,0],linewidth=4,edgecolor="black")
plt.show()

sns.violinplot(x='Investment Amount (USD)',y='Valuation (USD)',data=df)
plt.show()


sns.boxplot(x='Number of Investors',data=df)
plt.show()

sns.pairplot(data=df,height=1.5)
plt.show()

sns.catplot(x='Funding Rounds',y='Number of Investors',data=df ,kind='bar')
plt.show()

sns.stripplot(x='Funding Rounds',y='Number of Investors',data=df,dodge=True,palette='viridis',marker="*",size=10,alpha=0.2,jitter=0.5)
plt.show()

sns.kdeplot(x='Number of Investors',data=df,fill=True,shade=True,color='pink')
plt.show()


sns.swarmplot(x='Number of Investors',y='Industry',data=df,size=10)
plt.show()