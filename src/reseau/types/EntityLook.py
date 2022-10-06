from src.reseau.types.SubEntity import SubEntity

class EntityLook:
   def __init__(self,input):
      self.skins = []
      self.indexedColors = []
      self.scales = []
      self.subentities = []
      _val2 = 0
      _val3 = 0
      _val4 = 0
      _item5 = None
      self._bonesIdFunc(input)
      _skinsLen = input.readUnsignedShort()
      for _i2 in range(0,_skinsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of skins.")
         self.skins.append(_val2)
      _indexedColorsLen = input.readUnsignedShort()
      for _i3 in range(0,_indexedColorsLen):
         _val3 = input.readInt()
         self.indexedColors.append(_val3)
      _scalesLen = input.readUnsignedShort()
      for _i4 in range(0,_scalesLen):
         _val4 = input.readVarShort()
         self.scales.append(_val4)
      _subentitiesLen = input.readUnsignedShort()
      for _i5 in range(0,_subentitiesLen):
         _item5 = SubEntity(input)
         self.subentities.append(_item5)
   
   def _bonesIdFunc(self,input) :
      self.bonesId = input.readVarUhShort()
      if(self.bonesId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.bonesId) + ") on element of EntityLook.bonesId.")

   def resume(self):
      print("bonesId :",self.bonesId)
      print("skins :",self.skins)
      print("indexedColors :",self.indexedColors)
      print("scales :",self.scales)
      for e in self.subentities:
         e.resume()
