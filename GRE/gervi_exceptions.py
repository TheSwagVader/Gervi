from enum import Enum

errorLevels = Enum(WARNING, ERROR, CRITICAL, FATAL)
class GerviThrowable:
    @abstractmethod
    def throw(self):
        pass