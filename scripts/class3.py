class Father:
   name='Ahmed Pasha'
   profession='Officer'
   def job(me):print(me.profession)
   
class Son(Father):
   def __init__(me,name):print(name,me.name)

temo=Son('Tamer')       
temo.job() 
   
   
