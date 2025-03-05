import cv2
import time

from VortexInterfaces import CameraManagerInterfaces

class CameraManager(CameraManagerInterfaces):
    def __init__(self, source):
        """
        Initializes the CameraManager object with the specified camera source.

        :param source: camera index or video file path
        """
        self.source = source
        self.capture = None

    def openCamera(self, retryInterval=2, maxTries=5):
        """
        Opens the camera or video source.
        Tries to reconnect if the camera fails to open up to the maxTries limit.
        
        :param retryInterval: time in seconds to wait before retrying
        :param maxTries: maximum number of attempts to open the camera
        """
        # If capture is already defined and opened, close it first
        if self.capture is not None and self.capture.isOpened():
            # print("Camera already open, closing it first.")
            self.closeCamera()
        
        tries = 0
        while tries < maxTries:
            if "!" in self.source:
                self.capture = cv2.VideoCapture(self.source, cv2.CAP_GSTREAMER)
            elif self.source.isdigit():
                self.capture = cv2.VideoCapture(int(self.source))
            else:
                self.capture = cv2.VideoCapture(self.source)

            if self.capture.isOpened():
                # print("Camera opened successfully.")
                return  # Camera opened successfully, exit the function
            else:
                tries += 1
                # print(f"Failed to open camera. Attempt {tries}/{maxTries}. Retrying in {retryInterval} seconds...")
                time.sleep(retryInterval)
        
        # print(f"Failed to open camera after {maxTries} attempts.")

    def closeCamera(self):
        """
        Closes the camera or video source.
        """
        if self.capture is not None and self.capture.isOpened():
            self.capture.release()
            # print("Camera closed.")
        else:
            pass
            # print("No camera to close.")

    def readFrame(self):
        """
        Reads a frame from the camera/video.
        If reading the frame fails, it closes the current capture and reopens the camera.

        :return: frame if successfully read, None if not
        """
        if self.capture is None or not self.capture.isOpened():
            # print("Camera not opened, reopening...")
            self.openCamera()  # Try to reopen camera

        ret, frame = self.capture.read()

        if not ret:
            # print("Failed to read frame. Reopening camera...")
            self.closeCamera()  # Close the camera if frame read fails
            self.openCamera()  # Reopen camera
            return None

        return frame

    def setSource(self, newSource):
        """
        Changes the camera or video source.
        
        :param newSource: new camera index or video file path
        """
        # print(f"Changing source from {self.source} to {newSource}")
        self.source = newSource
        if self.capture is not None and self.capture.isOpened():
            print("Camera already open, closing it first.")
            self.closeCamera()