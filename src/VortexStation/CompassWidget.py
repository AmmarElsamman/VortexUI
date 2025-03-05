from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtCore import Qt, QRectF, QPointF
import math

class CompassWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.heading = 0
        self.setMinimumSize(150, 150)
        self.setMaximumSize(150, 150)
        
        # Dracula theme colors
        self.backgroundColor = QColor("#282A36")
        self.foregroundColor = QColor("#F8F8F2")
        self.accentColor = QColor("#FFB86C")
        
    def setHeading(self, heading):
        """Update compass heading (0-360 degrees)"""
        self.heading = heading % 360
        self.update()  # Trigger repaint
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Calculate center and radius
        center = QPointF(self.width() / 2, self.height() / 2)
        radius = min(self.width(), self.height()) / 2 - 10
        
        # Draw background circle
        painter.setPen(QPen(self.foregroundColor, 2))
        painter.setBrush(self.backgroundColor)
        painter.drawEllipse(center, radius, radius)
        
        # Draw cardinal points
        painter.setFont(QFont('Arial', 10, QFont.Bold))
        cardinalPoints = ['N', 'E', 'S', 'W']
        for i, point in enumerate(cardinalPoints):
            angle = math.radians(i * 90 - self.heading)
            x = center.x() + (radius - 30) * math.sin(angle)
            y = center.y() - (radius - 30) * math.cos(angle)
            
            # Highlight North in accent color
            if point == 'N':
                painter.setPen(self.accentColor)
            else:
                painter.setPen(self.foregroundColor)
                
            painter.drawText(QRectF(x-15, y-15, 30, 30), Qt.AlignCenter, point)
        
        # Draw degree markers
        painter.setPen(QPen(self.foregroundColor, 1))
        for i in range(0, 360, 30):
            angle = math.radians(i - self.heading)
            innerRadius = radius - 15
            outerRadius = radius - 5
            
            x1 = center.x() + innerRadius * math.sin(angle)
            y1 = center.y() - innerRadius * math.cos(angle)
            x2 = center.x() + outerRadius * math.sin(angle)
            y2 = center.y() - outerRadius * math.cos(angle)
            
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))
        
        # Draw heading indicator (triangle)
        painter.setPen(QPen(self.accentColor, 2))
        painter.setBrush(self.accentColor)
        
        triangleSize = 15
        points = [
            QPointF(center.x(), center.y() - radius + 5),
            QPointF(center.x() - triangleSize/2, center.y() - radius + triangleSize + 5),
            QPointF(center.x() + triangleSize/2, center.y() - radius + triangleSize + 5)
        ]
        painter.drawPolygon(points)
        
        # Draw heading text
        painter.setFont(QFont('Arial', 10, QFont.Bold))
        painter.setPen(self.foregroundColor)
        headingText = f"{int(self.heading)}°"
        painter.drawText(QRectF(center.x()-50, center.y()-20, 100, 40), Qt.AlignCenter, headingText)