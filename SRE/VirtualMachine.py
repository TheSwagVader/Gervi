#import configparser, sys
#
#sys.path.append('..')

#def loadVMF(file):
#    virtualMachineFile = configparser.ConfigParser()
#    virtualMachineFile.read(file)
#    return virtualMachineFile


#class VirtualMachine:
#    def __init__(self, file):
#        VMF = loadVMF(file)
#        self.workingMem = [
#            [binmath.BinaryData(VMF.getint('MEMORY', 'SegmentSize')) for i in range(VMF.getint('WM', 'Width'))]
#            for j in range(VMF.getint('WM', 'Heigth'))
#            ]
#        self.RAM = [
#            [binmath.BinaryData(VMF.getint('MEMORY', 'SegmentSize')) for i in range(VMF.getint('RAM', 'Width'))]
#            for j in range(VMF.getint('RAM', 'Heigth'))
#            ]
#        self.statusCode = 0
#    
#    def run(self):
#        pass
