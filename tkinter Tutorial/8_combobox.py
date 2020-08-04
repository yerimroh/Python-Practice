from tkinter import*
import tkinter.ttk as ttk # 콤보박스는 따로 임포트 해줘야함

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

###################################################
# 여러개의 옵션 중에 하나를 선택할 수 있는 라디오버튼 위젯

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31까지의 숫자 반환
combobox = ttk.Combobox(root, height = 5, values = values, state="readonly")
combobox.pack()
combobox.set("카드 결제일") # 사전에 미리 글귀 넣어놓고 시작 가능


def btnCmd():
    print(combobox.get()) # 선택된 값 표시

btn = Button(root, text = "선택하기", command = btnCmd)
btn.pack()



root.mainloop() #pygame.init() 같이 초기화해줌


