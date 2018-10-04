x=1
y=2

def xx():
    global x
    x=3
    y=4
    print('local x = %s'%x)
    print('local y = %s'%y)
       
print('global x = %s'%x)
print('global y = %s'%y)
xx()
print('again global x = %s'%x)
print('again global y = %s'%y)

