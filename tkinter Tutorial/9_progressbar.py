from tkinter import*
import tkinter.ttk as ttk # 콤보박스는 따로 임포트 해줘야함
import time

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

###################################################
# 프로그레스 바(현재 상황/전체 상황)

# # 첫번째 프로그레스 바 (mode = indeterminate인 경우)
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")
# progressbar.start(10) # 10ms마다 움직임
# progressbar.pack()

# # 두번째 프로그레스 바 (mode = determinate인 경우)
# progressbar2 = ttk.Progressbar(root, maximum = 100, mode = "determinate")
# progressbar2.start(10) # 10ms마다 움직임
# progressbar2.pack()

# 세번째 프로그레스 바 (length의 사용)
p_var3 = DoubleVar() # 소수도 사용하기 위해 DoubleVar() 씀
progressbar3 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var3)
progressbar3.pack()

# 프로그레스 
def btnCmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var3.set(i) # 프로그레스바의 값 업데이트
        progressbar3.update() # ui 업데이트


btn = Button(root, text = "시작", command = btnCmd2)
btn.pack()

# 프로그레스 바 중단 버튼
def btnCmd():
    progressbar3.stop() # 프로그레스 바 작동 중지

btn = Button(root, text = "중단", command = btnCmd)
btn.pack()



root.mainloop() #pygame.init() 같이 초기화해줌


