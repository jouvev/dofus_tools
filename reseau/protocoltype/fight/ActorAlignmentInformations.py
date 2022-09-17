class ActorAlignmentInformations:
    def __init__(self,content):
        self.alignement = content.readByte()
        self.alignementvalue = content.readByte()
        self.grade = content.readByte()
        self.power = content.readDouble()  
        
    def resume(self):
        print("alignement",self.alignement)
        print("alignementvalue",self.alignementvalue)
        print("grade",self.grade)
        print("power",self.power)