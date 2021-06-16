a=input()
list=[]
temp = ''
for i in a:
    if i == " ":
        list.append(temp)
        temp=''
    else:
        temp=temp+i
if temp:
    list.append(temp)
print(list)
