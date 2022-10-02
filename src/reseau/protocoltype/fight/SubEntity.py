import reseau.protocoltype.fight.EntityLook as et

class SubEntity:
    def __init__(self,content):
        self.bindingpointcategory = content.readByte()
        self.bindingpointindex = content.readByte()
        self.subentitylook = et.EntityLook(content)
        
    def resume(self):
        print("bindingpointcategory",self.bindingpointcategory)
        print("bindingpointindex",self.bindingpointindex)
        self.subentitylook.resume()