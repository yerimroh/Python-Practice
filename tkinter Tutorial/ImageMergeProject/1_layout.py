from tkinter import*
import tkinter.ttk as ttk # 콤보박스를 사용하기 위해

root = Tk()
root.title("이미지 합치기") # 제목 설정
root.geometry("640x480+300+200") # 크기 설정 

###########################################################################
# 파일 프레임 (파일추가/선택삭제)
fileFrame = Frame(root) # 프레임
fileFrame.pack()

addFileBtn = Button(fileFrame, text = "파일추가", padx = 5, pady = 5)
addFileBtn.pack(side = "left")

deleteFileBtn = Button(fileFrame, text = "선택삭제", padx = 5, pady = 5)
deleteFileBtn.pack(side = "right")

###########################################################################
# 리스트 프레임
listFrame = Frame(root) # 프레임
listFrame.pack(fill = "both")

scrollbar = Scrollbar(listFrame) # 스크롤바
scrollbar.pack(side = "right", fill = "y") # "fill = y 해줘야 위아래로 길게 보임"

# 파일목록
fileList = Listbox(listFrame, selectmode = "extended", height = 15, yscrollcommand = scrollbar.set) # 여러개 선택가능/ 한번에 15개 보임
fileList.pack(side = "left", fill = "both", expand = True) #화면에 맞게 크기 조정

scrollbar.config(command = fileList.yview)

#####################################################################
# 저장경로 프레임
pathFrame = LabelFrame(root, text = "저장 경로")
pathFrame.pack(fill = "x")

txtPath = Entry(pathFrame) 
txtPath.pack(side = "left", fill = "x", expand = True, ipady = 3) # i pad는 이너 패딩..

# 버튼들
pathSearchBtn = Button(pathFrame, text = "찾아보기", padx = 5, pady = 5)
pathSearchBtn.pack(side = "right")



#####################################################################
# 옵션 프레임
optionFrame = LabelFrame(root, text = "옵션")
optionFrame.pack()

# 1. 가로 넓이 옵션
# 가로넓이 레이블
widthLabel = Label(optionFrame, text = "가로넓이", width = 8)
widthLabel.pack(side = "left")

# 가로넓이 콤보박스
widthOption = ["원본유지", "1024", "80", "640"] #옵션 리스트
widthCombobox = ttk.Combobox(optionFrame, state = "readonly", values = widthOption, width = 10)
widthCombobox.current(0)
widthCombobox.pack(side = "left")

# 2. 간격 옵션
# 간격옵션 레이블
spaceLabel = Label(optionFrame, text = "간격옵션", width = 8)
spaceLabel.pack(side = "left")

# 간격옵션 콤보박스
spaceOption = ["없음", "좁게", "보통", "넓게"] #옵션 리스트
spaceCombobox = ttk.Combobox(optionFrame, state = "readonly", values = spaceOption, width = 10)
spaceCombobox.current(0)
spaceCombobox.pack(side = "left")

# 3. 파일 포맷 옵션


####################################################################

root.resizable(False, False) # 창 크기 변경 불허
root.mainloop() #pygame.init() 같이 초기화해줌
