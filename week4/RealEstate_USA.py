import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf)
brokered_by,price,zip_code=np.genfromtxt('week4\RealEstate-USA.csv',delimiter=',',usecols=(0,2,9), unpack=True, dtype=None,skip_header=1)
print(brokered_by)
print(price)
print(zip_code)

print('real estate usa price mean:',np.mean(price))
print('real estate usa price average:',np.average(price))
print('real estate usa price std:',np.std(price))
print('real estate usa price median:',np.median(price))
print('real estate usa price percentile_25:',np.percentile(price,25))
print('real estate usa price percentile-50:',np.percentile(price,50))
print('real estate usa price percentile_75:',np.percentile(price,75))

# -----maths operations------
print('real estate usa price  square:',np.square(price))
print('real estate usa price sqrt :',np.sqrt(price))
print('real estate usa price power:',np.power(price,2))
print('real estate usa price abs :',np.abs(price))


#-------basic arithematic functions-----

addition=price+zip_code
subtraction=price-zip_code
multiplication=price*zip_code
division=price/zip_code

print('real estate usa price  zipcode addition:',addition)

print('real estate usa price  zipcode subtraction:',subtraction)

print('real estate usa price  zipcode multiplication:',multiplication)

print('real estate usa price  zipcode division:',division)

#------Trignometry functions-----
pricepie=(price/np.pi)+1
sinevalues= np.sin(pricepie)
cosvalues=np.cos(pricepie)
tanvalues=np.tan(pricepie)

print('real estate usa price div pie sinvalues:',sinevalues)
print('real estate usa price div pie cosvalues:',cosvalues)
print('real estate usa price div pie tanvalues:',tanvalues)
print('real estate usa price div pie exponentional values:',np.exp(pricepie))


#----logarthim values----
log_array=np.log(pricepie)
log10_array=np.log10(pricepie)

print('real estate usa price div pie  natural logarithm values:',log_array)

print('real estate usa price div pie  base 10 natural logarithim values:',log10_array)


sinh_values=np.sinh(pricepie)
print('real estate usa price div pie sin hyperbolic values:',sinh_values)
cosh_values=np.cosh(pricepie)
print('real estate usa price div pie cos hyperbholic values:',cosh_values)
tanh_values=np.tanh(pricepie)
print('real estate usa price div pie tan hyberbholic values:',tanh_values)

asinh_values=np.asinh(pricepie)
print('real estate usa price div pie inverse hyperbolic sin values:',asinh_values)
acosh_values=np.cosh(pricepie)
print('real estate usa price div pie inverse hyperbolic cos values:',acosh_values)
atanh_values=np.atanh(pricepie)
print('real estate usa price div pie inverse hyperbolic tan values:',atanh_values)



D2pricezip=np.array([price,zip_code])
print('real estate usa price plus zip_code  -2dimention',D2pricezip)

print('real estate usa price plus zip_code  -2dimention',D2pricezip.ndim)
print('real estate usa price plus zip_code  -2dimention array size',D2pricezip.size)
print('real estate usa price plus zip_code  -2dimention array shape',D2pricezip.shape)
print('real estate usa price plus zip_code  -2dimention array datatype',D2pricezip.dtype)


D2pricezipslice=D2pricezip[:1,:5]
print('real estate usa price plus zip_code  -2dimention',D2pricezipslice)

D2pricezipslice=D2pricezip[:1,4:14:4]

print('real estate usa price plus zip_code  -2dimention',D2pricezipslice)


D2pricezipsliceitemsonly=D2pricezip[0,1]
print('real estate  usa plus price  ',D2pricezipsliceitemsonly)
 
for ele in np.nditer(D2pricezip):
    print (ele)



for index, ele in np.ndenumerate(D2pricezip):
    print(index,ele)
    D2pricezip1=np.reshape(D2pricezip,(1,400))
    print('real estate price and zipcode reshape',D2pricezip1)
