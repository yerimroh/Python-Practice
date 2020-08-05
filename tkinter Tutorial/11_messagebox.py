from tkinter import*
import tkinter.messagebox as msgbox

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

################################################################################################
#  팝업창
##############################################################
# yes/no/cancel 창 + 반응 처리 해보기
def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message = "예 아니오 취소")
    # 네: 저장 후 종료
    # 아니오 : 저장 안 하고 종료
    # 취소 : 프로그램 종료 취소(현재 화면에 남아있기)
    if response == 1: # 네를 클릭함
        print("ㄴㅔ")
    elif response == 0: # 아니오를 클릭함 
        print("아니오")
    else:
        print("취소")



btn7 = Button(root, text = "yes/no/cancel 창 띄우기", command = yesnocancel).pack()




##############################################################
# yes/no 창
def yesorno():
    msgbox.askyesno("예/아니오", "재시도하시겠습니까?")

btn6 = Button(root, text = "yes/no 창 띄우기", command = yesorno).pack()

##############################################################
# retry/cancel창 띄우기
def retrycancel():
    msgbox.askretrycancel("재시도/취소", "재시도하시겠습니까?")

btn5 = Button(root, text = "retry/cancel 창 띄우기", command = retrycancel).pack()

##############################################################
# okay/cancel창 띄우기
def okcancel():
    msgbox.askokcancel("확인/취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

btn4 = Button(root, text = "okay/cancel 창 띄우기", command = okcancel).pack()

##############################################################
# 에러 메세지
def error():
    msgbox.showerror("에러", "에러가 발행하였습니다")

btn3 = Button(root, text = "경고 창 띄우기", command = error).pack()

##############################################################
# 경고 메세지
def warning():
    msgbox.showwarning("경고", "에러가 발행하였습니다")

btn2 = Button(root, text = "에러 창 띄우기", command = warning).pack()

##############################################################
# 정보 메세지
def info():
    msgbox.showinfo("알림", "에러가 발행하였습니다")

btn = Button(root, text = "정보 창 띄우기", command = info).pack()


###################################################################################################
root.mainloop() #pygame.init() 같이 초기화해줌


