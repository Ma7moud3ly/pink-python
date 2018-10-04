while True:
    try:
        x = int(input('Enter A Number : '))
    except:
        print('incorrect number')
        continue
    if x%2==0:
        print('Even')
    else:
        print('Odd')
