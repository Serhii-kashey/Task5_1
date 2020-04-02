#Task2_1
a=0
b=100
n1=input("Please, input number's between \n H= %d and P= %d using spaces as spliter and press enter: " %(b,a) )
n2=n1.replace('-',"")
nn=n2.split(" ")
lengh=(len(nn))
n=n1.split(" ")
s=1
ss=0
ssg=0
for i in n:
    si=int(i)
   
    if si > b:
        
        s*=si
    elif si < a:
        ss+=si
    else:
        ssg+=1
print("Numbers between H and P are: %d "%ssg)
print("Sum of numbers less than P : %d "%ss)
print("Mult of numbers more than H are: %d "%s)

        
