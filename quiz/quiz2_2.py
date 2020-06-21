'''
2.
년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하는 함수를 만드세요.
테스트코드
<입력>
print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))
<출력>
연도를 입력하시오 : 2020
월을 입력하시오 : 3
일을 입력하시오 : 13
2020년 3월 13일은 금요일 입니다.
'''
import datetime
def printDayOfTheWeek(y,m,d):
    w=datetime.date(y,m,d).weekday()
    if w==6:
        return "일요일"
    elif w==5:
        return "토요일"
    elif w==4:
        return "금요일"
    elif w==3:
        return "목요일"
    elif w==2:
        return "수요일"
    elif w==1:
        return "화요일"
    else:
        return "월요일"
    return None

myYear=int(input("연도를 입력하시오 : "))
myMonth=int(input("월을 입력하시오 : "))
myDay=int(input("일을 입력하시오 : "))

print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))