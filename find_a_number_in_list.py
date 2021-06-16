a=input("Enter the elements of number ")  
list = []
tmp = ''
for i in a:
    if i == ' ':
        list.append(tmp)
        tmp = ''
    else:
        tmp = tmp + i
if tmp:
    list.append(tmp)
#print(list)
def find(list):
    b=(input("The elements to be search in list"))
    if b in list:
        return("found")
    else:
        return("not found")
print(find(list))
