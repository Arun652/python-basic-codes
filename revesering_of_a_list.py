a = input()
list=[]
temp=''
for i in a:
    if i == ' ':
        list.append(temp)
        temp=''
    else:
        temp=temp+i
if temp:
    list.append(temp)
print(list)

list2=[]
a=len(list)
for i in list:
    list2.append(list[a])
    a=a-1
print(list2)
