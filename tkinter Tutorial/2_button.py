from tkinter import*

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정

# 기본 버튼
btn1 = Button(root, text="버튼")
btn1.pack()

# 크기를 지정한 버튼(글자크기는 똑같음)
btn2 = Button(root, padx = 10, pady = 5, text="버튼333333333332")
btn2.pack()

# 여백 조정
btn3 = Button(root, width = 10, height = 5, text = "버튼333333333333")
btn3.pack()

# 버튼 색상 지정
btn4 = Button(root, fg = "cornsilk4", bg = "yellow", text="버튼4")
# fg는 글자 색, bg는 배경 색
btn4.pack()

# 이미지를 사용해서 버튼 생성
btnImage = PhotoImage(file = "tkinter Tutorial\\button background.png")
btn5 = Button(root, image = btnImage)
btn5.pack()


# 버튼에 동작 넣기

def btnCmd():
    print("클릭!")

btn6 = Button(root, text = "동작하는 버튼", command = btnCmd)
btn6.pack()


root.mainloop() #pygame.init() 같이 초기화해줌


