class Father:
   father_name='Ahmed Pasha'
   profession='Police Officer'
   def job(me):print(me.profession)
   
class Son(Father):
   def __init__(me,name):
       print(name,me.father_name)

temo=Son('Tamer')       
temo.job()
