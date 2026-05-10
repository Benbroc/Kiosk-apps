import sys
import subprocess
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView

class KioskBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kill_explorer()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        
        self.setCentralWidget(self.browser)
        
        self.showFullScreen()

    def kill_explorer(self):
        try:
            subprocess.run(["taskkill", "/F", "/IM", "explorer.exe"], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Fehler beim Beenden des Explorers: {e}")

    def start_explorer(self):
        try:
            subprocess.Popen(["explorer.exe"])
        except Exception as e:
            print(f"Fehler beim Starten des Explorers: {e}")

    def keyPressEvent(self, event):
        if event.key() == 0x01000000:
            self.close()

    def closeEvent(self, event):
        self.start_explorer()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KioskBrowser()
    sys.exit(app.exec())
