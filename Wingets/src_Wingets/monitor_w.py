from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
import psutil
import os

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JBS Workflow Monitor")
        self.setGeometry(100, 100, 320, 160)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.offset = None

        self.setStyleSheet("""
            QWidget {
                background: transparent;
            }
            QLabel {
                color: white;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
            }
        """)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(16, 16, 16, 16)

        def get_icon_path(filename):
            return os.path.abspath(os.path.join(os.path.dirname(__file__), "icons", filename))

        self.cpu_layout, self.cpu_value = self.create_info_line(get_icon_path("cpu_icon.png"))
        self.ram_layout, self.ram_value = self.create_info_line(get_icon_path("ram_icon.png"))
        self.disk_layout, self.disk_value = self.create_info_line(get_icon_path("disk_icon.png"))


        self.layout.addLayout(self.cpu_layout)
        self.layout.addLayout(self.ram_layout)
        self.layout.addLayout(self.disk_layout)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_info)
        self.timer.start(1000)

    def create_info_line(self, icon_path):
        layout = QHBoxLayout()
        icon = QLabel()
        pixmap = QPixmap(icon_path)
        if pixmap.isNull():
            icon.setText("❌")  # Mostra se o ícone não carregar
        else:
            icon.setPixmap(pixmap.scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label = QLabel("...")
        layout.addWidget(icon)
        layout.addSpacing(10)
        layout.addWidget(label)
        layout.addStretch()
        return layout, label

    def update_info(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        self.cpu_value.setText(f"CPU: {cpu}%")
        self.ram_value.setText(f"RAM: {ram}%")
        self.disk_value.setText(f"Disco: {disk}%")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() & Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = None

if __name__ == "__main__":
    app = QApplication([])
    window = SystemMonitor()
    window.show()
    app.exec()
