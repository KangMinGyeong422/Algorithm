import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from TitleScreen import TitleScreen

### 참고 자료
class RefScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('참고')
        self.resize(1280, 760)
        
        describe = "이지영, 『C로 배우는 쉬운 자료구조』, 한빛아카데미(2021)\n\nDardao, 『PyQt5 Tutorial - 파이썬으로 만드는 나만의 GUI 프로그램』, 유페이퍼(2020)\n\nTwoIceFish, Cyber-Luna, [정보] 파이썬 subprocess 설명 및 예제, https://twoicefish-secu.tistory.com/509"
        
        # 참고 화면 텍스트 추가
        label = QLabel(describe)
        font = label.font()
        font.setPointSize(15)
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        
        # 돌아가기 버튼
        backBtn = QPushButton('돌아가기', self)
        backBtn.setFixedSize(150, 50)
        backBtn.clicked.connect(self.show_titleScreen)
        
        # 레이아웃 설정
        vbox = QVBoxLayout(self)
        vbox.addWidget(label, alignment=Qt.AlignCenter)
        vbox.addWidget(backBtn, alignment=Qt.AlignRight)
        
    def close_RefScreen(self):
        self.close()
    
    def show_titleScreen(self):
        from TitleScreen import TitleScreen
        self.title_screen = TitleScreen()
        self.title_screen.show()
        self.hide()