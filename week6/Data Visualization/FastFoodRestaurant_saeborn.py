import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('week6/Data Visualization/FastFoodRestaurants.csv', delimiter=',')
print(df.head())

sns.set_theme(style='darkgrid')
sns.scatterplot(x='latitude',y='longitude',data=df,palette='spring',hue='name')
plt.show()

sns.set_theme(style='white')
sns.countplot(x='name',data=df)
plt.xticks(rotation=45)
plt.title('Count of Restaurants')
plt.show()

sns.barplot(x='province',y='name',data=df)
plt.show()



sns.histplot(df['latitude'], bins=10)
plt.title("Latitude Distribution")
plt.show()

sns.violinplot(df['name'],color='pink')
plt.show()

sns.boxplot(x='name',data=df)
plt.show()

sns.pairplot(data=df,height=1.5)
plt.show()

sns.catplot(x='country',y='province',data=df ,kind='bar')
plt.show()

sns.stripplot(x='country',y='province',data=df,dodge=True,palette='viridis',marker="*",size=10,alpha=0.2,jitter=0.5)
plt.show()


sns.swarmplot(x='country',y='name',data=df,size=10)
plt.show()