"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(a,b):
    while True:
        if a==b:
            return a
        elif a>b:
            a-=b
        elif b>a:
            b-=a
        else:
            return 1
print(gcd(12,6))