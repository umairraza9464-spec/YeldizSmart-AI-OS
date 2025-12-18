"""YeldizSmart AI - Enhanced Modern UI with Real-time Dashboard"""
from PyQt5.QtCore import QUrl, Qt, QTimer, pyqtSignal, QObject
from PyQt5.QtGui import QColor, QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QListWidgetItem, QLabel, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QProgressBar, QDockWidget
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QSize

class EnhancedMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 YeldizSmart AI OS - Lead Generation Automation")
        self.setGeometry(100, 100, 1600, 900)
        self.setStyleSheet(self._get_stylesheet())
        
        # Main container
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # ========== LEFT SIDEBAR ==========
        sidebar = self._create_sidebar()
        main_layout.addWidget(sidebar, 1)
        
        # ========== CENTER AREA ==========
        center_widget = self._create_center_area()
        main_layout.addWidget(center_widget, 5)
        
        # ========== STATUS BAR ==========
        self._create_status_bar()
        
        # Set main widget
        self.setCentralWidget(main_widget)
        
        # Real-time updates
        self._setup_real_time_updates()
    
    def _create_sidebar(self) -> QWidget:
        """Create beautiful left sidebar with navigation"""
        sidebar = QWidget()
        sidebar.setMaximumWidth(200)
        sidebar.setStyleSheet("""
            QWidget { background-color: #1e1e2e; border-right: 2px solid #00d4ff; }
            QListWidget { background-color: #1e1e2e; border: none; }
            QListWidget::item:selected { background-color: #00d4ff; color: #000; }
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Logo/Title
        title = QLabel("YeldizSmart AI")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setStyleSheet("color: #00d4ff; padding: 15px; background: #0f0f1e;")
        layout.addWidget(title)
        
        # Navigation items
        self.side_list = QListWidget()
        items = [
            "📊 Dashboard",
            "📄 Google Sheets",
            "☁️ Google Drive",
            "✉️ Gmail",
            "🎯 Mission Control",
            "⚙️ Settings",
            "📈 Analytics"
        ]
        
        for item_text in items:
            item = QListWidgetItem(item_text)
            item.setFont(QFont("Arial", 10))
            self.side_list.addItem(item)
        
        self.side_list.currentRowChanged.connect(self._on_nav_changed)
        layout.addWidget(self.side_list)
        
        # Bottom stats
        stats_box = QWidget()
        stats_layout = QVBoxLayout(stats_box)
        stats_layout.setSpacing(5)
        
        stat_labels = [
            "🔥 Leads Today: 47",
            "✅ HOT: 12",
            "⏳ WARM: 23",
            "❄️ COLD: 12"
        ]
        for stat in stat_labels:
            label = QLabel(stat)
            label.setStyleSheet("color: #00ff88; font-size: 9px; padding: 3px;")
            stats_layout.addWidget(label)
        
        layout.addWidget(stats_box)
        return sidebar
    
    def _create_center_area(self) -> QWidget:
        """Create center tabbed browser area"""
        center = QWidget()
        layout = QVBoxLayout(center)
        layout.setContentsMargins(5, 5, 5, 5)
        
        # Top toolbar
        toolbar = self._create_toolbar()
        layout.addWidget(toolbar, 0)
        
        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane { border: 1px solid #00d4ff; }
            QTabBar::tab { background: #2d2d3d; color: #fff; padding: 8px 15px; }
            QTabBar::tab:selected { background: #00d4ff; color: #000; font-weight: bold; }
        """)
        
        # Browser tab
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.tabs.addTab(self.browser, "🌐 Browser")
        
        # Mission Control tab
        mission_control = self._create_mission_control()
        self.tabs.addTab(mission_control, "🎯 Mission Control")
        
        # Stats tab
        stats_tab = self._create_stats_tab()
        self.tabs.addTab(stats_tab, "📊 Analytics")
        
        layout.addWidget(self.tabs, 1)
        return center
    
    def _create_toolbar(self) -> QWidget:
        """Create top toolbar with quick actions"""
        toolbar = QWidget()
        toolbar.setMaximumHeight(50)
        toolbar.setStyleSheet("background-color: #2d2d3d; border-bottom: 1px solid #00d4ff;")
        
        layout = QHBoxLayout(toolbar)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 5, 10, 5)
        
        # Status indicator
        status_label = QLabel("🟢 RUNNING")
        status_label.setStyleSheet("color: #00ff88; font-weight: bold; font-size: 11px;")
        layout.addWidget(status_label)
        
        # Buttons
        buttons = [("▶ Start", "#00d4ff"), ("⏸ Pause", "#ffa500"), ("⏹ Stop", "#ff4444"), ("🔄 Refresh", "#00ff88")]
        for btn_text, color in buttons:
            btn = QPushButton(btn_text)
            btn.setMaximumWidth(100)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color}; color: #000; border: none; border-radius: 5px;
                    font-weight: bold; padding: 5px;
                }}
                QPushButton:hover {{ opacity: 0.8; }}
            """)
            layout.addWidget(btn)
        
        layout.addStretch()
        
        # Time
        time_label = QLabel("04:32 AM IST")
        time_label.setStyleSheet("color: #00d4ff; font-size: 10px;")
        layout.addWidget(time_label)
        
        return toolbar
    
    def _create_mission_control(self) -> QWidget:
        """Create Mission Control dashboard"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Title
        title = QLabel("🎯 MISSION CONTROL - Live Campaign Monitoring")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setStyleSheet("color: #00d4ff; padding: 10px;")
        layout.addWidget(title)
        
        # Table
        table = QTableWidget()
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["City", "Platform", "Accounts", "Status", "Lead Count", "Success Rate"])
        table.setStyleSheet("""
            QTableWidget { background-color: #1e1e2e; color: #fff; gridline-color: #00d4ff; }
            QHeaderView::section { background-color: #00d4ff; color: #000; font-weight: bold; }
        """)
        
        # Sample data
        campaigns = [
            ["Mumbai", "FB", "3", "🟢 RUNNING", "45", "94%"],
            ["Delhi", "OLX", "2", "🟢 RUNNING", "28", "87%"],
            ["Pune", "FB+OLX", "4", "🟡 PAUSED", "12", "91%"],
            ["Bangalore", "FB", "2", "🟢 RUNNING", "33", "89%"],
        ]
        
        for row_idx, row_data in enumerate(campaigns):
            table.insertRow(row_idx)
            for col_idx, cell_text in enumerate(row_data):
                item = QTableWidgetItem(cell_text)
                item.setFont(QFont("Arial", 10))
                table.setItem(row_idx, col_idx, item)
        
        layout.addWidget(table)
        return widget
    
    def _create_stats_tab(self) -> QWidget:
        """Create analytics dashboard"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Stats cards
        stats = [
            ("📈 Total Leads", "156", "#00ff88"),
            ("🔥 HOT Leads", "47", "#ff4444"),
            ("⏳ WARM Leads", "62", "#ffa500"),
            ("❄️ COLD Leads", "47", "#00d4ff"),
        ]
        
        for stat_title, stat_value, color in stats:
            card = QWidget()
            card_layout = QVBoxLayout(card)
            card.setStyleSheet(f"background-color: #2d2d3d; border-left: 4px solid {color}; border-radius: 5px;")
            
            title = QLabel(stat_title)
            title.setStyleSheet(f"color: {color}; font-weight: bold; font-size: 12px;")
            value = QLabel(stat_value)
            value.setStyleSheet(f"color: #fff; font-size: 24px; font-weight: bold;")
            
            card_layout.addWidget(title)
            card_layout.addWidget(value)
            layout.addWidget(card)
        
        layout.addStretch()
        return widget
    
    def _create_status_bar(self):
        """Create enhanced status bar"""
        status_bar = QStatusBar()
        status_bar.setStyleSheet("background-color: #1e1e2e; color: #00ff88; border-top: 1px solid #00d4ff;")
        status_bar.showMessage("🚀 YeldizSmart AI Running | 6 FB Accounts | 6 OLX Accounts | DB: ✓ | Sync: ✓")
        self.setStatusBar(status_bar)
    
    def _get_stylesheet(self) -> str:
        """Modern dark theme stylesheet"""
        return """
            QMainWindow { background-color: #0f0f1e; }
            QLabel { color: #fff; }
            QPushButton { background-color: #00d4ff; color: #000; border: none; border-radius: 3px; padding: 5px; font-weight: bold; }
            QPushButton:hover { background-color: #00ff88; }
        """
    
    def _on_nav_changed(self, index: int):
        """Handle navigation changes"""
        urls = {
            0: "https://docs.google.com/spreadsheets/",  # Dashboard
            1: "https://docs.google.com/spreadsheets/",  # Sheets
            2: "https://drive.google.com/",              # Drive
            3: "https://mail.google.com/",               # Gmail
            4: "https://docs.google.com/spreadsheets/",  # Mission Control
            5: "https://example.com/settings",           # Settings
            6: "https://example.com/analytics",          # Analytics
        }
        if index in urls:
            self.browser.setUrl(QUrl(urls[index]))
    
    def _setup_real_time_updates(self):
        """Setup real-time update timer"""
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self._update_stats)
        self.update_timer.start(5000)  # Update every 5 seconds
    
    def _update_stats(self):
        """Update live statistics"""
        pass  # Real-time updates logic here
