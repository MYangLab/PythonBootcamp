
import sys
 
def dividetwo(num):
    return 2/num
 
try:
    print (dividetwo(float(sys.argv[1])))
except ValueError:
    print ('not a float!')
except IndexError:
    print ('did you put a number in the command line?')
except:
    print ('Some other error!')
