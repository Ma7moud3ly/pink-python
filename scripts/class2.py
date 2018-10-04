class Operation:
   num1=num2=0
   def __init__(me,num1,num2):
      me.num1=num1
      me.num2=num2
   def add(me):return me.num1+me.num2 #add num1 and num2
   def sub(me):return me.num1-me.num2 #subtract num2 from num1
   def mul(me):return me.num1*me.num2 #multiply num1 by mum2
   def div(me):return me.num1/me.num2 #divide num1 on num2
    
x=Operation(100,5)
print(x.add())
print(x.sub())
print(x.mul())
print(x.div())

y=Operation(200,20)
print(y.add())
print(y.sub())
print(y.mul())
print(y.div())

x.num1=30
x.num2=5
print(x.add())
print(x.sub())
print(x.mul())
print(x.div())
