import src.reseau.TypesFactory as pf
from src.reseau.types.EntityLook import EntityLook

class GameContextSummonsInformation:
   def __init__(self,input):
      self.summons = []
      _id5 = 0
      _item5 = None
      _id1 = input.readUnsignedShort()
      self.spawnInformation = pf.TypesFactory.get_instance_id(_id1,input)
      self._waveFunc(input)
      self.look = EntityLook(input)
      _id4 = input.readUnsignedShort()
      self.stats = pf.TypesFactory.get_instance_id(_id4,input)
      _summonsLen = input.readUnsignedShort()
      for _i5 in range(0,_summonsLen):
         _id5 = input.readUnsignedShort()
         _item5 = pf.TypesFactory.get_instance_id(_id5,input)
         self.summons.append(_item5)
   
   def _waveFunc(self,input) :
      self.wave = input.readByte()
      if(self.wave < 0) :
         raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element of GameContextSummonsInformation.wave.")

   def resume(self):
      print("wave :",self.wave)
      self.look.resume()
      for e in self.summons:
         e.resume()
