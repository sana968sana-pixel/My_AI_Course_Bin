import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data =pd.DataFrame({'x':np.arange(100),'y':np.random.rand(100).cumsum()})

sns.set_theme(style='dark')

sns.lineplot(x='x',y='y',data=data)
plt.show()

df=pd.read_csv('week6/Data Visualization/Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',')
print(df.head(3))

sns.histplot(x='Property Type',data=df)
plt.show()

sns.kdeplot(x='Sales Ratio',data=df,color='pink')
plt.show()

sns.heatmap(data=data,linecolor='yellow')
plt.show()

sns.scatterplot(x='Town',y='Property Type',data=df)
plt.show()

sns.violinplot(df['Property Type'],color='pink')
plt.show()

sns.boxplot(x='Property Type',data=df)
plt.show()

sns.pairplot(data=df,height=1.5)
plt.show()

sns.catplot(x='Town',y='Property Type',data=df ,kind='bar')
plt.show()

sns.stripplot(x='Town',y='Property Type',data=df,dodge=True,palette='viridis',marker="*",size=10,alpha=0.2,jitter=0.5)
plt.show()

sns.kdeplot(x='Sales Ratio',data=df,fill=True,shade=True,color='pink')
plt.show()

sns.kdeplot(x='Sales Ratio',y='Assessed Value',data=df,fill=True,shade=True,cmap='spring')
plt.show()

sns.swarmplot(x='Town',y='Property Type',data=df,size=10)
plt.show()