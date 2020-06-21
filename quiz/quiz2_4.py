'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''
class card():
    def __init__(self):
        self.name=""
    def dis(self,n):
        if n=="영화관":
            return 0.8
        elif n=="마트":
            return 0.9
        elif n=="교통":
            return 0.9
        else:
            return 1

class Multi_card(card):
    def __init__(self):
        self.count=0
        print("카드가 발급 되었습니다.")
    def charge(self,a):
        self.count+=a
        print("{}이 충전되었습니다.".format(a))

    def consume(self, p, n):
        p*=self.dis(n)
        if p>self.count:
            print("잔액이 부족합니다.")
        else:
            self.count-=p
            print("{}에서 {}원을 사용했습니다.".format(n, p))

    def print(self):
        print("잔액이 {}원 입니다.".format(self.count))

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()