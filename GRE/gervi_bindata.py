class TooBigValueOfException(BaseException): ...

class IsNotWordValueException(BaseException): ...

class TooSmallBinaryDataSizeException(BaseException): ...

class TooSmallBinaryDataSizeForReadingWordException(BaseException): ...

class InvalidCharNumberException(BaseException): ...

class TooBigOtherValueException(BaseException): ...

class BinaryData:
    """
    Gervi Binary data class
    A fudamental class for GVM. It is a list of numbers, which can be 1 or 0
    """
    def __init__(self, size = 8):
        """
        BinaryData constructor
        in: size (integer, optional, default = 8)
        raises: TooSmallBinaryDataSizeException if size < 8
        """
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
    
    def __fill(self, other):
        processList = self.__returnStrArgs(other)
        filler = len(processList[0]) - len(processList[1])
        if filler < 0:
            raise TooBigOtherValueException('Size of other (%d bits) greater than %d bits' % (other.size, self.size))
        processList[1] = '0' * filler + processList[1]
        return processList

    def __getNums(self, other):
        return [self.getInt(), other.getInt()]
    def __eq__(self, other):
        return str(self) == str(other)
    
    def setValue(self, index):
        """
        BinaryData.setValue
        in: index (integer)
        out: none
        Sets 1 at index in data list if it not are 0
        """
        if self.__data[index] == 0:
            self.__data[index] = 1
    
    def resetValue(self, index):
        """
        BinaryData.resetValue
        in: index (integer)
        out: none
        Sets 0 at index in data list if it not are 1
        """
        if self.__data[index] == 1:
            self.__data[index] = 0
    
    def resetAll(self):
        """
        BinaryData.resetAll
        in: none
        out: none
        Sets 0 at all indexes in data list
        """
        for i in range(self.size):
            if self.__data[i] == 1:
                self.resetValue(i)
    
    def getElement(self, index):
        return self.__data[index]

    #inserting methods
    def valueOf(self, binaryDataObject):
        """
        BinaryData.valueOf
        in: binaryDataObject (BinaryData)
        out: none
        Copy value of binaryDataObject
        """
        if str(self).find('1') != -1:
            self.resetAll()
        cachedbdo = str(binaryDataObject)
        filler = self.size - len(cachedbdo)
        if filler < 0:
            raise TooBigValueOfException('The size of binaryDataObject greater than %s bits' % (self.size))
        cachedbdo = '0' * filler + cachedbdo
        for i in range(self.size):
            if cachedbdo[i] == '1':
                self.setValue(i)
            else:
                self.resetValue(i)

    def valueOfNumber(self, integerValue):
        """
        BinaryData.valueOfNumber
        in: integerValue (integer)
        out: none
        Transform integerValue to binary form and copy it in data list. Ignores sign.
        """
        if str(self).find('1') != -1:
            self.resetAll()
        inInt = bin(integerValue)[2:]
        filler = self.size - len(inInt)
        if filler < 0:
            raise TooBigValueOfException('The size of inInt greater than %s bits' % (self.size))
        inInt = '0' * filler + inInt
        for i in range(self.size):
            if inInt[i] == '1':
                self.setValue(i)

    def valueOfChar(self, character):
        """
        BinaryData.valueOfChar
        in: character (char)
        out: none
        It calls BinaryData.valueOfNumber(ord(character))
        """
        self.valueOfNumber(ord(character))
    
    def valueOfBoolean(self, booleanValue):
        """
        BinaryData.Boolean
        in: booleanValue (bool)
        out: none
        If booleanValue is False then it records 0 in data list, else it records 1
        """
        if booleanValue:
            self.valueOfNumber(1)
        else:
            self.valueOfNumber(0)
    
    def valueOfStringBinaryDataObject(self, strBDO):
        if str(self).find('1') != -1:
            self.resetAll()
        filler = self.size - len(strBDO)
        if filler < 0:
            raise TooBigValueOfException('The size of binaryDataObject greater than %s bits' % (self.size))
        strBDO = '0' * filler + strBDO
        for i in range(self.size):
            if strBDO[i] == '1':
                self.setValue(i)
            else:
                self.resetValue(i)
    #end inserting methods

    #getting methods
    def get(self):
        return self.__data

    def getInt(self):
        numString = str(self)
        #numString = numString[numString.find('1'):]
        if numString[0] == '0':
            return int(numString[1:], 2)
        else:
            return int(numString[1:], 2) * -1
    
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
    
    def getBoolean(self):
        return bool(self.getElement(-1))
    # end getting methods

    #logical methods

    #common logical methods
    def logicAnd(self, other):
        #if self.size < second.size:
        #    raise TooBigV
        processData = self.__fill(other)
        for i in range(self.size):
            if processData[0][i] == '1' == processData[1][i]:
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicOr(self, other):
        processData = self.__fill(other)
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
        processData = self.__fill(other)
        for i in range(self.size):
            if (processData[0][i] == '1' and processData[1][i] == '1') or (processData[0][i] == '0' and processData[1][i] == '0'):
                self.resetValue(i)
            else:
                self.setValue(i)
    
    def logicNand(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if not (processData[0][i] == '1' == processData[1][i]):
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicNor(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if not (processData[0][i] == '1' or processData[1][i] == '1'):
                self.setValue(i)
            else:
                self.resetValue(i)

    def logicXnor(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if not (processData[0][i] == '1' and processData[1][i] == '1') or not (processData[0][i] == '0' and processData[1][i] == '0'):
                self.resetValue(i)
            else:
                self.setValue(i)
    
    #uncommon logical methods

    def logicImp(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if processData[0][i] == '1' and processData[1][i] == '0':
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicRimp(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if processData[0][i] == '0' and processData[1][i] == '1':
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicNimp(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if not (processData[0][i] == '1' and processData[1][i] == '0'):
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicNrimp(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if not (processData[0][i] == '0' and processData[1][i] == '1'):
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicEqv(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if processData[0][i] == processData[1][i]:
                self.setValue(i)
            else:
                self.resetValue(i)
    
    def logicNeqv(self, other):
        processData = self.__fill(other)
        for i in range(self.size):
            if processData[0][i] != processData[1][i]:
                self.setValue(i)
            else:
                self.resetValue(i)
    
    #end logical methods
    
    #math methods
    def add(self, other):
        processData = self.__getNums(other)
        self.valueOfNumber(processData[0] + processData[1])

    def substract(self, other):
        processData = self.__getNums(other)
        self.valueOfNumber(processData[0] - processData[1])

    def multiply(self, other):
        processData = self.__getNums(other)
        self.valueOfNumber(processData[0] * processData[1])

    def divide(self, other):
        processData = self.__getNums(other)
        self.valueOfNumber(processData[0] / processData[1])    
    #end math methods