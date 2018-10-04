#print دالة 

print('Hi') #بتطبع نصوص
print(123)  #أرقام 

x = [1,2,3]
print(x)    #list

y = {'day1':'sat','day2':'sun'}
print(y)    #dict

name = "Mahmoud"  #متغير نصى
#عشان نطبع نص جنب المتغير
#نخلى المتغير برامتر تانى فى الدالة
print("1-My Name is:",name)

#أو نعمل دمج بين النص والمتغير النصى بعلامة +
print("2-My Name is:"+name)

age = 23  #متغير عددى
#ينفع نمرره كبرامتر تانى وهيتطبع جنب النص
print("3-My Age is:",age)
#أو نستخدم المعامل %
print("4-My Age is: %s"%age)
#مينفعش ندمج بين متغير نصى ومتغير عددى وهيطلع ايرور
print("4-My Name is:"+age)
