from tkinter import*

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

###################################################
# 체크 박스 (체크/체크 해제 가능)

checkVariable = IntVar() # checkVariable에 int형으로 값을 저장.
checkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable = checkVariable)

# 프로그램 내에서 선택/해제 하기
checkbox.select() # 선택 함
checkbox.deselect() # 선택 해제

checkbox.pack()

# 체크박스를 만들때 var도 새로 만들어줘야 함
checkVariable2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일동안 보지 않기", variable = checkVariable2)
chkbox2.pack()






def btnCmd():
    # 프로그램 내에서 체크의 여부 확인
    print(checkVariable.get()) # 숫자 0 = 체크 x ; 숫자 1 = 체크 o 

btn = Button(root, text = "클릭", command = btnCmd)
btn.pack()



root.mainloop() #pygame.init() 같이 초기화해줌


