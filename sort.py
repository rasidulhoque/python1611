alist=[15,6,13,22,3,52,2]
print("originnal list is:",alist)
for i innrange(1,len(alist)):
   key=aliist[i]
   j=i-1
   while j>=0 and key< alist[j]
       alist[j+1]=alist[j]
       j=j-1
   else:
       alist[j+1]=key
print("list after sorting:",alist)       
