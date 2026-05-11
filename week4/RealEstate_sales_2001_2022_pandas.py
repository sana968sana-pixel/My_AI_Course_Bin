import pandas as pd
print(pd.__version__)

df=pd.read_csv('week4/Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',',parse_dates=[2],date_format={'date_added':'%d-%m-%y'})

print(df)

print('First 3 rows',df.head(3))

print('Last 2 rows',df.tail(2))

print("datatypes",df.dtypes)

print('df.info',df.info())

# summary of all statistics functions
print('describes shows all the  statistics functions\n',df.describe()) 
 

print('counting the rows and column in dataframe',df.shape)#no of rows and column

#access single col
Sales_Ratio=df["Sales Ratio"]
print("acess the name column",Sales_Ratio)

#multiple col
multicol=df[["Property Type","Residential Type"]]
print("acess multiple colums:",multicol)

#------------------------use .loc-------------------------
# single row using loc
third_row=df.loc[[2]]
print("selecting single rows using loc:",third_row)

 # multiple row  using loc
two_rows=df.loc[[2,5]]
print("selecting multiple rows using loc:",two_rows)

#slice  of rows
slice_rows=df.loc[3:7]
print("slice of rows:",slice_rows)

#conditional selection of rows
select_rows=df.loc[df["Residential Type"]=="Two Family"]
print("selecting a single colum Residential Type  those value ponce:",select_rows)


#select single col
select_rows2=df.loc[:2,'Town']
print(select_rows2)

#select multiple colums
select_rows3=df.loc[:3,["Town","Residential Type"]]
print("select a slice of col:",select_rows3)

#select slice of column
select_rows4=df.loc[:2,"Assessed Value":"Sales Ratio"]
print("select a slice of column",select_rows4)

#select combine row and col
select_rows5=df.loc[df["Town"]=='Avon',"Date Recorded":"Sales Ratio"]
print("combined rows and col:",select_rows5)

#-----------------------using .iloc---------------------
select_row_iloc=df.iloc[[0, 5,7]]
print("select rows using iloc",select_row_iloc)


#select slice
select_row_iloc2=df.iloc[2:5]
print("select slice of row",select_row_iloc2)



#select combined row and column
select_row_iloc3=df.iloc[[1,3],2:5]
print("combined rows and column:",select_row_iloc3)


#select slice of col
select_row_iloc4=df.iloc[:,2:6]
print("select row and column",select_row_iloc4)


#----------MANIPULATION--------

df.loc[len(df.index)]= {
    'Serial Number': 20364,
    'List Year': 2020,
    'Date Recorded': '06/17/2021',
    'Town': 'Bethel',
    'Address': '1308 LEXINGTON BOULEVARD',
    'Assessed Value': 195300.00,
    'Sale Amount': 365000.00,
    'Sales Ratio': 0.535,
    'Property Type': 'Residential',
    'Residential Type': 'Condo'
}
print("modified data frame:")
print(df)

#----------drop rows---------

df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)
print("modified data ")
print(df)


#------------drop col-----------

df.drop("Non Use Code",axis=1, inplace=True)
df.drop(["Assessor Remarks","OPM remarks"], axis=1,inplace=True)
print("modified data frame")
print(df)

#--------------rename------------
df.rename(columns= {"Location":"Location_changed"}, inplace=True)
df.rename(mapper= {'Address': 'Address_Changed', 'Location':'Location_changed'}, axis=1, inplace=True)

print("Modified DataFrame  - Rename Labels :")
print(df)

df.rename(index={0: 7}, inplace=True)
df.rename(mapper={1: 10, 2: 140}, axis=0, inplace=True)
print("Modified DataFrame :")
print(df)

#-----------select rows----------
selected_rows=df.query("Town =='Middletown' or 'Property Type'=='Residential' ")
print(select_rows. to_string())
print(len(select_rows))

#------------sort rows----------
df['Date Recorded'] = pd.to_datetime(df['Date Recorded'])
sorted_df= df.sort_values(by='Date Recorded')
print(sorted_df.to_string(index=False))

sorted_df1=df.sort_values(by=['Town','Property Type'])
print("sorted by price and city in ascending order")
print(sorted_df1.to_string(index=False))


#--------- data cleaning------
df_cleaned=df.dropna()
print("cleaned data",df_cleaned)

df.fillna('0',inplace=True)
print("filling  values with 0",df)



#----------createlist------------
ar=[0,3,5,7]
array=pd.array(ar)
print(array)

#-------------arrays of integers--------
int_array=pd.array([1,2,3,6],dtype='int')
print(int_array)

