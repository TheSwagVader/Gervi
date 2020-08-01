from gervi_vmf import VirtualMachineFile
from gervi_workingmem import WorkingMemory
from gervi_ram import RandomAccessMemory


class VirtualMachine:
    def __init__(self, file):
        vmf = VirtualMachineFile()
        vmf.load(file)
        properties = vmf.getProperties()
        self.__name = properties['name']
        self.__author = properties['author']
        self.__email = properties['email']
        self.__version = properties['version']
        self.__desc = properties['desc']
        self.__segmentSize = properties['segsize']
        self.__workingMemory = WorkingMemory(self.__segmentSize, properties['wmsizeh'], properties['wmsizev'])
        self.__RAM = RandomAccessMemory(properties['ramsizeh'], properties['ramsizev'])
        self.__statusCode = 0
    
    def run(self):
        print('It works!')
