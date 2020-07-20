from segon_bindata import BinaryData

class WorkingMemory:
    def __init__(self, segmentSize,  horizontalSize, verticalSize):
        self.__memory = [[BinaryData(segmentSize) for i in range(horizontalSize)] for j in range(verticalSize)]
        self.__protected = [[False for i in range(horizontalSize)] for j in range(verticalSize)]
    
    def isProtected(self, addrX, addrY):
        return self.__protected[addrY][addrX]
    
    def dataAt(self, addrX, addrY):
        print(str(self.__memory[addrY][addrX]))
    
    def write(self, addrX, addrY, data):
        self.__memory[addrY][addrX].valueOf(data)
    
    def read(self, addrX, addrY):
        return self.__memory[addrY][addrX]
    
    def protect(self, addrX, addrY):
        self.__protected[addrY][addrX] = True
