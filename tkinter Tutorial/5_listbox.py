from tkinter import*

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

####################################################
# 리스트 박스
listbox = Listbox(root, selectmode = "extended", height = 0)
listbox.insert(0, "사과")
listbox.insert(0, "딸기")
listbox.insert(0, "바나나")
listbox.insert(END, "포도")
listbox.insert(END, "수박") # element들 넣어주기
listbox.pack()


def btnCmd():
    # 삭제
    # listbox.delete(0) # n번째 element를 삭제함

    # 갯수 확인
    # print("리스트에는, {0} 개의 element들이 있습니다.".format(listbox.size()))

    # 항목 확인
    # print("1번째부터 3번째까지의 element들: ", listbox.get(0, 2))

    # 선택 element 확인 
    # print("선택된 항목: {0}".format(listbox.curselection()))

btn = Button(root, text = "클릭", command = btnCmd)
btn.pack()



root.mainloop() #pygame.init() 같이 초기화해줌


