def swap(list):
    l=len(list)
    temp=list[a-1]
    newlist[a-1]=list[b-1]
    newlist[b-1]=temp
    return(newlist)


list=[i for i in input('variables').split()]
a=int(input())
b=int(input())
newlist=list
print (swap(newlist))
