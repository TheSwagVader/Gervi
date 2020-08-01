from configparser import ConfigParser

GVM_PATH = '../VMs/'
class VirtualMachineFile:
    def __init__(self):
        self.file = ConfigParser()

    def load(self, file):
        self.file.read(GVM_PATH + file)
    
    def getProperties(self):
        return {
            'name' : self.file.get('META', 'Name'),
            'author' : self.file.get('META', 'Author'),
            'email' : self.file.get('META', 'AuthorEmail'),
            'version' : self.file.get('META', 'Version'),
            'desc' : self.file.get('META', 'Description'),
            'segsize' : self.file.getint('MEMORY', 'SegmentSize'),
            'wmsizev' : self.file.getint('MEMORY', 'WMSizeV'),
            'wmsizeh' : self.file.getint('MEMORY', 'WMSizeH'),
            'ramsizev' : self.file.getint('MEMORY', 'RAMSizeV'),
            'ramsizeh' : self.file.getint('MEMORY', 'RAMSizeH')
        }
