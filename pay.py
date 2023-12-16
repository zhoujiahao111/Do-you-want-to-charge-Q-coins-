# coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QEvent, QPoint
import random
from PyQt5.QtWidgets import QDesktopWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 240)  # 设置窗口大小为固定值
        self.setWindowTitle('充 Q 币')

        self.setMouseTracking(True)

        self.label = QLabel(self)
        self.label。setGeometry(20， 20, 150, 150)  # 设置图片位置和大小
        self.label。setScaledContents(True)  # 图片自适应大小
        self.label。setMouseTracking(True)

        self.button = QPushButton('确定', self)
        self.button。setGeometry(50, 200, 80, 30)  # 设置按钮位置和大小
        self.button。clicked.connect(self.close)  # 点击按钮关闭窗口
        self.button。setMouseTracking(True)

        self.buttonNO = QPushButton('取消', self)
        self.buttonNO。setGeometry(250, 200, 80, 30)  # 设置按钮位置和大小
        self.buttonNO。setMouseTracking(True)


        self.label_text = QLabel('你要充Q币吗', self)
        self.label_text。setGeometry(160, 18, 200, 150)  # 设置文本位置和大小
        self.label_text。setMouseTracking(True)

        font = self.label_text。font()
        font.setPointSize(21)  # 设置字号为21
        font.setBold(True)  # 设置加粗效果
        font.setWeight(75)  # 设置字体粗细为黑体

        self.label_text。setFont(font)  # 应用修改后的字体

        self.installEventFilter(self)  # 安装事件过滤器

    def eventFilter(self, obj, event):
        if obj == self and event.type() == QEvent.MouseMove:
            mouse_pos = event.globalPos()  # 获取鼠标在屏幕上的位置
            button_pos = self.buttonNO。mapToGlobal(QPoint(0, 0))  # 获取取消按钮在屏幕上的位置

            if -10 < (mouse_pos.x() - button_pos.x()) < 90 and -10 < (mouse_pos.y() - button_pos.y()) < 40:  # 判断距离是否小于10
                # print(mouse_pos, mouse_pos.x() - button_pos.x(), (mouse_pos.y() - button_pos.y()))
                self.moveWindow()  # 执行移动窗口函数

        return super().eventFilter(obj, event)
    def moveWindow(self): #随机移动窗口且不超出屏幕范围
        desktop = QDesktopWidget()
        screen_rect = desktop.availableGeometry()
        window_rect = self.geometry()
        # 随机选择新的窗口中心点，确保窗口不会超出屏幕边界
        new_center_x = random.randint(screen_rect.left() + window_rect.width() // 2,
                                      screen_rect.right() - window_rect.width() // 2)
        new_center_y = random.randint(screen_rect.top() + window_rect.height() // 2,
                                      screen_rect.bottom() - window_rect.height() // 2)
        # 创建一个新的中心点 QPoint 对象
        new_center = QPoint(new_center_x, new_center_y)

        # 移动窗口中心到新的位置
        window_rect.moveCenter(new_center)
        self.move(window_rect.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # 设置左边图片的路径
    image_path = './企鹅.png.png'
    pixmap = QPixmap(image_path)
    window.label。setPixmap(pixmap)

    window.show()
    sys.exit(app.exec_())
