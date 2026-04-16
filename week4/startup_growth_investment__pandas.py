import pandas as pd
print(pd.__version__)
df_index=pd.read_csv('week4/startup_growth_investment_data.csv', delimiter=',',index_col='Startup Name')
print(df_index)

print('df_data types',df_index.dtypes)
print('df.info',df_index.info())
print('describes shows all the  statistics functions\n',df_index.describe())
print('countingthe rows and column in dataframe',df_index.shape)
print('Last three Rows:')
print(df_index.tail(3))


print('First Three Rows:')
print(df_index.head(3))
#unique values 
print(df_index['Industry'].unique())
print(df_index['Industry'].value_counts())
#all columns names
print('acess all column name',df_index.columns)

#acess column
Industry=df_index['Industry']
print('acess single column',Industry)

#acess multiple column

multicolumn = df_index[['Country','Year Founded']]
print('acess multiple column at a time\n',multicolumn)

#-------------using loc selecting rows and columns----------------
select_row=df_index.loc[["Startup_6"]]
print('select row using loc ',select_row)

#using loc select multiple rows

second_row2 = df_index.loc[['Startup_8','Startup_67' ]]
print("#Selecting multiple rows using .loc",second_row2)

#using loc select range of rows

select_row3 = df_index.loc['Startup_8':'Startup_67' ]
print("#Selecting slice of rows using .loc",select_row3)

#select condition
select_row4=df_index.loc[df_index['Number of Investors']==50]
print("Conditional selection of rows using loc")
print(select_row4)

#Selecting a single column using .loc
select_row5 = df_index.loc[:'Startup_6','Growth Rate (%)']
print("#Selecting a single column using .loc",select_row5)


#Selecting multiple columns using .loc
select_row6 = df_index.loc[:'Startup_4',['Investment Amount (USD)','Growth Rate (%)']]
print("#Selecting multiple columns using .loc",select_row6)


#Selecting a slice of columns using .loc
select_row7 = df_index.loc[:'Startup_3','Country':'Number of Investors']
print("#Selecting a slice of columns using .loc",select_row7)


#----------------select rows and colums using iloc-------------------------

select_row8 = df_index.iloc[6]
print("Selecting a single row using .iloc",select_row8)


#Selecting multiple rows using .iloc
select_row9 = df_index.iloc[[6, 98,75]]
print("Selecting multiple rows using .iloc",select_row9)


#Selecting a slice of rows using .iloc
select_row10 = df_index.iloc[0:4]
print("Selecting a slice of rows using .iloc",select_row10)

#-------------- add new row------------------
df_index.loc['Startup_5001'] = ['Blockchain',8,1335165853.1,6621448041.824468,50,'Germany',2012,77.1] 
print("Modified DataFrame - add a new row:")
print(df_index)

#using drop 
df_index.drop('Startup_1', axis=0, inplace=True)
df_index.drop(columns='Year Founded', inplace=True)
print("Modified DataFrame - Remove Rows:")
print(df_index)


#using query
 