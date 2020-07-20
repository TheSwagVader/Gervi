from segon_bindata import BinaryData

class WorkingMemory:
    def __init__(self, segmentSize,  horizontalSize, verticalSize):
        self.memory = [[BinaryData(segmentSize) for i in range(horizontalSize)] for j in range(verticalSize)]