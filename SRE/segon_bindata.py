class TooBigValueOfException(BaseException): ...

class IsNotWordValueException(BaseException): ...

class TooSmallBinaryDataSizeException(BaseException): ...

class TooSmallBinaryDataSizeForReadingWordException(BaseException): ...

class InvalidCharNumberException(BaseException): ...

class TooBigOtherValueException(BaseException): ...

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
    
    def __returnStrArgs(self, other):
        return [str(self), str(other)]
    
    def __supply(self, other):
        processList = self.__returnStrArgs(other)
        supplier = len(processList[0]) - len(processList[1])
        if supplier < 0:
            raise TooBigOtherValueException('Size of other (%d bits) greater than %d bits' % (other.size, self.size))
        processList[1] = '0' * supplier + processList[1]
        return processList

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

    #inserting methods
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

    def valueOfChar(self, character):
        self.valueOfNumber(ord(character))
    #end inserting methods

    #getting methods

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

    #common logical methods
    def logicAnd(self, other):
        #if self.size < second.size:
        #    raise TooBigV
        processData = self.__supply(other)
        for i in range(self.size):
            if processData[0][i] == '1' == processData[1][i]:
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicOr(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if processData[0][i] == '1' or processData[1][i] == '1':
                self.setValue(i)
            else:
                self.resetValue(i)

    def logicNot(self):
        for i in range(self.size):
            if self.getElement(i) == 0:
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicXor(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if (processData[0][i] == '1' and processData[1][i] == '1') or (processData[0][i] == '0' and processData[1][i] == '0'):
                self.resetValue(i)
            else:
                self.setValue(i)
    
    def logicNand(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if not (processData[0][i] == '1' == processData[1][i]):
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicNor(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if not (processData[0][i] == '1' or processData[1][i] == '1'):
                self.setValue(i)
            else:
                self.resetValue(i)

    def logicXnor(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if not (processData[0][i] == '1' and processData[1][i] == '1') or not (processData[0][i] == '0' and processData[1][i] == '0'):
                self.resetValue(i)
            else:
                self.setValue(i)
    
    #uncommon logical methods

    def logicImp(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if processData[0][i] == '1' and processData[1][i] == '0':
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicRimp(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if processData[0][i] == '0' and processData[1][i] == '1':
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicNimp(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if not (processData[0][i] == '1' and processData[1][i] == '0'):
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicNrimp(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if not (processData[0][i] == '0' and processData[1][i] == '1'):
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicEqv(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if processData[0][i] == processData[1][i]:
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicNeqv(self, other):
        processData = self.__supply(other)
        for i in range(self.size):
            if processData[0][i] != processData[1][i]:
                self.setValue(i)
            else:
                self.resetValue(i)
    
    #end logical methods
    