n=int(input())
list=[]
while n>=1:
    a=n//2
    b=n%2
    list.append(b)
    n=a
count=0
result=0
list1=list[::-1]
for i in range(len(list1)):
    if list1[i] == 0:
        count=0
    else:
        count=count+1
        result=max(result,count)
        
print(result)
