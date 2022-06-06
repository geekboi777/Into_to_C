# N = 4

# 1
# 23
# 345
# 4567

n=int(input())
x=1
for i in range(1,n+1):
    j=i
    for x in range(i):
        print(j,end="")
        j+=1
    print("")

        
