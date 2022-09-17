class GameFightTurnListMessage:
    def __init__(self,content):
        self.idlen = content.readUnsignedShort()
        self.ids = []
        
        for i in range(self.idlen):
            self.ids.append(content.readDouble())
        
        self.deadlen = content.readUnsignedShort()
        self.deads = []
        
        for i in range(self.deadlen):
            self.deads.append(content.readDouble()) 
    
    def resume(self):
        for i in self.ids:
            print("id",i)
        for i in self.deads:
            print("dead",i)