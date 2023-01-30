def goodpair(num):
   count=0
   n=len(num)
   for i in range(n):
      for j in range(i+1,n):
         if num[i] == num[j]:
             print((i,j))
             count+=1
   return count

num=[1,2,3,1,1,3]
print(goodpair(num))
