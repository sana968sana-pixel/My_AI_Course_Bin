import numpy as np
Investment_Amount,Valuation,GrowthRate =np.genfromtxt("week4\startup_growth_investment_data.csv", delimiter=",", usecols=(3,4,8),unpack=True,dtype=None,skip_header=1)
print(Investment_Amount)
print(Valuation)
print(GrowthRate)
#____statistics operations-----
print("Startup_growth_investment_data GrowthRate mean: " , np.mean(GrowthRate))
print("Startup_growth_investment_data GrowthRate average: " , np.average(GrowthRate))
print("Startup_growth_investment_data GrowthRate std: " , np.std(GrowthRate))
print("Startup_growth_investment_data GrowthRate median: " , np.median(GrowthRate))
print("Startup_growth_investment_data GrowthRate percentile - 25: " , np.percentile(GrowthRate,25))
print("Startup_growth_investment_data GrowthRate percentile  - 75: " , np.percentile(GrowthRate,75))
print("Startup_growth_investment_data GrowthRatepercentile  - 3: " , np.percentile(GrowthRate,3))
print("Startup_growth_investment_data GrowthRate min : " , np.min(GrowthRate))
print("Startup_growth_investment_data GrowthRate max : " , np.max(GrowthRate))


#-----------Maths operations------

print("Startup_growth_investment_data GrowthRate square",np.square(GrowthRate))
print("Startup_growth_investment_data GrowthRate square root",np.sqrt(GrowthRate))
print("Startup_growth_investment_data GrowthRate power",np.power(GrowthRate,2))
print("Startup_growth_investment_data GrowthRate abs",np.abs(GrowthRate))

#---------basic arithematic--------

addition=Investment_Amount+Valuation
subtraction=Investment_Amount-Valuation
multiplication=Investment_Amount*Valuation
division=Investment_Amount/Valuation


print("Startup_growth_investment_data Investment_Amount  Valuation  Addition: " , addition)
print("Startup_growth_investment_data Investment_Amount  Valuation  subtraction: " , subtraction)
print("Startup_growth_investment_data Investment_Amount  Valuation  multiplication: " , multiplication)
print("Startup_growth_investment_data Investment_Amount  Valuation  division: " , division)

#-------trignometry function--------
GrowthRatePie=(GrowthRate / np.pi) + 1
print("Startup_growth_investment_data GrowthRate_div_pie sin values",np.sin(GrowthRate))
print("Startup_growth_investment_data GrowthRate_div_pie cos values",np.cos(GrowthRate))
print("Startup_growth_investment_data GrowthRate_div_pie tan values",np.tan(GrowthRate))
print("Startup_growth_investment_data GrowthRate_div_pie exponentional values",np.exp(GrowthRate))

print("Startup_growth_investment_data GrowthRate_div_pie sin hyberbholic values :",np.sinh(GrowthRate))
print("Startup_growth_investment_data GrowthRate_div_pie cos hyperbholic values :",np.cosh(GrowthRate))
print("Startup_growth_investment_data GrowthRate_div_pie tan hyperbholic values :",np.tanh(GrowthRate))

print("Startup_growth_investment_data GrowthRate_div_pie sin inverse hyperbholic values :",np.asinh(GrowthRate))
print("Startup_growth_investment_data GrowthRate_div_pie cos inverse hyperbholic values :",np.acosh(GrowthRate))
print("Startup_growth_investment_data GrowthRate_div_pie tan inverse hyperbholic values :",np.atanh(GrowthRate))

#---------logarthmic --------
log_values=np.log(GrowthRatePie)
log10_values=np.log10(GrowthRatePie)
print("Startup_growth_investment_data natural logarithm values:",log_values)
print("Startup_growth_investment_data base 10  natural logarithm values:",log10_values)

#---------2 Dinmensional arrray-----
D2InvestVal=np.array([Investment_Amount,Valuation])
print("Startup_growth_investment_data Investment_Amount  Valuation  2 dimentional array :",D2InvestVal)
print("Startup_growth_investment_data Investment_Amount  Valuation  2 dimentional array for dimension  :",D2InvestVal.ndim)
print("Startup_growth_investment_data Investment_Amount  Valuation  2 dimentional array size :",D2InvestVal.size)
print("Startup_growth_investment_data Investment_Amount  Valuation  2 dimentional array shape :",D2InvestVal.shape)
print("Startup_growth_investment_data Investment_Amount  Valuation  2 dimentional array  datatype:",D2InvestVal.dtype)

D2InvestValSlice=D2InvestVal[1,:5]
print("Startup_growth_investment_data investmental_amount and valuation",D2InvestValSlice)
D2InvestValSlice=D2InvestVal[0:2, 1:4]
print("Startup_growth_investment_data investmental_amount and valuation",D2InvestValSlice)


#----for loop----
for ele in np.nditer(D2InvestVal):
    print(ele)

for  index,ele in np.ndenumerate(D2InvestVal):
    print( index,ele)

