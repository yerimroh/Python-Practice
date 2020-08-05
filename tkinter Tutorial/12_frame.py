from tkinter import*


root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

#######################################################################

label = Label(root, text = "메뉴를 선택해 주세요.").pack(side = "top")

btn = Button(root, text = "주문하기").pack(side = "bottom")

################################################################################################
# 가본 프레임

# 햄버거 메뉴판 예시
frame_burger = Frame(root, relief = "solid", bd = 1)
frame_burger.pack(side = "left", fill = "both", expand = True)

Button(frame_burger, text = "햄버거").pack()
Button(frame_burger, text = "치즈버거").pack()
Button(frame_burger, text = "불고기버거").pack()


##################################################################
# 제목이 있는 레이블 프레임

# 음료 메뉴판 예시
frame_drink = LabelFrame(root, text = "음료")
frame_drink.pack(side = "left", fill = "both", expand = True)

Button(frame_drink, text = "콜라").pack()
Button(frame_drink, text = "사이다").pack()
Button(frame_drink, text = "맥주").pack()


###################################################################################################
root.mainloop() #pygame.init() 같이 초기화해줌


