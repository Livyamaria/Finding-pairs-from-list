llist=[]
set1=[]
n=int(input("enter the limit"))
for i in range (0,n):
    ele=int(input("enter the value"))
    llist.append(ele)
print(llist)
ln=len(llist)
target=10
for i in range(0,ln):
    match=target-llist[i]
    if match in set1:
        print(llist[i],match)
    else:
        set1.append(llist[i])


