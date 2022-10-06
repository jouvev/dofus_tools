import tmp.TypesFactory as pf

class IgnoredAddRequestMessage:
   def __init__(self,input):
      _id1 = input.readUnsignedShort()
      self.target = pf.TypesFactory.get_instance_id(_id1,input)
      self._sessionFunc(input)
   
   def _sessionFunc(self,input) :
      self.session = input.readBoolean()

   def resume(self):
      print("session :",self.session)
