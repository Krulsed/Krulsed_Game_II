import sys
from PySide6.QtWidgets import QApplication, QWidget,QPushButton, QVBoxLayout


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("KHL AI — Season Simulator")
window.resize(1200,800)
##

btn_continue = QPushButton("Продолжить сезон")
btn_stats = QPushButton("Статистика сезона")
btn_calendar = QPushButton("Календарь")

layout = QVBoxLayout()

##
layout = QVBoxLayout()
layout.setSpacing(24)
layout.setContentsMargins(292, 52, 292, 52)
layout.addStretch()
layout.addWidget(btn_continue)
layout.addWidget(btn_stats)
layout.addWidget(btn_calendar)
layout.addStretch()

window.setLayout(layout)






window.setStyleSheet("""
    QWidget { background-color: #12151c; color: #e6e9ef; }
    QPushButton {
        background-color: #252c3b;
        border-radius: 10px;
        padding: 15px;
        font-size: 16px;
        font-weight: bold;
    }
    QPushButton:hover { background-color: #34405a; }
""")





def on_continue_clicked():
    print("Продолжаем сезон")
    window.setWindowTitle("KHL AI — Продолжить сезон")

def on_stats_clicked():
    print("Изучаем статистику сезона")
    window.setWindowTitle("KHL AI — Статистика сезона")

def on_calendar_clicked():
    print("Смотрим календарь")
    window.setWindowTitle("KHL AI — Календарь матчей")


btn_continue.clicked.connect(on_continue_clicked)
btn_stats.clicked.connect(on_stats_clicked)
btn_calendar.clicked.connect(on_calendar_clicked)






window.show()
sys.exit(app.exec())
