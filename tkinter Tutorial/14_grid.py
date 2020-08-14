from tkinter import*


root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

#######################################################################
# 그리드

# # 그리드 기본
# # 정렬해볼 element들
# btn1 = Button(root, text = "버튼 1")
# btn2 = Button(root, text = "버튼 2")

# #그리드에 지정해주기
# btn1.grid(row = 0, column = 0)
# btn2.grid(row = 1, column = 1)

########################################################################
# 실전연습(키보드 일부 레이아웃 흉내내 보기)

# 첫번째줄
btnf16 = Button(root, text = "F16", padx = 10, pady = 10) 
btnf17 = Button(root, text = "F17", padx = 10, pady = 10) 
btnf18 = Button(root, text = "F18", padx = 10, pady = 10) 
btnf19 = Button(root, text = "F19", padx = 10, pady = 10) 

btnf16.grid(row = 0, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btnf17.grid(row = 0, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btnf18.grid(row = 0, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btnf19.grid(row = 0, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

# 두번째줄
btnClear = Button(root, text = "clear", padx = 10, pady = 10) 
btnEqual = Button(root, text = "=", padx = 10, pady = 10) 
btnDivide = Button(root, text = "/", padx = 10, pady = 10) 
btnMultiply = Button(root, text = "*", padx = 10, pady = 10) 

btnClear.grid(row = 1, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btnEqual.grid(row = 1, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btnDivide.grid(row = 1, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btnMultiply.grid(row = 1, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

# 세번째줄
btn7 = Button(root, text = "7", padx = 10, pady = 10) 
btn8 = Button(root, text = "8", padx = 10, pady = 10) 
btn9 = Button(root, text = "9", padx = 10, pady = 10) 
btnSubtract = Button(root, text = "-", padx = 10, pady = 10) 

btn7.grid(row = 2, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn8.grid(row = 2, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn9.grid(row = 2, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btnSubtract.grid(row = 2, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

# 네번째줄 
btn4 = Button(root, text = "4", padx = 10, pady = 10) 
btn5 = Button(root, text = "5", padx = 10, pady = 10) 
btn6 = Button(root, text = "6", padx = 10, pady = 10) 
btnAddition = Button(root, text = "+", padx = 10, pady = 10) 

btn4.grid(row = 3, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn5.grid(row = 3, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn6.grid(row = 3, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btnAddition.grid(row = 3, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

# 다섯번째줄
btn1 = Button(root, text = "1", padx = 10, pady = 10) 
btn2 = Button(root, text = "2", padx = 10, pady = 10) 
btn3 = Button(root, text = "3", padx = 10, pady = 10) 
btnEnter = Button(root, text = "Enter", padx = 10, pady = 10)  # 위아래로 긴 버튼!!

btn1.grid(row = 4, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn2.grid(row = 4, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn3.grid(row = 4, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btnEnter.grid(row = 4, column = 3, rowspan = 2, sticky = N+E+W+S, padx = 3, pady = 3) # 현재 위치로부터 아래쪽으로 몇 줄을 더 더함

# 여섯번째줄
btn0 = Button(root, text = "0", padx = 10, pady = 10)
btnPeriod = Button(root, text = ".", padx = 10, pady = 10)

btn0.grid(row = 5, column = 0, columnspan = 2, sticky = N+E+W+S, padx = 3, pady = 3) # 현재 위치로부터 오른쪽으로 2칸 더함
btnPeriod.grid(row = 5, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)

###################################################################################################
root.mainloop() #pygame.init() 같이 초기화해줌


