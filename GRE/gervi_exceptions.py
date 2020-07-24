from enum import Enum
from abc import abstractmethod
class ErrorLevels(Enum):
    WARNING, ERROR, CRITICAL, FATAL = range(4)
class GerviThrowable:
    @abstractmethod
    def throw(self):
        pass

class GerviError(GerviThrowable):
    def __init__(self, errorName, errorMsg, errorLevel):
        self.__errorName = errorName
        self.__errorMsg = errorMsg
        self.__errorLevel = errorLevel
    
    #def throw(self):