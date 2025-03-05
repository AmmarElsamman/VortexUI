import cv2
from PyQt5.QtCore import QTimer, pyqtSlot, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QSizePolicy


class CameraDisplay(QLabel):
    clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(320, 240)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("border: 2px solid #6272A4;")  # Dracula purple border
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()


class CameraWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cap = None
        
        # Set size policy to expand in both directions
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(640, 480)  # Set minimum size for the camera feed
        
        self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_frame)

    def start_camera(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("Error: Could not open camera.")
                return False
            self.timer.start(30)
            return True
        return False

    def stop_camera(self):
        if self.cap is not None:
            self.timer.stop()
            self.cap.release()
            self.cap = None
            self.clear()  # Clear the current image
            return True
        return False

    @pyqtSlot()
    def update_frame(self):
        if self.cap is None:
            return
            
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.setPixmap(QPixmap.fromImage(image))
        else:
            print("Error: Could not read frame.")

    def closeEvent(self, event):
        self.stop_camera()
        event.accept()