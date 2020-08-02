from gervi_vmf import VirtualMachineFile
from gervi_workingmem import WorkingMemory
from gervi_ram import RandomAccessMemory
from gervi_extcom import CommandRunner


class VirtualMachine:
    def __init__(self, file):
        vmf = VirtualMachineFile()
        vmf.load(file)
        properties = vmf.getProperties()
        self.__name = properties['name']
        self.__shortname = properties['shortname']
        self.__author = properties['author']
        self.__email = properties['email']
        self.__version = properties['version']
        self.__desc = properties['desc']
        self.__segmentSize = properties['segsize']
        self.__workingMemory = WorkingMemory(self.__segmentSize, properties['wmsizeh'], properties['wmsizev'])
        self.__RAM = RandomAccessMemory(properties['ramsizeh'], properties['ramsizev'])
        self.__statusCode = 0
        self.__commandRunner = CommandRunner(vmf)
    
    def run(self):
        print('[%s v. %s][by %s(%s)]\n[%s]' % (self.__name, self.__version, self.__author, self.__email, self.__desc))
        while True:
            command = input('%s>' % (self.__shortname))
            if command == 'shtd': \
                break
            else:
                self.__commandRunner.run(input('%s>' % (self.__shortname)))
