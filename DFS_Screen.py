import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import subprocess

### DFS

class DFS_Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('DFS')
        self.resize(1280, 720)
        
        # label
        label = QLabel('그래프 DFS 알고리즘', self)
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        
        des = QLabel('\n그래프는 입력이 복잡할 것 같아 교재에 등장하는 G9 그래프를 입력했습니다.')
        des.setAlignment(Qt.AlignLeft)
        desFont = des.font()
        desFont.setPointSize(20)
        des.setFont(desFont)
        
        # 출력 영역 스크롤 생성
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        
        # 결과 출력 라벨을 스크롤 영역에 배치
        self.resultLabel = QLabel('출력', self)
        self.resultLabel.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        resultLabelFont = self.resultLabel.font()
        resultLabelFont.setPointSize(20)
        self.resultLabel.setFont(resultLabelFont)
        
        result = self.runDFS()
        
        # 결과 표시
        self.resultLabel.setText(f'{result}')
        
        scroll_area.setWidget(self.resultLabel)
        
        # 스크롤 영역 높이 설정
        scroll_area.setFixedHeight(400)
        
        # 돌아가기 버튼
        backBtn = QPushButton('돌아가기', self)
        backBtn.setFixedSize(150, 50)
        backBtn.clicked.connect(self.show_startScreen)
        
        # 레이아웃 설정
        main_vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()
        
        hbox.setAlignment(Qt.AlignCenter)
        
        main_vbox.addStretch(1)
        main_vbox.addWidget(label)
        main_vbox.addWidget(des)
        
        main_vbox.addLayout(hbox)
        main_vbox.addStretch(1)
        main_vbox.addWidget(scroll_area)
        main_vbox.addStretch(1)
        main_vbox.addWidget(backBtn, alignment=Qt.AlignRight)
        
    def show_startScreen(self):
        from StartScreen import StartScreen
        self.start_screen = StartScreen()
        self.start_screen.show()
        self.hide()    
        
    def runDFS(self):
        # C 코드 실행 결과
        command = ['DFS.exe']
        proc = QProcess(self)
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # C 코드가 종료할 때까지 대기하고 결과를 반환
        stdout, stderr = proc.communicate()
        return stdout        