import tmp.TypesFactory as pf

class AcquaintanceAddedMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.acquaintanceAdded = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      pass