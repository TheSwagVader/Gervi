class InvalidRAMAddressException(BaseException): ...

class RandomAccessMemory:
    def __init__(self, horizontalSize, verticalSize):
        self.__ram = [[None for i in range(horizontalSize)] for j in range(verticalSize)]
        self.__area = (horizontalSize, verticalSize)
    
    def isFree(self, addrX, addrY):
        return self.__ram[addrY][addrX] == None
    
    def isNotFree(self, addrX, addrY):
        return not self.isFree(addrX, addrY)
    
    def clear(self):
        self.__ram = [[None for i in range(self.__area[0])] for j in range(self.__area[1])]
    
    def erase(self, addrX, addrY):
        self.__ram[addrY][addrX] = None

    def push(self, data, addrX = 'nearest_free', addrY = 'nearest_free'):
        if (addrX == 'nearest_free' or addrY == 'nearest_free') and not (addrX == 'nearest_free' == addrY):
            raise InvalidRAMAddressException('RAM address not can be [%s:%s]' % (addrX, addrY))
        elif addrX == 'nearest_free' and addrY == 'nearest_free':
            for i in range(len(self.__ram)):
                for j in range(len(self.__ram[i])):
                    if self.isFree(j, i):
                        self.__ram[i][j] = data
                        return
            self.push(data, 0, 0) #if ram not have free segments
        else:
            self.__ram[addrY][addrX] = data
    
    def pull(self, addrX, addrY):
        cahced = self.__ram[addrY][addrX]
        self.erase(addrX, addrY)
        return cahced
    
    def get(self, addrX, addrY):
        return self.__ram[addrY][addrX]
        
