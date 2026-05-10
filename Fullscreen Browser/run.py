import sys
import subprocess
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QAction

class KioskBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kill_explorer()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com:5000"))
        self.browser.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.browser.customContextMenuRequested.connect(self.show_context_menu)
        self.setCentralWidget(self.browser)
        self.showFullScreen()

    def kill_explorer(self):
        try:
            subprocess.run(["taskkill", "/F", "/IM", "explorer.exe"], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
        except Exception:
            pass

    def start_explorer(self):
        try:
            subprocess.Popen(["explorer.exe"])
        except Exception:
            pass

    def show_context_menu(self, pos):
        menu = QMenu(self)
        exit_action = QAction("Close", self)
        exit_action.triggered.connect(self.close)
        menu.addAction(exit_action)
        menu.exec(self.browser.mapToGlobal(pos))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.start_explorer()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KioskBrowser()
    sys.exit(app.exec())
