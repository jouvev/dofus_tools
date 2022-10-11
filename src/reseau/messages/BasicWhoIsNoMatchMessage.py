import src.reseau.TypesFactory as pf

class BasicWhoIsNoMatchMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.target = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      pass