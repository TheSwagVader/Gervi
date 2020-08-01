from gervi_bindata import BinaryData

#from gervi_ram import RandomAccessMemory as RAM
class WritingToProtectedAddressException(BaseException): ...

class WorkingMemory:
    def __init__(self, segmentSize,  horizontalSize, verticalSize):
        self.__memory = [[BinaryData(segmentSize) for i in range(horizontalSize)] for j in range(verticalSize)]
        self.__protected = [[False for i in range(horizontalSize)] for j in range(verticalSize)]
    
    def isProtected(self, addrX, addrY):
        return self.__protected[addrY][addrX]
    
    def getAddressContest(self, addrX, addrY):
        return self.__memory[addrY][addrX]
    
    def write(self, addrX, addrY, data):
        if self.__protected[addrY][addrX]:
            raise WritingToProtectedAddressException('Address [%d:%d] is protected. Writing impossible', (addrX, addrY))
        else:
            self.__memory[addrY][addrX].valueOf(data)
    
    def safeWrite(self, addrX, addrY, data):
        if self.__protected[addrY][addrX]:
            pass
        else:
            self.__memory[addrY][addrX].valueOf(data)
    
    def read(self, ramObject, addrX, addrY, ramDestinationAddrX = 'nearest_free', ramDestinationAddrY = 'nearest_free'):
        ramObject.push(self.__memory[addrY][addrX].get(), ramDestinationAddrX, ramDestinationAddrY)
    
    def readInt(self, ramObject, addrX, addrY, ramDestinationAddrX = 'nearest_free', ramDestinationAddrY = 'nearest_free'):
        ramObject.push(self.__memory[addrY][addrX].getInt(), ramDestinationAddrX, ramDestinationAddrY)
    
    def protect(self, addrX, addrY):
        if not self.__protected[addrY][addrX]:
            self.__protected[addrY][addrX] = True

    def unprotect(self, addrX, addrY):
        if self.__protected[addrY][addrX]:
            self.__protected[addrY][addrX] = False