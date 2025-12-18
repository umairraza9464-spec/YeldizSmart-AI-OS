from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QListWidgetItem
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YeldizSmart AI")
        self.resize(1400, 800)

        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # Side panel
        self.side_list = QListWidget()
        for name in ["Sheets", "Drive", "Gmail", "Web Store", "Mission Control"]:
            QListWidgetItem(name, self.side_list)
        self.side_list.currentRowChanged.connect(self._on_side_change)

        # Center browser
        center_widget = QWidget()
        center_layout = QVBoxLayout(center_widget)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))

        center_layout.addWidget(self.browser)

        main_layout.addWidget(self.side_list, 1)
        main_layout.addWidget(center_widget, 4)

        self.setCentralWidget(main_widget)

    def _on_side_change(self, index: int):
        urls = {
            0: "https://docs.google.com/spreadsheets/",
            1: "https://drive.google.com/",
            2: "https://mail.google.com/",
            3: "https://chromewebstore.google.com/",
            4: "https://docs.google.com/spreadsheets/"
        }
        url = urls.get(index, "https://google.com")
        self.browser.setUrl(QUrl(url))
