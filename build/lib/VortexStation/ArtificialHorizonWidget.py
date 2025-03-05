from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QBrush, QPainterPath
from PyQt5.QtCore import Qt, QRectF, QPointF
import math
import time

class ArtificialHorizonWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize attitude values
        self.pitch = 0  # Degrees (-90 to +90)
        self.roll = 0   # Degrees (-180 to +180)
        
        
        
        # Dracula theme colors
        self.backgroundColor = QColor("#282A36")  # Dark background
        self.foregroundColor = QColor("#F8F8F2")  # Light text
        self.accentColor = QColor("#FFB86C")      # Orange accent
        self.sky_color = QColor("#6272A4")        # Dracula purple for sky
        self.ground_color = QColor("#44475A")     # Darker purple for ground
        self.line_color = QColor("#BD93F9")   # Dracula darker purple
        
        # Set minimum size to match compass
        self.setMinimumSize(150, 150)
        self.setMaximumSize(150, 150)

    
    def setPitch(self, pitch):
        """Set pitch angle in degrees"""
        self.pitch = max(-90, min(90, pitch))
        self.update()
    

    def setRoll(self, roll):
        """Set roll angle in degrees"""
        self.roll = roll % 360
        if self.roll > 180:
            self.roll -= 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Get widget dimensions
        w = self.width()
        h = self.height()
        radius = min(w, h) / 2 - 10
        center = QPointF(w / 2, h / 2)

        # Draw background circle
        painter.setPen(QPen(self.line_color, 2))
        painter.setBrush(self.backgroundColor)
        painter.drawEllipse(center, radius, radius)

        # Save state before rotation
        painter.save()
        painter.translate(center)
        painter.rotate(-self.roll)

        # Create circular clip region
        path = QPainterPath()
        path.addEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.setClipPath(path)

        # Calculate pitch offset
        pitch_offset = (self.pitch * radius) / 45.0
        
        # Draw sky and ground
        painter.setPen(Qt.NoPen)
        
        # Sky
        painter.setBrush(QBrush(self.sky_color))
        painter.drawRect(-radius, -radius, radius * 2, radius + pitch_offset)
        
        # Ground
        painter.setBrush(QBrush(self.ground_color))
        painter.drawRect(-radius, pitch_offset, radius * 2, radius)

        # Draw pitch lines
        painter.setPen(QPen(self.foregroundColor, 2))
        for i in range(-90, 91, 10):
            y = (-i * radius) / 45.0 + pitch_offset
            if abs(y) <= radius:
                # Adjust line width based on importance
                width = radius/2 if i == 0 else radius/3 if i % 30 == 0 else radius/4
                
                # Draw the line
                painter.drawLine(-width, y, width, y)
                
                # Add pitch values
                if i != 0 and i % 10 == 0:
                    painter.setFont(QFont('Arial', 8, QFont.Bold))
                    text = str(abs(i))
                    # Draw white background for better visibility
                    painter.setPen(self.backgroundColor)
                    painter.drawText(-width - 25, y + 5, text)
                    painter.drawText(width + 5, y + 5, text)
                    # Draw text in foreground color
                    painter.setPen(self.foregroundColor)
                    painter.drawText(-width - 25, y + 5, text)
                    painter.drawText(width + 5, y + 5, text)

        # Restore painter state
        painter.restore()

        # Draw roll indicators
        for i in range(0, 360, 30):
            angle = math.radians(i)
            x1 = center.x() + (radius - 20) * math.sin(angle)
            y1 = center.y() - (radius - 20) * math.cos(angle)
            x2 = center.x() + (radius - 10) * math.sin(angle)
            y2 = center.y() - (radius - 10) * math.cos(angle)
            
            if i == 0:
                # Draw triangle for 0 degrees
                painter.setPen(QPen(self.accentColor, 2))
                painter.setBrush(self.accentColor)
                points = [
                    QPointF(x2, y2),
                    QPointF(x2 - 5, y2 - 8),
                    QPointF(x2 + 5, y2 - 8)
                ]
                painter.drawPolygon(points)
            else:
                painter.setPen(QPen(self.line_color, 2))
                painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        # Draw aircraft reference
        painter.setPen(QPen(self.accentColor, 3))
        painter.setBrush(self.accentColor)
        
        # Center dot
        painter.drawEllipse(center, 4, 4)
        
        # Wings and nose
        wing_size = radius / 6
        painter.drawLine(int(center.x() - wing_size*2), int(center.y()), 
                        int(center.x() - wing_size/2), int(center.y()))
        painter.drawLine(int(center.x() + wing_size/2), int(center.y()), 
                        int(center.x() + wing_size*2), int(center.y()))
        painter.drawLine(int(center.x()), int(center.y() - wing_size), 
                        int(center.x()), int(center.y() + wing_size/2))

        