# n=int(input("enter number:"))
# if (n>0):
#     print("it is positive")
# elif (n<0):
#     print("it is negetive")
# else:
#     print("it is zero")


# year=2020
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("it is leap year")
# else:
#     print("it is not leap year")


# x=input("enter char:")
# v=['a','e','i','o','u']
# if x in v:
#     print("vowel")
# else:
#     print("consonent")


# n1=input("enter char:")
# n2=n1 [::-1]
# if n1==n2:
#     print("it is palidromme")
# else:
#     print("not palidrome")


# username=input("enter username:")
# password=input("enter password:")
# if username == "hitesh" and password =="1234":
#     print("granted")
# else:
#     print("not granted")


# x=1
# while(x<11):
#     print(x)
#     x=x+1


# x=2
# while(x<=100):
#     print(x)
#     x=x+2


# x=100
# while(x>=2):
#     print(x)
#     x=x-2


# x=101
# while(x>1):
#     print(x)
#     x=x-2



# x=int(input("enter number:"))
# factorial=1
# while(x>1):
#     factorial*=x
#     x=x-1
# print(factorial)


# username=input("enter username:")
# password=input("enter password:")
# while True:
#     if username=="hitesh" and password=="1234":
#         print("succesfullly login")
#         break
#     else:
#        print("enter again")



# n=int(input("enter number:"))
# a=0
# b=1
# print(a)
# while(b<n):
#     print(b)
#     c=a+b
#     a=b
#     b=c



# s=" hitesh dhakad ward no twenty shirpur"
# search=input("char:")
# count=0
# for char in s:
#     if char==search:
#         count=count+1
# print(f"the char:{search} occur:{count} time in the string")


# x=[10,20,30]
# x.append(40)
# print(x)

# x=[10,20,33,40]
# x.insert(2,30)
# print(x)

# x=[10,20,30]
# y=[40,50,60]
# x.extend(y)
# print(x)

# x=[10,20,30]
# y=[40,50,60]
# z=(x+y)
# print(z)


# x=[1,2,3,4,5]
# y=[4,5,6,7,8]
# common=[]
# for i in x:
#     if i in y:
#         common.append(i)
#         print(common)


# x=[1,2,3,4,5]
# print(len(x))

# x=[10,20,30,40,50]
# x[1]=100
# print(x)

# x=[10,20,30,40,50]
# x.remove(20)
# print(x)


# x=[10,20,30,40,50]
# del x[0]
# print(x)


# x=[10,20,30,40,50]
# x.clear()
# print(x)



# x=[10,20,30,40,50]
# x.sort()
# print()


# x=[10,20,30,40,50]
# x.sort(reverse=True)
# print()


# x=[10,20,30,40,50]
# i=0
# while(i<len(x)):
#     print(x[i])
#     i=i+1


# input_list=[1,1,2,2,3,3,4,4]
# unique_list=input(set(input_list))
# print("remove duplicate",unique_list)


# x=int(input("enter number:"))
# even=[]
# i=2
# while(i<100):
#     even.append(i)
#     i=i+2 
# print(even)

# x=int(input("enter number:"))
# odd=[]
# i=1
# while(i<100):
#     odd.append(i)
#     i=i+2 
# print(odd)

# x=[1,2,3,4,5, -1,-2,-3,-4,-5]
# pos=[]
# neg=[]
# i=0
# while(i<len(x)):
#     if x[i]>0:
#         pos.append(x[i])
#     else:
#         neg.append(x[i])
#     i=i+1
# print(pos)
# print(neg)


# x=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# i=2
# while(i<10):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#     i=i+1
# print(even)
# print(odd)


# my_list=[i for i in range(10)]
# print(my_list)

# my_list=[i for i in range(1,11) if i%2==0]
# print(my_list)

# my_list=[i for i in range(1,11) if i%2!=0]
# print(my_list)


# my_list=[i**2 for i in range(1,11) if i%3==0]
# print(my_list)

# my_list=[i*2 for i in range(1,11) if i%2==0]
# print(my_list)

# my_list=[[x*y for y in range(5)]for x in range(5)]
# print(my_list)


# my_list=[[x*y for y in range(5) if y%2==0]for x in range(5) if x%2==0]
# print(my_list)


# x=[10,20,30,40]
# for i in x:
#  print(x)



# x=[1,2,3,4,5, -1,-2,-3,-4,-5]
# pos=[]
# neg=[]
# for i in x:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(pos)
# print(neg)


# x=["apple","banan","mango"]
# for i in x:
#     if i=="banan":
#      continue
# print(x)

# x=[10,20,30,40,50]
# for i in x:
#     if i==30:
#         print("present")
#         break
# else:
#         print("not present")



# for i in range(10):
#     if i==5:
#         break
#     print(i)


# n=int(input("enter number:"))
# factorial=1
# if n>=1:
#     for i in range(1,n+1):
#         factorial*=i
#     print(factorial)


# x=[10,20,30,40,100,200,400,500]
# count=0
# for i in x:
#     if 10<= i<=99:
#         count=count+1
# print("two digit",count)

# x=[10,20,30,40,100,200,400,500,600]
# count=0
# for i in x:
#     if 99<= i<=999:
#         count=count+1
# print("three digit",count)


# x=[0,20,30,40,100,200,400,500,600]
# total_sales=sum(x)
# print(total_sales)


# x=[0,20,30,40,100,200,400,500,600]
# min_sales=min(x)
# print(min_sales)


# x=[0,20,30,40,100,200,400,500,600]
# avg_sales=sum(x)/ len(x)
# print(avg_sales)

# for i in range(2,100,2):
#     print(i)


# for i in range(1,100,2):
#     print(i)

# for i in range(1011,2,-2):
#     print(i)


# x={"name":"hitesh","age":23,"city":"pune"}
# print(x)

# x={"name":"hitesh","age":10}
# x["age"]=23
# print(x)

# x={"name":"hitesh","age":10}
# x["city"]="pune"
# print(x)

# x={"name":"hitesh"}
# x.update({"age":23,"city":"pune"})
# print(x)


# x={"name":"hitesh","age":23,"city":"pune"}
# x.pop('name')
# print(x)

# x={"name":"hitesh","age":23,"city":"pune"}
# x.popitem()
# print(x)


# x={"name":"hitesh","age":23,"city":"pune"}
# y=x.copy()
# print(y)

# x={"name":"hitesh","age":23,"city":"pune"}
# for i in x:
#  print(i)

# x={"name":"hitesh","age":23,"city":"pune"}
# for i in x:
#  print(x[i])

# x={"name":"hitesh","age":23,"city":"pune"}
# for i in x.items():
#  print(i)



n=int(input("enter number:"))
count=0
i=1
while(i<=n):
    if i%n==0:
        count=count+1
        i=i+1
    if(count==2):
     print("it is prime")
     break
else:
    print("not prime")