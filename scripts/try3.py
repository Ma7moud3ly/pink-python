marks={'ahmed':20,'ali':19,'mahmoud':10,'noor':18}

name=input('Enter your name : ')

try:mark=marks[name]

except:mark='user not found'

finally:print(mark)
