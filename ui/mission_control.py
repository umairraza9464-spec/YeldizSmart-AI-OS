from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class MissionControlWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(
            ["Campaign", "City", "Platform", "Status", "Lead Count"]
        )
        layout.addWidget(self.table)

    def update_campaigns(self, campaigns):
        self.table.setRowCount(len(campaigns))
        for row, c in enumerate(campaigns):
            self.table.setItem(row, 0, QTableWidgetItem(c.get("campaign", "")))
            self.table.setItem(row, 1, QTableWidgetItem(c.get("city", "")))
            self.table.setItem(row, 2, QTableWidgetItem(c.get("platform", "")))
            self.table.setItem(row, 3, QTableWidgetItem(c.get("status", "")))
            self.table.setItem(row, 4, QTableWidgetItem(str(c.get("lead_count", 0))))
