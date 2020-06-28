l=[9,4,3,1,12]

for i in range(len(l)):
    print("---------------------------- 주어진 위치 = {}번 인덱스 ------------------------------".format(i))
    p=i
    print("{}번 인덱스의 값은 {}입니다.".format(i,l[i]),end="")
    print("현재까지는 {}가 최소값입니다.".format(l[i]))
    for j in range(i+1,len(l)):
        print("{}번 인덱스의 값은 {}입니다.".format(j,l[j]),end="")
        if l[p]>l[j]:
            print("{}는 {}보다 작으므로 {}이 최소값입니다.".format(l[j],l[p],l[j]))
            p=j
        else:
            print("{}는 {}보다 작으므로 {}이 최소값입니다.".format(l[p],l[j],l[p]))
    print("최소값은 {}번 인덱스의 {}입니다.".format(p,l[p]))
    print("\n\n{}번 인덱스의 {}를 {}번 인덱스로 옮기고,\n{}번 인덱스의 {}를 {}번 인덱스로 옮깁니다.\n\n".format(p,l[p],i,i,l[i],p))
    l[p],l[i] = l[i],l[p]
    print(l)
    print("{}번 인덱스까지 정렬되었습니다.".format(i))                