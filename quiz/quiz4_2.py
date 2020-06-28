l=[7,4,5,1,3]

for i in range(len(l)-1):
    print("\n<{}회전>".format(i+1))
    for j in range(len(l)-i-1):
        
        if l[j] > l[j+1]:
            print("{}번 인덱스에 있는 {}과 {}번 인덱스에 있는 {}를 비교하여 {}가 더 작으므로 교환".format(j,l[j],j+1,l[j+1],l[j+1]))
            l[j+1],l[j]=l[j],l[j+1]
        else:
            print("{}번 인덱스에 있는 {}과 {}번 인덱스에 있는 {}를 비교하여 {}가 더 작으므로 교환x".format(j,l[j],j+1,l[j+1],l[j]))
    print("\n결과\nlist =",l)