#l=[9,4,3,1,12]
l=[12,8,4,6,2,4,9,32,45,7,68,21,95,42,1]
for i in range(len(l)-1):
    print("\n우리에게는 {}라는 정렬된 리스트가 있습니다.".format(l[0:i+1]))
    print("원소 {}가 추가됩니다.".format(l[i+1]))
    for j in range(i+1,0,-1):
        if l[j]<l[j-1]:
            print("{}는 {}번 인덱스 {}보다 작으므로, {}인덱스 {}를 한칸 뒤로 옮깁니다.".format(l[j],j-1,l[j-1],j-1,l[j-1]))
            l[j],l[j-1]=l[j-1],l[j]
        else:
            print("{}을 {}번 인덱스에 삽입합니다.".format(l[j],j))
            break
        if j==1:
            print("{}을 {}번 인덱스에 삽입합니다.".format(l[j-1],j-1))
            break
    
print("\n결과\n",l)