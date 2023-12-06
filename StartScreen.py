import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

### 시작 
class StartScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('알고리즘 선택')
        self.resize(1280, 760)
        
        # 시작 화면에 텍스트 추가
        label = QLabel('실행할 알고리즘을 선택해 주세요.\n', self)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        
        ## 알고리즘 텍스트와 버튼
        sortLabel = QLabel('정렬 알고리즘', self)
        selectFont = sortLabel.font()
        selectFont.setPointSize(20)
        sortLabel.setFont(selectFont)
        
        selectSortBtn = QPushButton('선택정렬', self)
        selectSortBtn.setFixedHeight(30)
        selectSortBtn.clicked.connect(self.show_SelectSortScreen)
        
        bubbleSortBtn = QPushButton('버블정렬', self)
        bubbleSortBtn.setFixedHeight(30)
        bubbleSortBtn.clicked.connect(self.show_BubbleSortScreen)
        
        quickSortBtn = QPushButton('퀵정렬', self)
        quickSortBtn.setFixedHeight(30)
        quickSortBtn.clicked.connect(self.show_QuickSortScreen)
        
        insertSortBtn = QPushButton('삽입정렬', self)
        insertSortBtn.setFixedHeight(30)
        insertSortBtn.clicked.connect(self.show_InsertSortScreen)
        
        mergeSortBtn = QPushButton('병합정렬', self)
        mergeSortBtn.setFixedHeight(30)
        mergeSortBtn.clicked.connect(self.show_MergeSortScreen)
        
        radixSortBtn = QPushButton('기수정렬', self)
        radixSortBtn.setFixedHeight(30)
        radixSortBtn.clicked.connect(self.show_RadixSortScreen)

        graphLabel = QLabel('그래프')
        gselectFont = graphLabel.font()
        gselectFont.setPointSize(20)
        graphLabel.setFont(gselectFont)
        
        DFSBtn = QPushButton('DFS')
        DFSBtn.setFixedHeight(30)
        DFSBtn.clicked.connect(self.show_DFS_Screen)
        
        BFSBtn = QPushButton('BFS')
        BFSBtn.setFixedHeight(30)
        BFSBtn.clicked.connect(self.show_BFS_Screen)
        
        dijkstraBtn = QPushButton('다익스트라')
        dijkstraBtn.setFixedHeight(30)
        dijkstraBtn.clicked.connect(self.show_DijkstraScreen)
        
        floyedBtn = QPushButton('플로이드')
        floyedBtn.setFixedHeight(30)
        floyedBtn.clicked.connect(self.show_FloyedScreen)
        
        # 시작 화면에 종료 버튼 추가
        backBtn = QPushButton('돌아가기', self)
        backBtn.setFixedSize(150, 50)
        backBtn.clicked.connect(self.Show_TitleScreen)

        # 레이아웃 설정
        hbox1 = QVBoxLayout()
        hbox2 = QVBoxLayout()
        
        hbox1.addWidget(sortLabel)
        hbox1.addWidget(selectSortBtn)
        hbox1.addWidget(bubbleSortBtn)
        hbox1.addWidget(quickSortBtn)
        hbox1.addWidget(insertSortBtn)
        hbox1.addWidget(mergeSortBtn)
        hbox1.addWidget(radixSortBtn)
        
        hbox2.addWidget(graphLabel)
        hbox2.addWidget(DFSBtn)
        hbox2.addWidget(BFSBtn)
        hbox2.addWidget(dijkstraBtn)
        hbox2.addWidget(floyedBtn)

        vbox = QVBoxLayout(self)
        vbox.addWidget(label)
        
        hbox = QHBoxLayout()
        hbox.addLayout(hbox1)
        hbox.addSpacing(30)  # 30 픽셀의 간격을 줍니다.
        hbox.addLayout(hbox2)
        
        vbox.addLayout(hbox)
        vbox.addStretch(2)
        vbox.addWidget(backBtn, alignment=Qt.AlignRight)
           
    def Show_TitleScreen(self):
        from TitleScreen import TitleScreen
        self.title_screen = TitleScreen()
        self.title_screen.show()
        self.hide()
    
    def show_SelectSortScreen(self):
        from SelectSortScreen import SelectSortScreen
        self.selectSort_screen = SelectSortScreen()
        self.selectSort_screen.show()
        self.hide()
        
    def show_BubbleSortScreen(self):
        from BubbleSortScreen import BubbleSortScreen
        self.bubbleSort_screen = BubbleSortScreen()
        self.bubbleSort_screen.show()
        self.hide()
    
    def show_QuickSortScreen(self):
        from QuickSortScreen import QuickSortScreen
        self.QuickSort_Screen = QuickSortScreen()
        self.QuickSort_Screen.show()
        self.hide()
        
    def show_InsertSortScreen(self):
        from InsertionSortScreen import InsertionSortScreen
        self.InsertionSortScreen = InsertionSortScreen()
        self.InsertionSortScreen.show()
        self.hide()
        
    def show_MergeSortScreen(self):
        from MergeSortScreen import MergeSortScreen
        self.MergeSortScreen = MergeSortScreen()
        self.MergeSortScreen.show()
        self.hide()
        
    def show_RadixSortScreen(self):
        from RadixSortScreen import RadixSortScreen
        self.RadixSortScreen = RadixSortScreen()
        self.RadixSortScreen.show()
        self.hide()
        
    def show_DFS_Screen(self):
        from DFS_Screen import DFS_Screen
        self.DFS_Screen = DFS_Screen()
        self.DFS_Screen.show()
        self.hide()
        
    def show_BFS_Screen(self):
        from BFS_Screen import BFS_Screen
        self.BFS_Screen = BFS_Screen()
        self.BFS_Screen.show()
        self.hide()
        
    def show_DijkstraScreen(self):
        from DijkstraScreen import DijkstraScreen
        self.DijkstraScreen = DijkstraScreen()
        self.DijkstraScreen.show()
        self.hide()
        
    def show_FloyedScreen(self):
        from FloyedScreen import FloyedScreen
        self.FloyedScreen = FloyedScreen()
        self.FloyedScreen.show()
        self.hide()
    
    def close_StartScreen(self):
        self.close()        
