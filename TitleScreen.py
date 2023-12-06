import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

### 타이틀
class TitleScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('알고리즘')
        self.resize(1280, 720)
        

        # 화면 설정
        title = QLabel('알고리즘 프로젝트', self)
        font1 = title.font()
        font1.setPointSize(100)
        font1.setBold(True)
        title.setFont(font1)
        
        descriptionTitle = QLabel('알고리즘을 실행하고 그 과정과 결과를 출력합니다.', self)
        font2 = descriptionTitle.font()
        font2.setPointSize(40)
        descriptionTitle.setFont(font2)

        # 버튼 폰트
        btnfont = QFont()
        btnfont.setPointSize(30)
        
        startBtn = QPushButton('시작', self)
        startBtn.setFixedHeight(100)
        startBtn.setFont(btnfont)
        startBtn.clicked.connect(self.show_startScreen)
        
        referenceBtn = QPushButton('참고 자료', self)
        referenceBtn.setFixedHeight(100)
        referenceBtn.setFont(btnfont)
        referenceBtn.clicked.connect(self.show_refScreen)
        
        quitBtn = QPushButton('종료', self)
        quitBtn.setFixedHeight(100)
        quitBtn.setFont(btnfont)
        quitBtn.clicked.connect(self.close)        

        # 화면 레이아웃
        vbox = QVBoxLayout(self)
        
        vbox.addStretch(1)
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(descriptionTitle, alignment=Qt.AlignCenter)
        vbox.addStretch(1)
        
        hbox = QHBoxLayout()
        hbox.addWidget(startBtn)
        hbox.addWidget(referenceBtn)
        hbox.addWidget(quitBtn)
  
        vbox.addLayout(hbox)
        
    def show_startScreen(self):
        from StartScreen import StartScreen
        self.start_screen = StartScreen()
        self.start_screen.show()
        self.hide() # 타이틀 화면 숨기기
    
    def show_refScreen(self):
        from RefScreen import RefScreen
        self.ref_screen = RefScreen()
        self.ref_screen.show()
        self.hide()
