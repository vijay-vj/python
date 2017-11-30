
class myClass():
    def method1(self):
        print ("This is method 1")
     
    def method2(self, str):   
        print("Second method " + str)
        
def main():
    x =0 
    c = myClass()
    c.method1()
    c.method2("is with string as input")
    f = secondClass()
    f.method1()
    f.method3("Implementing the inheritance  ")
    
    
class secondClass(myClass):
    def method3(self, str):    
        print("This is the dependent class")
    
    def method1(self):
        myClass.method1(self);
        print ("We are in method 1 of implemented class")
        
if __name__ == "__main__": 
    main()