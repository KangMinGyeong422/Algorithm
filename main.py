import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from TitleScreen import TitleScreen

try:
    from PyQt5.QtWidgets import QApplication, QLabel
except ImportError:
    print("PyQt5가 설치되어 있지 않습니다. 설치 중...")
    # PyQt5를 설치하는 코드
    subprocess.call(["pip", "install", "PyQt5"])
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = TitleScreen()
    myApp.show()

    # 종료
    app.setQuitOnLastWindowClosed(True)
    sys.exit(app.exec_())
