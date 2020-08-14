# title: 제목 없음 - Windows 메모장
# 메뉴: 파일, 편집, 서식, 보기, 도움말
# 메뉴 구현: 파일 메뉴 내에서 열기/저장/끝내기 3개 처리
# 열기 - mynote.txt. 열어서 보여주기
# 저장 - mynote.txt 파일에 현재 내용 저장하기
# 끝내기 - 프로그램 종료
# 프로그램 시작 시 본문은 비어있는 상태
# 프로그램 크기조정 가능해야 함
# 우측에 스크롤 바 넣기


from tkinter import*
import os

root = Tk()
root.title("메모장")
root.geometry("640x480")

###################################################
# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")

# 텍스트 박스
txtBox = Text(root, width = 30, height = 20, yscrollcommand = scrollbar.set)
txtBox.pack(side = "left", fill = "both", expand = True) 

scrollbar.config(command = txtBox.yview)

####################################################
# method들

def openFile():
    if os.path.isfile("mynote.txt"): # 파일이 있으면 True, 없으면 False
        with open("mynote.txt", "r", encoding = "utf8") as file:
            txtBox.delete("1.0", END) # 불러오기 전에 띄워진 내용들 지움
            txtBox.insert(END, file.read()) # 읽어온 파일 띄움

def saveFile():
    with open("mynote.txt", "w", encoding = "utf8") as file:
        file.write(txtBox.get("1.0", END)) # 모든 내용을 가져와서 저장

####################################################
# 메뉴 
menu = Menu(root) #메뉴

# 파일 메뉴
menuFile = Menu(menu, tearoff = 0)
menuFile.add_command(label = "열기", command = openFile) #열기 
menuFile.add_command(label = "저장", command = saveFile) #저장
menuFile.add_command(label = "끝내기", command = root.quit) #끝내기
menu.add_cascade(label = "파일", menu = menuFile) # 파일메뉴 더해주기

# 편집 메뉴
editMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = "편집", menu = editMenu) # 파일메뉴 더해주기

# 서식 메뉴
formatMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = "서식", menu = formatMenu) # 서식메뉴 더해주기

# 보기 메뉴
viewMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = "보기", menu = viewMenu) # 서식메뉴 더해주기

# 도움말 메뉴
helpMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = "도움말", menu = helpMenu) # 서식메뉴 더해주기

root.config(menu = menu)


####################################################

root.mainloop()