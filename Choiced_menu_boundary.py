from tkinter import *
from PIL import Image, ImageTk

class Choiced_menu:
    
    def __init__(self):

        self.Choiced_menu_window = Tk()
        self.Choiced_menu_window.title("메뉴 선택 화면")
        self.Choiced_menu_window.geometry("600x800+300+100")
        self.Choiced_menu_window.resizable(True, True)
        # self.scrollable_frame = self.y_scrollable_frame()        # 스크롤바 생성
        self.ShowUi()
        self.Choiced_menu_window.mainloop()


    # 프레임 세팅
    def ShowUi(self):
        self.left_frame = self.setFrame_pack(self.Choiced_menu_window, 'left', 200, 800)               # 좌측 프레임
        self.right_frame = self.setFrame_pack(self.Choiced_menu_window, 'left', 400, 800)             # 우측 프레임
        self.right_top_frame = self.setFrame_pack(self.right_frame, 'top', 400, 700)           # 우측 상단 프레임  
        self.right_bottom_frame = self.setFrame_pack(self.right_frame, 'bottom', 400, 100)    # 우측 하단 프레임

    # pcak로 생성하는 프레임
    def setFrame_pack(self, frame, pos, wid, hei):             # 프레임 생성 함수
        frame = Frame(frame, width = wid, height=hei, relief="solid", bd = 0.5, background="#C1FFD4")    #, background="#C1FFD4"
        frame.pack(side = pos)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        return frame    

    # grid로 생성하는 프레임
    def setFrame_grid(self, frame, wid, hei, row, col):
        frame = Frame(frame, width = wid, height = hei, relief="solid", bd = 0.5)   # , background="#C1FFD4"
        frame.grid(row = row, column= col, padx = 10, pady = 10)
        frame.pack_propagate(False)
        return frame
















'''



    # 세로 스크롤 가능한 프레임을 설정하는 함수 (GPT & 제미나이 사용)
    # def y_scrollable_frame(self):
        # 캔버스와 스크롤바를 담을 컨테이너 프레임을 right_top_frame 내부에 생성합니다.
        # right_top_frame은 pack으로 관리되므로, 이 컨테이너도 pack으로 배치합니다.
        canvas_scrollbar_container = Frame(self.right_top_frame)
        canvas_scrollbar_container.pack(fill="both", expand=True)
        # canvas_scrollbar_container.pack_propagate(False)

        # 캔버스 생성 (부모를 canvas_scrollbar_container로 변경)
        canvas = Canvas(canvas_scrollbar_container, bg="white")

        # 스크롤바 생성 (부모를 canvas_scrollbar_container로 변경)
        scrollbar = Scrollbar(canvas_scrollbar_container, orient="vertical", command=canvas.yview)

        # 캔버스와 스크롤바를 canvas_scrollbar_container 내에서 pack으로 배치합니다.
        # 스크롤바를 먼저 배치하여 오른쪽에 고정하고, 캔버스가 남은 공간을 채우도록 합니다.
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # 캔버스와 스크롤바 연결
        canvas.configure(yscrollcommand=scrollbar.set)

        # 스크롤 가능한 내부 프레임 (이 프레임은 캔버스에 의해 관리됩니다 - create_window)
        # 이 프레임 내에서는 grid를 자유롭게 사용할 수 있습니다.
        scrollable_frame = Frame(canvas)

        # 캔버스 안에 윈도우(scrollable_frame) 생성
        # window=scrollable_frame: 캔버스에 표시할 위젯
        # anchor='nw': 위젯의 북서쪽(north-west) 모서리가 캔버스 좌표 (0,0)에 고정되도록 합니다.
        canvas_window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

        # 스크롤 영역 설정 및 프레임 크기 조절 시 캔버스 너비 조정
        def on_frame_configure(event):
            # 스크롤 영역을 scrollable_frame의 전체 크기로 설정합니다.
            canvas.configure(scrollregion=canvas.bbox("all"))
            # 캔버스 너비를 스크롤 가능한 프레임의 너비와 일치시키기
            # 이렇게 하면 스크롤 가능한 프레임이 캔버스 너비에 맞춰지고 가로 스크롤바가 생기지 않습니다.
            canvas.itemconfig(canvas_window_id, width=canvas.winfo_width())

        # scrollable_frame의 크기가 변경될 때마다 on_frame_configure 함수를 호출합니다.
        scrollable_frame.bind("<Configure>", on_frame_configure)
        # 캔버스 크기가 변경될 때도 on_frame_configure를 호출하여 scrollable_frame의 너비를 조정합니다.
        canvas.bind("<Configure>", on_frame_configure)

        # 마우스 휠 스크롤 기능 추가 (전역 바인딩)
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # setMenu에서 사용할 수 있도록 scrollable_frame을 반환합니다.
        return scrollable_frame
'''
if __name__ == "__main__":
    mainui = Choiced_menu()


