class TooBigValueOfException(BaseException): ...

class IsNotWordValueException(BaseException): ...

class TooSmallBinaryDataSizeException(BaseException): ...

class TooSmallBinaryDataSizeForReadingWordException(BaseException): ...

class InvalidCharNumberException(BaseException): ...

class BinaryData:
    def __init__(self, size = 8):
        if size < 8:
            raise TooSmallBinaryDataSizeException('Require 8 bit for BinaryData size, but got %d' % (size))
        self.__data = [0 for i in range(size)]
        self.size = size
    def __str__(self):
    
        string = ''
        for i in range(len(self.__data)):
            string += str(self.__data[i])
        return string
    
    def __eq__(self, other):
        return str(self) == str(other)
    
    def setValue(self, index):
        if self.__data[index] == 0:
            self.__data[index] = 1
    
    def resetValue(self, index):
        if self.__data[index] == 1:
            self.__data[index] = 0
    
    def resetAll(self):
        for i in range(self.size):
            if self.__data[i] == 1:
                self.resetValue(i)
    
    def getElement(self, index):
        return self.__data[index]

    def valueOfNumber(self, integerValue):
        if str(self).find('1') != -1:
            self.resetAll()
        inInt = bin(integerValue)[2:]
        supplier = self.size - len(inInt)
        if supplier < 0:
            raise TooBigValueOfException('The size of inInt greater than %s bits' % (self.size))
        inInt = '0' * supplier + inInt
        for i in range(self.size):
            if inInt[i] == '1':
                self.setValue(i)
    
    #def valueOfWord(self, wordValue):
    #    if wordValue > 65535:
    #        raise IsNotWordValueException('Excepted value lesser than 65536, got %d' % (wordValue))
    #    inWord = bin(wordValue)[2:]
    #    supplier = self.size - len(inWord)
    #    if supplier < 0:
    #        raise TooBigValueOfException('The size of inWord(16 bits) greater than %d bits' % (self.size))
    #    inWord = '0' * supplier + inWord
    #    for i in range(self.size):
    #        if inWord[i] == '1':
    #            self.setValue(i)
    def getInt(self):
        numString = str(self)
        numString = numString[numString.find('1'):]
        if numString[0] == 0:
            return int(numString[1:], 2)
        else:
            return -int(numString[1:], 2)
    
    def getUnsignedInt(self):
        return int(str(self), 2)

    def getWord(self):
        if self.size < 16:
            raise TooSmallBinaryDataSizeForReadingWordException('Size of BinaryData is %d, but Word require 16 bits' % (self.size))
        return int(str(self)[-16:], 2)
    
    def getByte(self):
        return int(str(self)[-8:], 2)
    
    def getChar(self):
        cache = self.getUnsignedInt()
        try:
            return chr(cache)
        except ValueError:
            raise InvalidCharNumberException('Char code must be in 0..1114111, got %d' % (cache))
    # end getting methods

    #logical methods

    def logicAnd(self, other):
        #if self.size < second.size:
        #    raise TooBigV
        selfStr, otherStr = str(self), str(other)
        supplier = len(selfStr) - len(otherStr)
        if supplier < 0:
            raise TooBigValueOfException('The size of inInt greater than %s bits' % (self.size))
        otherStr = '0' * supplier + otherStr
        for i in range(self.size):
            if selfStr[i] == '1' == otherStr[i]:
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicOr(self, other):
        selfStr, otherStr = str(self), str(other)
        supplier = len(selfStr) - len(otherStr)
        if supplier < 0:
            raise TooBigValueOfException('The size of inInt greater than %s bits' % (self.size))
        otherStr = '0' * supplier + otherStr
        for i in range(self.size):
            if selfStr[i] == '1' or otherStr[i] == '1':
                self.setValue(i)
            else:
                self.resetValue(i)

