from tkinter import*

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

###################################################
# 여러개의 옵션 중에 하나를 선택할 수 있는 라디오버튼 위젯

# 버거 주문칸 
label1 = Label(root, text = "메뉴를 선택하세요").pack()

burger_var = IntVar() # 다 같은 세트로 묶어줘야하기 땜에 var하나만 만들어두됨
btn_burger1 = Radiobutton(root, text = "햄버거", value = 1, variable = burger_var)
btn_burger2 = Radiobutton(root, text = "불고기버거", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "치즈버거", value = 3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

# 음료 주문칸
label2 = Label(root, text = "음료를 선택하세요")
label2.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "콜라", value = "콜라", variable = drink_var)
btn_drink1.select() # 미리 선택한 채로 시작 
btn_drink2 = Radiobutton(root, text = "사이다", value = "사이다", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btnCmd():
    print(burger_var.get()) # 선택된 라디오 항목의 값(value)를 출력
    print(drink_var.get()) # 음료 중 선택된 값을 출력

btn = Button(root, text = "주문하기", command = btnCmd)
btn.pack()



root.mainloop() #pygame.init() 같이 초기화해줌


