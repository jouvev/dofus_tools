from reseau.protocoltype.fight.EntityDispositionInformations import EntityDispositionInformations

class FightEntityDispositionInformations(EntityDispositionInformations):
    def __init__(self,content):
        super().__init__(content)
        self.carryingcharacterid = content.readDouble()
        
    def resume(self):
        super().resume()
        print("carryingcharacterid",self.carryingcharacterid)
        