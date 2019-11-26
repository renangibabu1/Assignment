"""
list = ['aman',34,43.4,'saurav']
print(list)

a = int(input("Enter a number :" ))
b = int(input("Enter a number :" ))
c = int(input("Enter a number :" ))


if a>b and a>c:
    print("a is large :",a)
elif b>c and b>a:
    print("b is large :",b)
elif c>a and c>b:
    print("c is large:",c)
else:
          print("value D")

age = int(input("Enter age :"))
if age >= 18:
    print(" valid to voting")
else:
    print("not valid to vote ")
   


num = int(input(" Enter Number :"))
if num == 10:
    print("number :",num)
elif num == 20:
    print("number :",num)    
elif num == 30:
    print("number :",num)
else:
    print(" number is not valid ")


marks = int(input("Enter student marks :"))
if marks > 85 and marks < 100:
    print(" A grade ")
elif marks > 70 and marks < 85:
    print(" A+ grade ")
elif marks > 55 and marks < 70:
    print("b grade ")
elif marks > 35 and marks < 55:
    print("C grade ")
else:
    print("D grade")

i=10
while i > 0:
    print(i)
    i -=1
else:
    print("the while is exhausted")

    
i = 1
while i <= 10:
    print(i)
    i +=1
    if i == 3:
        break
else:
    print("the while is exhausted")
   

list =[1,2,3,4]  
count = 1;  
for i in list:  
    if i == 4:  
        print("item matched")  
        count = count + 1;  
        break  
print("found at",count,"location");


i = 0
while 1:
    print(i,"",end="")
    i +=1
    if i == 10:
        break
print("came out of while loop")


i = 0;  
while i!=10:  
    print("%d"%i);  
    continue;  
    i=i+1;  
str = "Hi Python !"
print(str,type(str),len(str))
print(str[10])
print(str[9])
print(str[8])
print(str[7])
print(str[6])
print(str[5])
print(str[4])
print(str[3])
print(str[2])
print(str[1])
print(str[0])
print(str[:])
  

integer = 10
float = 20.12
string = "babu"
print("{} is integer {} is float {} is string".format(integer,float,string))



str = "Java is a programming language"   
str2 = str.partition("is")  
print(str2)

str = "Java is a programming language"   
str2 = str.partition("av")  
print(str2)


text = " zfill example"
a = text.zfill(20)
print(a)
"""
"""
str = "Hello javaTpoint"
str1 = str.upper()
print(str1)

str = "Hello javaTpoint"
str1 = str.lower()
print(str1)

str = "Hello javaTpoint"
str1 = str.isupper()
print(str1)

str = "Hello javaTpoint"
str1 = str.islower()
print(str1)

str = "Hello javaTpoint"
str1 = str.capitalize()
print(str1)

str = "Hello javaTpoint"
str1 = str.casefold()
print(str1)

str = "Hello javaTpoint"
str1 = str.swapcase()
print(str1)

str = "Hello javaTpoint"
str1 = str.title()
print(str1)

str = "Hello javaTpoint"
str1 = str.istitle()
print(str1)

str = "Hello javaTpoint"
str1 = str.find("a")
print(str1)

str = "Hello javaTpoint"
str1 = str.isnumeric()
print(str1)

str = "Hello javaTpoint"
str1 = str.isdigit()
print(str1)

str = "Hello javaTpoint"
str1 = str.isalpha()
print(str1)

str = "Hello javaTpoint"
print(str.count("l",3))

"""
"""
l = [2,5,1,3]
for x in l:
    print(x)
l.append(4)
print(l)

l.pop()
print(l)

l = [2,5,1,3]
l1 = [8,7,5,6,9]
l.extend(l1)
print(l)

l = [2,5,1,3]
for x in l:
    print(x)
l1 = [8,7,5,6,9]
l.append(l1)
print(l)

l1.append([2,5,4,3])
print(l)

l = [2,5,1,3]
for x in l:
    print(x)
l.clear()

apple = ['a','p','p','l','e']
apple.sort()
print(apple)
apple.sort(reverse=True)
print(apple)
even=[2,4,6,8]
even.sort()
print(even)


apple = ['a','p','p','l','e']
apple.reverse()
print(apple)


list = ['1','2','3']
for i in list:
    print(i)
print("Before removing")
list.remove('2')
print("After removing")
for i in list:
    print(i)

list = ['1','2','3']
for i in list:
    print(i)
list.insert(3,['4','5','6'])
print("inserting")
print(list)
for i in list:
    print(i)

list = ['1','2','3']
list1 = ['5','4','8','7']
list.extend(list1)
print(list)
for x in list:
    print(x)


list = ['1','2','3']
list1 = list.copy()
print(list1)

list = ['1','2','3']
list1=[]
list1 = list[:]
print(list1)

list = ['1','2','3']
a = max(list)
print(a)

list = ['1','2','3']
a = min(list)
print(a)


tuple1 = (10, 20, 30, 40, 50, 60)  
print(tuple1)  
count = 0  
for i in tuple1:  
    print(count, i);

employees=list(((101,'babu',1),(102,'abc',2),(103,'def',3),(104,'ghi',4)))
print("__printing list__")
for i in employees:
    print(i)
employees[0] = (100,'amma',0)
print(employees)
print(len(employees),type(employees))
a = employees[0]
print(a)
print(employees[-2])

days = {"monday","tuesday","wednesday","thursdady","friday","saturday","sunday"}
print(days)
for i in days:
    print(i)

days = set(["monday","tuesday","wednesday","thursdady","friday","saturday","sunday"])
print(days)
for i in days:
    print(i)

Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)
Months.update(["july","august","september","october"])
'''print(Months)'''
Months.discard("June")
print(Months)


day1 = {"monday","tuesday","wednesday","thursday"}
day2 = {"friday","saturday","sunday"}
print(day1|day2)
print(day1.pop())
print(day1.discard("feb"))

inventory = {"shirts":25,"paints":220,"shock":434,"tshirts":250}
element = inventory.pop("shirts")
print(element)
print(" after pop using in dictionary")
print(inventory)

inventory = {"shirts":25,"paints":220,"shock":434,"tshirts":250}
element = inventory.pop("shoes")
print(element)
print(" after pop using in dictionary")
print(inventory)
"""
'''
inventory = {"shirts":25,"paints":220,"shock":434,"tshirts":250}
element = inventory.popitem()
print(element)
print(" after pop using in dictionary")
print(inventory)
print(inventory.has_key("shirts"))'''

'''
n = input("number of lines :")
for i in range(int(n)):
    s = input()
    alphabet = "skjgfhasjfg"
    result=''
    for x in s:
        for pos in range(52):
            if alphabet[pos] == x:
                i = pos
        if x not in alphabet or i>=26:
            result +=x
        else:
            result += alphabet[i+26]
        print(result)'''
    

'''
heads = int(input('Enter the total number of heads:'))
legs = int(input('Enter the total number of legs:'))
if legs % 2 !=0 or heads ==0 or heads > legs:
    print('No solution')
else:
    r = int((legs + (-2*heads))/2)
    c = int(heads - r)
    print('{} {}'.format(c,r))
'''

# Python code to remove duplicate elements 
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      

duplicate = [1,2,55,1,3,2,34,55] 
print(Remove(duplicate))



























    


















































    








































    


















































    












































    


















































    








