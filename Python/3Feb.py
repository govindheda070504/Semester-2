#program to find position of all the letters present in the string 
s1="abcagha"
start=0
str='a'
x=s1.find(str,0)
while(x1=-1)
    print(x)
    start=x+len(str)
    x=s1.find(str,start)
    
    
s1="i am learning python"
l=s1.split()
print(l)


#program to output  the name in the form of A.kumar(ankit kumar)/P.K.Rajput(pushpendra kumar rajput)/amit(amit)
short_name=" "
name=input("enter name ")
name= name.title()
l=name.split()
length=len(l)
for i in range(length-1):
  short_name=short_name+l[i][0]+"."
  short_name+=l[length-1]
  
#program to find the wheather the string is anagram 

 
