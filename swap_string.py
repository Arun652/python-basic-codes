def swap(list):
    l=len(list)
    temp=list[a-1]
    newlist[a-1]=list[b-1]
    newlist[b-1]=temp
    return(newlist)


list=[i for i in input('variables').split()]
a=int(input("The position first indicies of the list"))
b=int(input("The position second indicies of the list"))
newlist=list
print (swap(newlist))
