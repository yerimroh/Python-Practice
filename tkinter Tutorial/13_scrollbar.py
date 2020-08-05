from tkinter import*


root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

#######################################################################
# 스크롤 바


# 위젯과 스크롤 바를 같은 프레임에다 넣어서 관리하면 편하기 땜에 프레임 생성해줌
frame = Frame(root)
frame.pack()

# 스크롤 바
scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill = "y") # 오른쪽에다 정렬

# 위젯(리스트박스)/ set이 없으면 스크롤바를 내려도 다시 올라감
listbox = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand = scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side = "left")


scrollbar.config(command = listbox.yview) # 스크롤바도 리스트박스의 현 상황을 보게 만듬


###################################################################################################
root.mainloop() #pygame.init() 같이 초기화해줌


