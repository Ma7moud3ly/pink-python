from sys import argv

try:
    script=argv[0]
    message  =argv[1]
    print('script name :',script)
    print('user message :',message)
except:
    print('no inputs from command line!')
    
