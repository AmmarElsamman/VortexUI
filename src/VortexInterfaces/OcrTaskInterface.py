from abc import abstractmethod, ABC

class OcrTaskInterface(ABC):
    @abstractmethod
    def SubmitText(self):
        pass