class PlayerStatus:
    def __init__(self,content):
        self.status = content.readByte()
    
    def resume(self):
        print('status',self.status)