from tkinter import*

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정

# 기본 레이블
label1 = Label(root, text = "안녕하세요")
label1.pack() # 클릭해도 뭐 없음

# 레이블에 이미지 넣기
photo = PhotoImage(file = "tkinter Tutorial\\button background.png")
label2 = Label(root, image = photo)
label2.pack()

# 버튼을 눌렀을 때 글자 레이블을 바꾸기
def change():
    label1.config(text = "반가워요")

btn = Button(root, text = "글자 바꾸기", command = change)
btn.pack()

# 버튼을 눌렀을 때 이미지 레이블을 바꾸기
def imgChange():
    global photo2
    photo2 = PhotoImage(file = "tkinter Tutorial\\button background2.png")
    label2.config(image = photo2)

btn4 = Button(root, text = "이미지 바꾸기", command = imgChange)
btn4.pack()

root.mainloop() #pygame.init() 같이 초기화해줌


