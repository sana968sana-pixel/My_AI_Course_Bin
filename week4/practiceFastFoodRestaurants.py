import numpy as np
latitude,longitude,postalCode=np.genfromtxt('week4/FastFoodRestaurants.csv',delimiter=",",usecols=(4,5,7),unpack=True,dtype=float,skip_header=1,filling_values=0,invalid_raise=False )
print(latitude)
print(longitude)
print(postalCode)
#-------statistics operations-----
print('Fast_Food_Restaurants postalCode mean:',np.mean(postalCode))
print('Fast_Food_Restaurants postalCode average:',np.average(postalCode))
print('Fast_Food_Restaurants postalCode std:',np.std(postalCode))
print('Fast_Food_Restaurants postalCode median:',np.median(postalCode))
print('Fast_Food_Restaurants postalCode percentile_25:',np.percentile(postalCode,25))
print('Fast_Food_Restaurants postalCode percentile-50:',np.percentile(postalCode,50))
print('Fast_Food_Restaurants postalCode percentile_75:',np.percentile(postalCode,75))

#-------Maths operations--------
print('Fast_Food_Restaurants postalCode square:',np.square(postalCode))
print('Fast_Food_Restaurants postalCode square root:',np.sqrt(latitude))
print('Fast_Food_Restaurants postalCode power:',np.power(postalCode,2))
print('Fast_Food_Restaurants postalCode abs:',np.abs(postalCode))

#------basic arithmetic --------
add=latitude+longitude
sub=latitude-longitude
mul=latitude*longitude
div=latitude/longitude

print('Fast_Food_Restaurants postalCode latitude and longitude Addition:',add)

print('Fast_Food_Restaurants postalCode latitude and longitude subtraction:',sub)

print('Fast_Food_Restaurants postalCode latitude and longitude multiplication:',mul)

print('Fast_Food_Restaurants postalCode latitude and longitude division:',div)


#------Trignometric operations-------
postalCodepie=(postalCode/1000)+1
print('Fast_Food_Restaurants postalCode  sin values:',np.sin(postalCodepie))

print('Fast_Food_Restaurants postalCode  cos values:',np.cos(postalCodepie))

print('Fast_Food_Restaurants postalCode  tan values:',np.tan(postalCodepie))

print('Fast_Food_Restaurants postalCode  sin hyperbolic values:',np.sinh(postalCodepie))

print('Fast_Food_Restaurants postalCode  cos inverse hyperbolic values:',np.acosh(postalCodepie))

#-----logarithm values------
log_values=np.log(postalCodepie)
log10_values=np.log10(postalCodepie)

print('Fast_Food_Restaurants postalCode  natural logarithm values :',log_values)

print('Fast_Food_Restaurants postalCode   base 10 natural logarithm values :',log10_values)

D2longlat=np.array([longitude,latitude,])

print('Fast_Food_Restaurants postalCode  2 dimentional array :',D2longlat)

print('Fast_Food_Restaurants postalCode  2 dimentional array :',D2longlat.ndim)

print('Fast_Food_Restaurants postalCode  2 dimentional array size :',D2longlat.size)

print('Fast_Food_Restaurants postalCode  2 dimentional array  shape:',D2longlat.shape)

print('Fast_Food_Restaurants postalCode  2 dimentional array  dtatype:',D2longlat.dtype)

#-----slicing---
D2longlatSlice=D2longlat[1,:8]
print('Fast_Food_Restaurants postalCode  2 dimentional array slicing:',D2longlatSlice)

#-----for loop------
for ele in np.nditer(D2longlat):
    print(ele)

for index, ele in np.ndenumerate(D2longlat):
    print(index,ele)




