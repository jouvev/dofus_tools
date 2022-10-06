import tmp.TypesFactory as pf

class IdolFightPreparationUpdateMessage:
   def __init__(self,input):
      self.idols = []
      _id2 = 0
      _item2 = None
      self._idolSourceFunc(input)
      _idolsLen = input.readUnsignedShort()
      for _i2 in range(0,_idolsLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.idols.append(_item2)
   
   def _idolSourceFunc(self,input) :
      self.idolSource = input.readByte()
      if(self.idolSource < 0) :
         raise RuntimeError("Forbidden value (" + str(self.idolSource) + ") on element of IdolFightPreparationUpdateMessage.idolSource.")

   def resume(self):
      print("idolSource :",self.idolSource)
      for e in self.idols:
         e.resume()
