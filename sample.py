
###print("This is a test from the file")
##
##x = 10
##print('x = ' , str(x))
##x = 20
##print('x = ' , str(x))
##x = 30
##print('x = ' , str(x))
##
##
##
##x, y, z = 100, 10, -10
##print('X: ', x , 'Y: ', y, 'Z:', z)
##x = int(101)
##y = 11
##z = -11
##print('X: ', x , 'Y: ', y, 'Z:', z)
##
##
##
##avogadros_number = 6.022e23
##c = 2.998e8
##print("Avogadro's number =", avogadros_number)
##print("Speed of light =", c)
##
##
##
##filename = 'c:\\test\\123'
##print(filename)
##
##
##
##print('this is testing for collecting input: ')
###x = eval(input())
##
##print('Inputted text is: ', x)
##print('Inputted text type is: ', type(x))
##
##
##num1, num2 = eval(input('Enter the numbers 1 and 2: '))
##print('num1+ num2: ', num1+num2)
##
##num1 = eval(input('Enter numb1: '))
##num2 = eval(input('Enter Num2: '))
##
##print('Summmation: ', num1+num2)
##
##
##print(eval(input('Numbers are: ')))
##w, y, z = 10, 100, 112
##print(w,y,z)
##print(w,y,z, sep = ',' )
##
##
##x=6
##print(x, type(x))
##x = '7'
##print(x, type(x))
##
##print('A','B','C','D', sep = '\n')
##print('B', end = '')
##print('C', end = '')
##print('D', end = '')
##
##
##value1 = eval(input('ENter value1: '))
##value2 = eval(input('ENter value2: '))
##
##
##
##
##value3 = value1/value2
##value4 = value1 // value2
##
##print(value3)
##print(value4)
##
##
##value3, value4 = value4, value3
##
##
##print(value3)
##print(value4)
#

##
##x = 3
##print('x')
##print("x")
##print(x)
##
##
##
####n1= eval(input())
####n2 = eval(input())
####print(n1+ n2)
##
##
##a = True
##b = False
##print('a =', a, ' b =', b)
### Reassign a
##a = False;
##print('a =', a, ' b =', b)
##


##
##t1, t2 = eval(input('Enter two numbers: '))
##
##print(t1, t2)
##
##if t1 > t2:
##    print('t1 > t2')
##elif t1 == t2:
##    print('t1 = t2')
##elif t1 < t2:
##    print('t1 < t2')
##print(end='[')    


## x = 5
##y =3 
##t1, t2, t3, t4 = True, False, x == 3, y < 3

##print(t1, t2,t3,t4)

#===============================================================================
# 
# def main():
#     print("Hello World")
# 
# 
# 
# if __name__ == "__main__":
#     main()
#     print("This is a diff way")
#     
#===============================================================================


f = 0; 
print (f)


def somefunction():
    global f
    f = "def" 
    print (f)
    
somefunction()
print (f)


def func1():
    print ("This is a string")
func1()
print (func1())


def fun_with_aug(arg1, arg2):
    print(arg1, " and second arg is: ", arg2)
    
fun_with_aug(10,100)
print (fun_with_aug(10,100))



def cube(x):
    return(x*x*x)

print (cube(3))


def power (num, x=1):
    result=1 ; 
    for i in range(x):
       # print (x)
        #print (num)
        result = result*num
    return result  
    

power(2,3)    
print (power(2,5))

def multi_add(*args):
    result = 0
    for i in args :
        result = result + i 
    return result 

print(multi_add(1,2,3,4,5))

def comparision(x,y):
    if (x < y): 
        print (" x is less than y")
    elif (x == y):        
        print ("x is equal y")
    else :
        print("x is greater than y")
            
comparision(3,1)        

def comparison_2(m,n):
    st = "m is less than n " if (m < n) else " m is equal to n"
    print (st)

comparison_2(10,13)


def main():
    x = 0 
    #--------------------- while (x < 5):
        #-------- print (x)
        #----------- x = x +1
    days = ["mon", "Tue","Wed", "Thur","Fri","Sat","Sun"]    
    #for i in days:
        #if ( i == "Sat"): break
        #if (i == "Wed"): continue
        #print (i)    
    
    for i in enumerate(days):
        print (i) 
        
        
if __name__ == "__main__": 
    main()
    
