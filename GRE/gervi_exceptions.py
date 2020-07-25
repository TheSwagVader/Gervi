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
    
    def throw(self):
        print('[%s] %s : %s' % (self.__errorLevel.name, self.__errorName, self.__errorMsg))
        if self.__errorLevel == ErrorLevels.WARNING:
            return 0
        elif self.__errorLevel == ErrorLevels.ERROR:
            answer = input('Continue? (y/n):')
            return 0 if answer == 'y' else 1
        else: 
            return 1

class GerviException(GerviThrowable):
    def __init__(self, exceptionName, exceptionMsg):
        self.__exceptionName = exceptionName
        self.__exceptionMsg = exceptionMsg
    
    def throw(self):
        print('%s: %s' % (self.__exceptionName, self.__exceptionMsg))
        return 1

UnknownError = GerviError('UnknownError', 'an unknown error called', ErrorLevels.FATAL)

UnknownException = GerviException('UnknownException', 'an unknown exception throwed')
