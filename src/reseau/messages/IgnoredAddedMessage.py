import src.reseau.TypesFactory as pf

class IgnoredAddedMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.ignoreAdded = pf.TypesFactory.get_instance_id(_id1,input)
      self._sessionFunc(input)
   
   def _sessionFunc(self,input) :
      self.session = input.readBoolean()

   def resume(self):
      print("session :",self.session)
