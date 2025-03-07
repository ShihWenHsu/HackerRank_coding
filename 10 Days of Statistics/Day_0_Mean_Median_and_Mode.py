# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

N=input()
n=int(N)
ARRAY=list(map(int, input().split()))
SUM=0
for i in range(n):
    SUM+=ARRAY[i]
    #print(ARRAY[i])

#AVERAGE
MEAN = float(SUM/n)
print(MEAN)


#Sorting
ARRAY.sort()
mid = int(n/2)
#print(mid) 

if n % 2 == 0:
    median = (ARRAY[mid] + ARRAY[mid-1])/2
else:
    median = ARRAY[mid]
print(median)

     
#duplicate
tmp = Counter(ARRAY)
common_list = tmp.most_common()
mode = common_list[0][0]

#print(min(ARRAY))
print(mode)
