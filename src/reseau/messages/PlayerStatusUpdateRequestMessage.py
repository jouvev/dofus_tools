import src.reseau.TypesFactory as pf

class PlayerStatusUpdateRequestMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.status = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      self.status.resume()
