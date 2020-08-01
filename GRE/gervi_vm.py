#from gervi_vmf import VirtualMachineFile as VMF
#from gervi_workingmem import Work


#class VirtualMachine:
#    def __init__(self, file):
#        vmf = VMF()
#        vmf.load(file)
#        self.properties = vmf.getProperties()
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
