import tmp.TypesFactory as pf

class BasicWhoIsRequestMessage:
   def __init__(self,input):
      self._verboseFunc(input)
      _id2 = input.readUnsignedShort()
      self.target = pf.TypesFactory.get_instance_id(_id2,input)
   
   def _verboseFunc(self,input) :
      self.verbose = input.readBoolean()

   def resume(self):
      print("verbose :",self.verbose)
