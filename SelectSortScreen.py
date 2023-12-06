from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import subprocess

### 선택 정렬

class SelectSortScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('선택 정렬')
        self.resize(1280, 720)

        # label
        label = QLabel('입력할 값 입력', self)
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)

        # 데이터 입력
        self.inputLabel = QLabel('배열 크기 입력(공백을 포함한 숫자 이외의 문자 입력시 오류 발생 주의): ', self)
        self.inputBox = QLineEdit(self)

        inputFont = self.inputLabel.font()
        inputFont.setPointSize(20)
        self.inputLabel.setFont(inputFont)

        inputBoxFont = self.inputBox.font()
        inputBoxFont.setPointSize(20)
        self.inputBox.setFont(inputBoxFont)

        self.valueLabel = QLabel('배열 값 입력(공백(스페이스 바)으로 구분): ', self)
        self.valueBox = QLineEdit(self)

        valueLabelFont = self.valueLabel.font()
        valueLabelFont.setPointSize(20)
        self.valueLabel.setFont(valueLabelFont)

        valueBoxFont = self.valueBox.font()
        valueBoxFont.setPointSize(20)
        self.valueBox.setFont(valueBoxFont)

        # 정렬 버튼
        self.sortBtn = QPushButton('정렬', self)
        self.sortBtn.clicked.connect(self.sortData)

        self.sortBtn.setFixedHeight(30)

        # 스크롤 영역 생성
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # 결과 출력 라벨을 스크롤 영역에 배치
        self.resultLabel = QLabel('출력', self)
        self.resultLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        resultLabelFont = self.resultLabel.font()
        resultLabelFont.setPointSize(20)
        self.resultLabel.setFont(resultLabelFont)

        scroll_area.setWidget(self.resultLabel)

        # 스크롤 영역의 높이를 400으로 설정
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
        main_vbox.addWidget(self.inputLabel)
        main_vbox.addWidget(self.inputBox)
        main_vbox.addWidget(self.valueLabel)
        main_vbox.addWidget(self.valueBox)

        main_vbox.addLayout(hbox)
        main_vbox.addWidget(self.sortBtn)
        main_vbox.addStretch(1)
        main_vbox.addWidget(scroll_area)
        main_vbox.addStretch(1)
        main_vbox.addWidget(backBtn, alignment=Qt.AlignRight)

    def show_startScreen(self):
        from StartScreen import StartScreen
        self.start_screen = StartScreen()
        self.start_screen.show()
        self.hide()

    def sortData(self):
        arraySize = self.inputBox.text()
        arrayValue = self.valueBox.text()

        if not arraySize.isdigit() or not arrayValue:
            self.resultLabel.setText('잘못된 입력')
            return

        arraySize = int(arraySize)
        arrayValue = [int(x) for x in arrayValue.split()]

        # python에서 C코드 호출
        result = self.runCSelectionSort(arraySize, arrayValue)

        # 결과 표시
        self.resultLabel.setText(f'{result}')

    def runCSelectionSort(self, arraySize, arrayValue):
        # C코드 실행 결과
        command = ['SelectSort.exe']
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        proc.stdin.write(str(arraySize) + '\n')  # 배열 크기를 C 코드로 전달
        for value in arrayValue:
            proc.stdin.write(str(value) + '\n')  # 배열 값들을 C 코드로 전달

        # C 코드가 종료할 때까지 대기하고 결과를 반환
        stdout, stderr = proc.communicate()
        return stdout


if __name__ == "__main__":
    app = QApplication([])
    window = SelectSortScreen()
    window.show()
    app.exec_()
