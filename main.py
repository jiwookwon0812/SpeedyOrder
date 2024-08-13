
import Q

burger = ['치즈버거', '불고기버거', '새우버거', '치킨버거']
drink = ['콜라', '사이다', '제로 콜라', '제로 사이다', '오렌지 쥬스', '물', '아메리카노']
side = ["감자튀김", "치킨너겟", "치즈스틱", "어니언링", "아이스크림"]

fastmenu1 = Q.Q()
fastmenu2 = Q.Q()
slowmenu1 = Q.Q()
slowmenu2 = Q.Q()

def menu(menulist):
    sum = 0
    for i in range (len(menulist)): # 메뉴들을 리스트로 받음
        if menulist[i] in burger:
            sum += 1
        else:
            sum += 0
    if sum != 0:
        print("주문하신 메뉴는 오래 걸리는 메뉴입니다.")
        print("아래의 화면으로 준비상황을 확인해주세요.")
        print()
    else:
        print("주문하신 메뉴는 빨리 나오는 메뉴입니다.")
        print("위의 화면으로 준비상황을 확인해주세요.")
        print()
    return sum

ordernumber = 5000 # 주문번호 5000부터 시작
def order():
    global ordernumber
    menulist = []
    a = input("어떤 메뉴를 주문하시겠어요? : ")
    menulist.append(a)
    while True:
        b = int(input("더 주문하시겠어요? : 1. 네, 2. 아니오"))
        if b == 2:
            break
        else:
            c = input("어떤 메뉴를 더 주문하시겠어요? : ")
            menulist.append(c)

    ordernumber += 1
    print()
    print("=============================")
    print(menulist,"주문 완료 되었습니다. 감사합니다.")
    print("=============================")
    print()

    if (menu(menulist)) == 0:
        fastmenu1.enqueue((menulist, ordernumber))
        print("--------------------빠른 메뉴 준비중-----------------------")
        fastmenu1.print_queue()
        print("----------------------------------------------------------")
        print()
        print("--------------------빠른 메뉴 준비완료---------------------")
        fastmenu2.print_queue()
        print("----------------------------------------------------------")
        print()
    else:
        slowmenu1.enqueue((menulist, ordernumber))
        print("-------------------느린 메뉴 준비중-----------------------")
        slowmenu1.print_queue()
        print("---------------------------------------------------------")
        print()
        print("--------------------느린 메뉴 준비완료---------------------")
        slowmenu2.print_queue()
        print("----------------------------------------------------------")
        print()
    return
    

count = 0
while True:
    order()
    q = int(input("완료된 주문 건이 있습니까? : 1. 빠른메뉴 완료 2. 느린메뉴 완료 3. 아니오"))
    if q == 1:
        if fastmenu1.size == 0:
            print("준비 중인 빠른 메뉴가 없습니다.")
        else:
            num = int(input("주문번호 : "))
            fastmenu2.enqueue(fastmenu1.dequeue_target(num))
            print("-----------------------빠른 메뉴 준비중----------------------")
            fastmenu1.print_queue()
            print("------------------------------------------------------------")
            print()
            print("-----------------------빠른 메뉴 준비완료----------------------")
            fastmenu2.print_queue()
        print("-------------------------------------------------------------")
        print()
    elif q == 2:
        if slowmenu1.size == 0:
            print("준비 중인 느린 메뉴가 없습니다.")
        else:
            num = int(input("주문번호 : "))
            slowmenu2.enqueue(slowmenu1.dequeue_target(num))
            print("-----------------------느린 메뉴 준비중----------------------")
            slowmenu1.print_queue()
            print("------------------------------------------------------------")
            print()
            print("-----------------------느린 메뉴 준비완료----------------------")
            slowmenu2.print_queue()
        print("-------------------------------------------------------------")
        print()
            
    else:
        print()

    count += 1
    if count == 100:
        break

