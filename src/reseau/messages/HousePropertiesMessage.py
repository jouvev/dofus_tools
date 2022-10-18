import src.reseau.TypesFactory as pf

class HousePropertiesMessage:
   def __init__(self,input):
      self.doorsOnMap = []
      _val2 = 0
      self._houseIdFunc(input)
      _doorsOnMapLen = input.readUnsignedShort()
      for _i2 in range(0,_doorsOnMapLen):
         _val2 = input.readInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of doorsOnMap.")
         self.doorsOnMap.append(_val2)
      _id3 = input.readUnsignedShort()
      self.properties = pf.TypesFactory.get_instance_id(_id3,input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.houseId) + ") on element of HousePropertiesMessage.houseId.")

   def resume(self):
      print("houseId :",self.houseId)
      self.properties.resume()
      print("doorsOnMap :",self.doorsOnMap)
