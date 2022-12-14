import src.reseau.TypesFactory as pf

class CompassUpdateMessage:
   def __init__(self,input):
      self._typeFunc(input)
      _id2 = input.readUnsignedShort()
      self.coords = pf.TypesFactory.get_instance_id(_id2,input)
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of CompassUpdateMessage.type.")

   def resume(self):
      print("type :",self.type)
      self.coords.resume()
