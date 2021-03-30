import tkinter as tk
import sys

# degree = {"0단계: 백색 국물", "1단계: 순한맛", "2단계: 중간맛", "3단계: 매운맛"}
weight_meal = {"청경채": 1, "숙주(1묶음)": 4, "검은목이버섯": 3, "흰목이버섯": 3, "건두부": 1, "감자": 2, "수제비": 5, "떡국떡": 6, "브로콜리": 5, "단호박": 3
               , "유부": 3, "팽이버섯(1묶음)": 15, "느타리버섯(1묶음)": 20, "새송이버섯": 6, "알배추": 3, "시금치": 2, "중국당면": 4, "옥수수면(1묶음)": 20,
               "쌀국수면(1묶음)": 20, "감자당면(1묶음)": 20, "수정당면(1묶음)": 20, "분모자": 10}
price_drink = {"쥬시쿨(복숭아)": 1200, "쥬시쿨(자두)": 1200, "환타(파인애플)": 1200, "환타(포도)": 1200, "환타(오렌지)": 1200}
price_side = {"라면사리": 1000, "우동사리": 1000, "도삭면": 2000, "양고기(100g)": 3000, "소고기(100g)": 3000, "꿔바로우[중]": 9900, "꿔바로우[대]": 15000}
price_stick = {"새우 꼬치": 1000, "소시지 꼬치": 1000, "순대 꼬치": 1000, "어묵 꼬치": 1000, "메추리알 꼬치": 1000}

order_meal = {}  # 재료(무게)
order_drink = {}  # 음료(1200원)
order_side = {}  # 사이드 메뉴
order_stick = {}  # 꼬치(1000원)

total_price = 0  # 가격
total_weight = 0  # 재료 무게


def show_meal():
    btn_meal.configure(bg="yellow")
    btn_drink.configure(bg="white")
    btn_side.configure(bg="white")
    btn_stick.configure(bg="white")
    frame6.pack_forget()  # pack_forget()을 사용해서 화면에서 없앰
    frame5.pack_forget()
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill="both", expand=True)  # 재료 영역
    frame6.pack(fill="both", expand=True)  # 텍스트 영역


def show_drink():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="yellow")
    btn_side.configure(bg="white")
    btn_stick.configure(bg="white")
    frame6.pack_forget()
    frame5.pack_forget()
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)  # 음료 영역
    frame6.pack(fill="both", expand=True)  # 텍스트 영역


def show_side():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="white")
    btn_side.configure(bg="yellow")
    btn_stick.configure(bg="white")
    frame6.pack_forget()
    frame5.pack_forget()
    frame3.pack_forget()
    frame2.pack_forget()
    frame4.pack(fill="both", expand=True)  # 사이드 메뉴 영역
    frame6.pack(fill="both", expand=True)  # 텍스트 영역


def show_stick():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="white")
    btn_side.configure(bg="white")
    btn_stick.configure(bg="yellow")
    frame6.pack_forget()
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack_forget()
    frame5.pack(fill="both", expand=True)  # 꼬치 영역
    frame6.pack(fill="both", expand=True)  # 텍스트 영역


# 재료 추가
def meal_add(w):
    global weight_meal, order_meal, total_price, total_weight
    if w not in weight_meal:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_weight = weight_meal.get(w)
    total_weight += this_weight

    total_price = 7000

    ok = "350"

    # 무게
    if w in order_meal:
        order_meal[w] = order_meal.get(w) + 1
    else:
        order_meal[w] = 1
    # 가격
        if w == ok:
            total_price == 7000
        elif w >= ok:
            total_price += 100
        elif w < ok:
            print("350g 이상부터 계산 가능합니다.")
            total_price == 0

    print_order()
    print_weight()
    print_price()


# 음료 추가
def drink_add(m):
    global price_drink, order_drink, total_price
    if m not in price_drink:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_drink.get(m)
    total_price += this_price

    if m in order_drink:
        order_drink[m] = order_drink.get(m) + 1
    else:
        order_drink[m] = 1
    print_order()
    print_price()


# 사이드 메뉴 추가
def side_add(m):
    global price_side, order_side, total_price
    if m not in price_side:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_side.get(m)
    total_price += this_price

    if m in order_side:
        order_side[m] = order_side.get(m) + 1
    else:
        order_side[m] = 1
    print_order()
    print_price()


# 꼬치 추가
def stick_add(m):
    global price_stick, order_stick, total_price
    if m not in price_stick:
        print("입력한 메뉴가 존재하지 않습니다.")
    this_price = price_stick.get(m)
    total_price += this_price

    if m in order_stick:
        order_stick[m] = order_stick.get(m) + 1
    else:
        order_stick[m] = 1
    print_order()
    print_price()


def print_order():
    global order_meal, order_drink, order_side, order_stick

    tmp = ""
    for i in order_meal:
        tmp = tmp + i + " X " + str(order_meal.get(i)) + "\n"
    for i in order_drink:
        tmp = tmp + i + " X " + str(order_drink.get(i)) + "\n"
    for i in order_side:
        tmp = tmp + i + " X " + str(order_side.get(i)) + "\n"
    for i in order_stick:
        tmp = tmp + i + " X " + str(order_stick.get(i)) + "\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)


def print_price():
    global total_price
    label_price.configure(text="총 금액 : " + str(total_price) + " 원")


def print_weight():
    global total_weight
    label_weight.configure(text="총 무게 : " + str(total_weight) + " g")


def order_end():
    global total_price, total_weight, order_meal, order_drink, order_side, order_stick
    total_price = 0
    total_weight = 0
    del order_meal
    del order_drink
    del order_side
    del order_stick

    order_meal = {}
    order_drink = {}
    order_side = {}
    order_stick = {}
    print_price()
    print_weight()
    print_order()
    show_meal()


window = tk.Tk()
window.title("마라탕탕 키오스크")
window.geometry("1300x700+100+50")  # 가로 크기, 세로 크기, 초기화면 x좌표, 초기화면 y좌표
window.resizable(False, False)  # 가로, 세로 크기조정 못함
# 상단 버튼들
frame1 = tk.Frame(window, width="1300", height="10")
frame1.pack(fill="both")
# 재료
frame2 = tk.Frame(window, width="1300")
frame2.pack(fill="both", expand=True)
# 음료
frame3 = tk.Frame(window, width="1300", height="10")
frame3.pack(fill="both", expand=True)
# 사이드 메뉴
frame4 = tk.Frame(window, width="1300", height="10")
frame4.pack(fill="both", expand=True)
# 꼬치
frame5 = tk.Frame(window, width="1300", height="10")
frame5.pack(fill="both", expand=True)

# 하단에 주문 내역과 수량이 표시
frame6 = tk.Frame(window, width="1300")
# frame6.pack(fill="both", expand=True)


btn_meal = tk.Button(frame1, text="재료\n(350g부터)", padx="10", pady="10", bg="yellow", command=show_meal)
btn_meal.grid(row=0, column=0, padx=10, pady=10)

btn_drink = tk.Button(frame1, text="음료\n(1200원)", padx="10", pady="10", bg="white", command=show_drink)
btn_drink.grid(row=0, column=1, padx=10, pady=10)

btn_side = tk.Button(frame1, text="사이드\n메뉴", padx="10", pady="10", bg="white", command=show_side)
btn_side.grid(row=0, column=2, padx=10, pady=10)

btn_stick = tk.Button(frame1, text="꼬치\n(1000원)", padx="10", pady="10", bg="white", command=show_stick)
btn_stick.grid(row=0, column=3, padx=10, pady=10)

label_price = tk.Label(frame1, text="총 금액 : 0 원", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="4", padx="10", pady="10")

label_weight = tk.Label(frame1, text="총 무게 : 0 g", width="20", padx=10, pady="10", fg="#FE2EC8",  font='Arial 15')
label_weight.grid(row=0, column="5", padx="10", pady="10")

btn_end = tk.Button(frame1, text="주문종료", padx="10", pady="10", command=order_end)
btn_end.grid(row=0, column=6, padx=10, pady=10)


# 재료
btn_meal_1 = tk.Button(frame2, text="청경채", padx="10", pady="10", width="10", command=lambda: meal_add('청경채'))
btn_meal_1.grid(row=0, column=0, padx=10, pady=10)

btn_meal_2 = tk.Button(frame2, text="숙주\n(1묶음)", padx="10", pady="10", width="10", command=lambda: meal_add('숙주(1묶음)'))
btn_meal_2.grid(row=0, column=1, padx=10, pady=10)

btn_meal_3 = tk.Button(frame2, text="검은목이\n버섯", padx="10", pady="10", width="10", command=lambda: meal_add('검은목이버섯'))
btn_meal_3.grid(row=0, column=2, padx=10, pady=10)

btn_meal_4 = tk.Button(frame2, text="흰목이\n버섯", padx="10", pady="10", width="10", command=lambda: meal_add('흰목이버섯'))
btn_meal_4.grid(row=0, column=3, padx=10, pady=10)

btn_meal_5 = tk.Button(frame2, text="감자", padx="10", pady="10", width="10", command=lambda: meal_add('감자'))
btn_meal_5.grid(row=0, column=4, padx=10, pady=10)

btn_meal_6 = tk.Button(frame2, text="수제비", padx="10", pady="10", width="10", command=lambda: meal_add('수제비'))
btn_meal_6.grid(row=0, column=5, padx=10, pady=10)

btn_meal_7 = tk.Button(frame2, text="떡국떡", padx="10", pady="10", width="10", command=lambda: meal_add('떡국떡'))
btn_meal_7.grid(row=0, column=6, padx=10, pady=10)

btn_meal_8 = tk.Button(frame2, text="브로콜리", padx="10", pady="10", width="10", command=lambda: meal_add('브로콜리'))
btn_meal_8.grid(row=0, column=7, padx=10, pady=10)

btn_meal_9 = tk.Button(frame2, text="단호박", padx="10", pady="10", width="10", command=lambda: meal_add('단호박'))
btn_meal_9.grid(row=0, column=8, padx=10, pady=10)

btn_meal_10 = tk.Button(frame2, text="유부", padx="10", pady="10", width="10", command=lambda: meal_add('유부'))
btn_meal_10.grid(row=0, column=9, padx=10, pady=10)

btn_meal_11 = tk.Button(frame2, text="팽이버섯\n(1묶음)", padx="10", pady="10", width="10", command=lambda: meal_add('팽이버섯(1묶음)'))
btn_meal_11.grid(row=1, column=0, padx=10, pady=10)

btn_meal_12 = tk.Button(frame2, text="느타리버섯\n(1묶음)", padx="10", pady="10", width="10", command=lambda: meal_add('느타리버섯(1묶음)'))
btn_meal_12.grid(row=1, column=1, padx=10, pady=10)

btn_meal_13 = tk.Button(frame2, text="새송이\n버섯", padx="10", pady="10", width="10", command=lambda: meal_add('새송이버섯'))
btn_meal_13.grid(row=1, column=2, padx=10, pady=10)

btn_meal_14 = tk.Button(frame2, text="알배추", padx="10", pady="10", width="10", command=lambda: meal_add('알배추'))
btn_meal_14.grid(row=1, column=3, padx=10, pady=10)

btn_meal_15 = tk.Button(frame2, text="시금치", padx="10", pady="10", width="10", command=lambda: meal_add('시금치'))
btn_meal_15.grid(row=1, column=4, padx=10, pady=10)

btn_meal_16 = tk.Button(frame2, text="중국당면", padx="10", pady="10", width="10", command=lambda: meal_add('중국당면'))
btn_meal_16.grid(row=1, column=5, padx=10, pady=10)

btn_meal_17 = tk.Button(frame2, text="옥수수면\n(1묶음)", padx="10", pady="10", width="10", command=lambda: meal_add('옥수수면(1묶음)'))
btn_meal_17.grid(row=1, column=6, padx=10, pady=10)

btn_meal_18 = tk.Button(frame2, text="쌀국수면\n(1묶음)", padx="10", pady="10", width="10", command=lambda: meal_add('쌀국수면(1묶음)'))
btn_meal_18.grid(row=1, column=7, padx=10, pady=10)

btn_meal_19 = tk.Button(frame2, text="감자당면\n(1묶음)", padx="10", pady="10", width="10", command=lambda: meal_add('감자당면(1묶음)'))
btn_meal_19.grid(row=1, column=8, padx=10, pady=10)

btn_meal_20 = tk.Button(frame2, text="수정당면\n(1묶음)", padx="10", pady="10", width="10", command=lambda: meal_add('수정당면(1묶음)'))
btn_meal_20.grid(row=1, column=9, padx=10, pady=10)

btn_meal_21 = tk.Button(frame2, text="분모자", padx="10", pady="10", width="10", command=lambda: meal_add('분모자'))
btn_meal_21.grid(row=1, column=10, padx=10, pady=10)


# 음료
btn_drink_1 = tk.Button(frame3, text="쥬시쿨\n(복숭아)", padx="10", pady="10", width="10", command=lambda: drink_add('쥬시쿨(복숭아)'))
btn_drink_1.grid(row=0, column=0, padx=10, pady=10)

btn_drink_2 = tk.Button(frame3, text="쥬시쿨\n(자두)", padx="10", pady="10", width="10", command=lambda: drink_add('쥬시쿨(자두)'))
btn_drink_2.grid(row=0, column=1, padx=10, pady=10)

btn_drink_3 = tk.Button(frame3, text="환타\n(파인애플)", padx="10", pady="10", width="10", command=lambda: drink_add('환타(파인애플)'))
btn_drink_3.grid(row=0, column=2, padx=10, pady=10)

btn_drink_4 = tk.Button(frame3, text="환타\n(포도)", padx="10", pady="10", width="10", command=lambda: drink_add('환타(포도)'))
btn_drink_4.grid(row=0, column=3, padx=10, pady=10)

btn_drink_5 = tk.Button(frame3, text="환타\n(오렌지)", padx="10", pady="10", width="10", command=lambda: drink_add('환타(오렌지)'))
btn_drink_5.grid(row=0, column=4, padx=10, pady=10)


# 사이드 메뉴
btn_side_1 = tk.Button(frame4, text="라면사리\n(1000원)", padx="10", pady="10", width="10", command=lambda: side_add('라면사리'))
btn_side_1.grid(row=0, column=0, padx=10, pady=10)

btn_side_2 = tk.Button(frame4, text="우동사리\n(1000원)", padx="10", pady="10", width="10", command=lambda: side_add('우동사리'))
btn_side_2.grid(row=0, column=1, padx=10, pady=10)

btn_side_3 = tk.Button(frame4, text="도삭면\n(1000원)", padx="10", pady="10", width="10", command=lambda: side_add('도삭면'))
btn_side_3.grid(row=0, column=2, padx=10, pady=10)

btn_side_4 = tk.Button(frame4, text="양고기(100g)\n(3000원)", padx="10", pady="10", width="10", command=lambda: side_add('양고기(100g)'))
btn_side_4.grid(row=0, column=3, padx=10, pady=10)

btn_side_5 = tk.Button(frame4, text="소고기(100g)\n(3000원)", padx="10", pady="10", width="10", command=lambda: side_add('소고기(100g)'))
btn_side_5.grid(row=0, column=4, padx=10, pady=10)

btn_side_6 = tk.Button(frame4, text="꿔바로우[중]\n(9900원)", padx="10", pady="10", width="10", command=lambda: side_add('꿔바로우[중]'))
btn_side_6.grid(row=0, column=5, padx=10, pady=10)

btn_side_7 = tk.Button(frame4, text="꿔바로우[대]\n(15000원)", padx="10", pady="10", width="10", command=lambda: side_add('꿔바로우[대]'))
btn_side_7.grid(row=0, column=6, padx=10, pady=10)


# 꼬치
btn_stick_1 = tk.Button(frame5, text="새우\n꼬치", padx="10", pady="10", width="10", command=lambda: stick_add('새우 꼬치'))
btn_stick_1.grid(row=0, column=0, padx=10, pady=10)

btn_stick_2 = tk.Button(frame5, text="소시지\n꼬치", padx="10", pady="10", width="10", command=lambda: stick_add('소시지 꼬치'))
btn_stick_2.grid(row=0, column=1, padx=10, pady=10)

btn_stick_3 = tk.Button(frame5, text="순대\n꼬치", padx="10", pady="10", width="10", command=lambda: stick_add('순대 꼬치'))
btn_stick_3.grid(row=0, column=2, padx=10, pady=10)

btn_stick_4 = tk.Button(frame5, text="어묵\n꼬치", padx="10", pady="10", width="10", command=lambda: stick_add('어묵 꼬치'))
btn_stick_4.grid(row=0, column=3, padx=10, pady=10)

btn_stick_5 = tk.Button(frame5, text="메추리알\n꼬치", padx="10", pady="10", width="10", command=lambda: stick_add('메추리알 꼬치'))
btn_stick_5.grid(row=0, column=4, padx=10, pady=10)

# text = open('complete.txt', 'a')
# 주문 리스트
text_1 = tk.Text(frame6, height="10")
text_1.pack()
# text.write(text_1)
# text.close()

window.mainloop()