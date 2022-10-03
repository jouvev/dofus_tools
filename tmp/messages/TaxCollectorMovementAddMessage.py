import tmp.TypesFactory as pf
class TaxCollectorMovementAddMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.informations = pf.TypesFactory.get_instance_id(_id1,input)