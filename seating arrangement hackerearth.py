'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
T = int(input())
for i in range(T):
    n = int(input())
    if n%12==1 or n%12==6 or n%12==0 or n%12==7:
        if n%12==1:
            print(str(n+11)+' '+"WS")

        elif n%12==0:
            print(str(n-11)+' '+"WS")

        elif n%12==6:
            print(str(n+1)+' '+"WS") 

        elif n%12==7:
            print(str(n-1)+' '+"WS")  

        else:
            pass             



    elif n%12==2 or n%12==5 or n%12==8 or n%12==11:
        if n%12==2:
            print(str(n+9)+' '+"MS")

        elif n%12==5:
            print(str(n+3)+' '+"MS")

        elif n%12==8:
            print(str(n-3)+' '+"mS") 

        elif n%12==11:
            print(str(n-9)+' '+"MS")  

        else:
            pass             



    elif n%12==3 or n%12==4 or n%12==9 or n%12==10:  
        if n%12==3:
            print(str(n+7)+' '+"AS")

        elif n%12==4:
            print(str(n+5)+' '+"AS")

        elif n%12==9:
            print(str(n-5)+' '+"AS") 

        elif n%12==10:
            print(str(n-7)+' '+"AS")  

        else:
            pass             
                    
    else:
        pass                


    
