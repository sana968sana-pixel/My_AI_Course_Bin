import numpy as np
Serial_Number,List_Year,Assessed_Value,Sale_Amount,SalesRatio=np.genfromtxt('week4\Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',',usecols=(0,1,5,6,7),dtype=float,unpack=True,skip_header=1,filling_values=0,invalid_raise=False)
print(Serial_Number)
print(List_Year)
print(Assessed_Value)
print(Sale_Amount)
print(SalesRatio)

#-----Statistics operations---
print('RealEstate_Sales 2001_2022  sales amount mean :',np.mean(Sale_Amount))
print('RealEstate_Sales 2001_2022  sales amount median :',np.median(Sale_Amount))
print('RealEstate_Sales 2001_2022  sales amount std :',np.std(Sale_Amount))
print('RealEstate_Sales 2001_2022  sales amount average :',np.average(Sale_Amount))
print('RealEstate_Sales 2001_2022  sales amount percentile_25 :',np.percentile(Sale_Amount,25))
print('RealEstate_Sales 2001_2022  sales amount percentile_50 :',np.percentile(Sale_Amount,50))
print('RealEstate_Sales 2001_2022  sales amount percentile_75 :',np.percentile(Sale_Amount,75))

#--------Maths operations-------

print('RealEstate_Sales 2001_2022  sales amount square:',np.square(Sale_Amount))
print('RealEstate_Sales 2001_2022  sales amount power :',np.power(Sale_Amount,2))
print('RealEstate_Sales 2001_2022  sales amount sqrt :',np.sqrt(Sale_Amount))
print('RealEstate_Sales 2001_2022  sales amount abs :',np.abs(Sale_Amount))


#------basic arithematic-----
addition= Assessed_Value+Sale_Amount
subtraction=Assessed_Value-Sale_Amount
multiplication=Assessed_Value*Sale_Amount
division=Assessed_Value/Sale_Amount

print('RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount Addition:',addition)
print('RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount subtraction:',subtraction)
print('RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount multiplication:',multiplication)
print('RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount division:',division)


#--------trignometry-----
Sales_amountPie = (Sale_Amount/1000) +1

sine_values = np.sin(Sales_amountPie)
cosine_values = np.cos(Sales_amountPie)
tangent_values = np.tan(Sales_amountPie)

print("RealEstate_Sales 2001_2022  Sale_Amount- Sine values:", sine_values)
print("RealEstate_Sales 2001_2022  Sale_Amount Cosine values:", cosine_values)
print("RealEstate_Sales 2001_2022  Sale_Amount Tangent values:", tangent_values)
print("RealEstate_Sales 2001_2022  Sale_Amount - Exponential values:", np.exp(Sales_amountPie))
#----logarthmic value-----
log_array = np.log(Sales_amountPie)
log10_array = np.log10(Sales_amountPie)

print("RealEstate_Sales 2001_2022  Sale_Amount -- Natural logarithm values:", log_array)
print("RealEstate_Sales 2001_2022  Sale_Amount -- Base-10 logarithm values:", log10_array)

#_________hyberbholic _______________

sinh_values = np.sinh(Sales_amountPie)
print("RealEstate_Sales 2001_2022  Sale_Amount   - Hyperbolic Sine values:", sinh_values)

cosh_values = np.cosh(Sales_amountPie)
print("RealEstate_Sales 2001_2022  Sale_Amount   - Hyperbolic Cosine values:", cosh_values)

tanh_values = np.tanh(Sales_amountPie)
print("RealEstate_Sales 2001_2022  Sale_Amount   -Hyperbolic Tangent values:", tanh_values)

asinh_values = np.arcsinh(Sales_amountPie)
print("RealEstate_Sales 2001_2022  Sale_Amount   -Inverse Hyperbolic Sine values:", asinh_values)

acosh_values = np.arccosh(Sales_amountPie)
print("RealEstate_Sales 2001_2022  Sale_Amount   -Inverse Hyperbolic Cosine values:", acosh_values)


#-------2Dimentional Array----

D2AssesSales = np.array([Assessed_Value, Sale_Amount])

print ("RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount - 2 dimentional arrary - " ,D2AssesSales)

print("RealEstate_Sales 2001_2022 Assessed_value  Sale_AmountZameen.com Long Plus Lat - 2 dimentional arrary - dimension" , D2AssesSales.ndim) 

print("RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount - 2 dimentional arrary - total number of elements" ,D2AssesSales.size)

print("RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount - 2 dimentional arrary - gives size of array in each dimension" ,D2AssesSales.shape)

print("RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount - 2 dimentional arrary - data type" ,D2AssesSales.dtype) 


# Splicing array
D2AssesSalesSlice=  D2AssesSales[:1,:5]
print("RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount - 2 dimentional arrary - Splicing array  " , D2AssesSalesSlice)
D2LongLatSlice2=  D2AssesSales[:1, 4:15:4]
print("RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount - 2 dimentional arrary - Splicing array  " , D2AssesSalesSlice)



# Indexing array
D2AssesSalesSliceItemOnly=  D2AssesSalesSlice[0,1]
print("RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount - 2 dimentional arrary - Index array " , D2AssesSalesSliceItemOnly)
D2LongLatSlice2ItemOnly=  D2LongLatSlice2[0, 2]
print("RealEstate_Sales 2001_2022 Assessed_value  Sale_Amount - 2 dimentional arrary - index array  " , D2AssesSalesSliceItemOnly)

for elem in np.nditer(D2AssesSales):
    print(elem)

for index, elem in np.ndenumerate(D2AssesSales):
    print(index, elem)
D2 = np.reshape(D2AssesSales, (1, 278))
print("RealEstate_Sales Assessed_value  Sale_Amount - 2 dimentional arrary - reshape : " , D2)
print("RealEstate_Sales Assessed_value  Sale_Amount - 2 dimentional arrary - reshape : Size " , D2.size)
print("RealEstate_Sales Assessed_value  Sale_Amount - 2 dimentional arrary - reshape : ndim " , D2.ndim)
print("RealEstate_Sales Assessed_value  Sale_Amount - 2 dimentional arrary - reshape : shape " , D2.shape)
print("RealEstate_Sales Assessed_value  Sale_Amount - 2 dimentional arrary - reshape : ndim " , D2.dtype)






