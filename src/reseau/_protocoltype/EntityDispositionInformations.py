class EntityDispositionInformations:
    def __init__(self,content):
        self.cellid = content.readShort()
        self.direction = content.readByte()
        
    def resume(self):
        print("cellid",self.cellid)
        print("direction",self.direction)