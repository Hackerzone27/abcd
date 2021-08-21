T = int(input())
caselist = []
for i in range(T):
    x = input()
    x = x.split()
    N = int(x[0])
    B = int(x[1])
    l = input()
    l = l.split()
    temp = []
    for j in l:
        temp.append(int(j))
    temp.sort()
    s = 0
    n = 0
    for k in temp:
        s+=k
        if s<=B:
            n+=1
        else:
            print(f"Case #{i+1}: {n}")
            break