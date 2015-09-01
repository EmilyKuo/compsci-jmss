__author__ = 'ekuo1'

mylist=[41,1,15,-13,21,10]

a= len(mylist)-1
swaps=True
while swaps==True:
    swaps=False
    for i in range(a):
        if mylist[i]>mylist[i+1]:
            a=mylist[i]
            mylist[i]=mylist[i+1]
            mylist[i+1]=a
            swaps=True
        if a !=1:
            a=a-1


print(mylist)