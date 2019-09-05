'''Calculator. An example - "calc 100*64 - (3000*0.75 + 100)*12"'''
import sys
import re
expression = ' '.join(sys.argv[1:])
not_allowed_symbols = re.findall('[^0-9)(*\-+./ ]',expression)
if len(not_allowed_symbols) != 0:
    print("only symbols 0-9 . - + / * () are allowed")
    sys.exit()
try:    
    res = eval(expression)
    print(res)
except ZeroDivisionError:
    print("oops.. divided by zero")
except Exception as e:
    print("your expression seems incorrect")
