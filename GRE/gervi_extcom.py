from gervi_vmf import VirtualMachineFile
import os
class CommandRunner:
    def __init__(self, virtualMachineFile):
        self.modules = virtualMachineFile.getModules()
    
    def run(self, command):
        for module in self.modules:
            modulePath = 'vm_modules/%s/' % (module)
            moduleComms = os.listdir(modulePath)
            for moduleComm in moduleComms:
                if moduleComm == command:
                    with open(modulePath + command, 'r', encoding='utf8') as com:
                        exec(com.read())
                return None
