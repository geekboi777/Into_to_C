      1
    2 3
  3 4 5
4 5 6 7
# for N = 4

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
x=1
k=0
for i in range(1,n+1):
    for k in range(n-i):
        print("",end=" ")
    j=i
    for x in range(i):
        print(j,end="")
        j+=1
    print("")

        
