import sys
from Window import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    sys.exit(app.exec_())
