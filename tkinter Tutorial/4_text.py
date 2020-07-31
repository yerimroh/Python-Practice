from tkinter import*

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

################################################
# 일반 텍스트 (빈 텍스트 상자) / 긴 글 용
txt = Text(root, width = 30, height = 5)
txt.pack()

# 사전에 글자가 새겨진(기본값) 텍스트 상자
txt2 = Text(root, width = 30, height = 5)
txt2.insert(END, "글자를 입력하세요")
txt2.pack()

################################################
# 일반 엔트리(단답용 작은 텍스트 상자/한줄만 쓸수있음)
entry = Entry(root, width = 30)
entry.pack()

# 사전에 글자가 새겨진(기본값) 엔트리 상자
entry2 = Entry(root, width = 30)
entry2.insert(END, "글자를 입력하세요")
entry2.pack()

##################################################
# 텍스트 상자/엔트리 속 글자 가져오기
def getText():
    # 텍스트 상자 속 글 가져오기
    print(txt.get("1.0", END)) # 1: 1번째 줄, 0: 0번째 column(index)

    # 텍스트 상자 속 글 지우기 
    txt.delete("1.0", END)

    # 엔트리 상자 속 글 가져오기
    print(entry.get())

    # 엔트리 상자 속 글 지우기
    entry.delete(0, END)

btn = Button(root, text = "가져오기", command = getText)
btn.pack()




root.mainloop() #pygame.init() 같이 초기화해줌


