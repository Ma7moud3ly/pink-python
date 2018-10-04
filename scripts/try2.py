while True:
  try:
    num1 = int(input('Enter A Num1 : '))
    num2 = int(input('Enter A Num1 : '))
    result=num1/num2
    print(result)
  except ZeroDivisionError:
    print('Cant divide on zero')
  except ValueError:
    print('Incorrect Number') 
