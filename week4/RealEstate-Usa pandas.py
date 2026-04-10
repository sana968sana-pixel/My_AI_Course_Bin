import pandas as pd
df = pd.read_csv('week4/RealEstate-USA.csv',delimiter=',')
print(df)
print(" data types" , df.dtypes)
print("info():   " , df.info() )

print("last three rows:")
print(df.tail(2))

print("first three rows:")
print(df.head(1))

print("summmary of statistics  dataframe:",df.describe())

print("counting the rows and columns :",df.shape)

#access single col
city=df["city"]
print("acess the name column",city)

#multiple col
city_state=df[["city","state"]]
print("acess multiple colums:",city_state)

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
select_rows=df.loc[df["city"]=="Ponce"]
print("selecting a sindle colum city  those value ponce:",select_rows)

#select single col
select_rows2=df.loc[:2,'street']
print(select_rows2)

#select multiple colums
select_rows3=df.loc[:3,["price","zip_code"]]
print("select a slice of col:",select_rows3)

#select slice of column
select_rows4=df.loc[:2,"status":"zip_code"]
print("select a slice of column",select_rows4)

#select combine row and col
select_rows5=df.loc[df["city"]=='Lares',"status":"house_size"]
print("combined rows and col:",select_rows5)

#-----------------------using .iloc---------------------
select_row_iloc=df.iloc[[0, 5,7]]
print("select rows using iloc",select_row_iloc)


#select slice
select_row_iloc2=df.iloc[2:7]
print("select slice of row",select_row_iloc2)



#select combined row and column
select_row_iloc3=df.iloc[[1,3],2:5]
print("combined rows and column:",select_row_iloc3)


#select slice of col
select_row_iloc4=df.iloc[:,2:6]
print("select row and column",select_row_iloc4)


#----------MANIPULATION--------

df.loc[len(df.index)]=[111111,"not for sale",50000,2,3,0.11,111345,"lahore","pakistan",345,122,""]
print("modified data frame:")
print(df)

#----------drop rows---------

df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)
print("modified data ")
print(df)


#------------drop colm-----------

df.drop("acre_lot",axis=1, inplace=True)
df.drop(["house_size","prev_sold_date"], axis=1,inplace=True)
print("modified data frame")
print(df)
#--------------rename------------
df.rename(columns= {"status":"status_changed"}, inplace=True)
df.rename(mapper= {'bed': 'bednumber_Changed', 'state':'state_changed'}, axis=1, inplace=True)

print("Modified DataFrame  - Rename Labels :")
print(df)

df.rename(index={0: 7}, inplace=True)
df.rename(mapper={1: 10, 2: 140}, axis=0, inplace=True)
print("Modified DataFrame :")
print(df)
#-----------select rows----------
selected_rows=df.query("street =='Adjuntas' or zip_code==601")
print(select_rows. to_string())
print(len(select_rows))

#------------sort rows----------
sorted_df= df.sort_values(by='price')
print(sorted_df.to_string(index=False))

sorted_df1=df.sort_values(by=['price','city'])
print("sorted by price and city in ascending order")
print(sorted_df1.to_string(index=False))


#--------- data cleaning------
df_cleaned=df.dropna()
print("cleaned data",df_cleaned)

df.fillna(0,inplace=True)
print("filling  values with 0",df)



#----------createlist------------
ar=[0,3,5,7]
array=pd.array(ar)
print(array)

#-------------arr
# ays of integers--------
int_array=pd.array([1,2,3,6],dtype='int')
print(int_array)