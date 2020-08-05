from tkinter import*

root = Tk() # 메인 창
root.title("Nado GUI") # 제목 설정
root.geometry("640x480") # 화면 크기

###################################################
# 상단의 메뉴 바
menu = Menu(root)


# File 메뉴 (기본적인 메뉴)
def create_new_file():
    print("새 문서를 만듭니다.")

menuFile = Menu(menu, tearoff = 0)
menuFile.add_command(label = "New File", command = create_new_file) #New File옵션
menuFile.add_command(label = "New Window") # New Window 옵션
menuFile.add_separator() # 구분선 
menuFile.add_command(label = "Open File") # Open File 옵션
menuFile.add_command(label = "Save All", state = "disable") # Save All 옵션(disabled)
menuFile.add_separator() # 구분선 
menuFile.add_command(label = "Quit", command = root.quit) # Quit 옵션/누르면 프로그램 종료

menu.add_cascade(label = "File", menu = menuFile) # menu바에다가 menu_file(파일)이 들어가는거

root.config(menu = menu)

#######################################################
# Language 메뉴 (라디오 버튼 사용)
menuLang = Menu(menu, tearoff = 0)
menuLang.add_radiobutton(label = "Python")
menuLang.add_radiobutton(label = "Java")
menuLang.add_radiobutton(label = "C++")

menu.add_cascade(label="Language", menu = menuLang) # 메뉴 바에다가 Language 메뉴 추가


#######################################################
# View 메뉴(체크박스 사용)
menu_view = Menu(menu, tearoff = 0)
menu_view.add_checkbutton(label = "Show Minimap")
menu.add_cascade(label = "View", menu = menu_view) # 메뉴 바에다가 View 메뉴 추가




root.mainloop() #pygame.init() 같이 초기화해줌


