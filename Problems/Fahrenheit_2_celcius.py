# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from 
# Start to End at the gap of W, into their corresponding Celsius values and print the table.

#  INPUT 
# 3 integers - S, E and W respectively 

# OUTPUT Fahrenheit to Celsius conversion table. One line for every Fahrenheit and corresponding Celsius value. 
# The Fahrenheit value and its corresponding Celsius value should be separate by single space.


import math
s = int(input())
e = int(input())
w = int(input())
fah =0 
while s<=e:
    fah = ((5*(s-32))/9)
    if fah < 0:
        print(s,math.ceil(fah))
    else:
        print(s,math.floor(fah))
    s+=w
