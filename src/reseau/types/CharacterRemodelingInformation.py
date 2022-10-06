from src.reseau.types.AbstractCharacterInformation import AbstractCharacterInformation

class CharacterRemodelingInformation(AbstractCharacterInformation):
   def __init__(self,input):
      self.colors = []
      _val5 = 0
      super().__init__(input)
      self._nameFunc(input)
      self._breedFunc(input)
      self._sexFunc(input)
      self._cosmeticIdFunc(input)
      _colorsLen = input.readUnsignedShort()
      for _i5 in range(0,_colorsLen):
         _val5 = input.readInt()
         self.colors.append(_val5)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()
   
   def _cosmeticIdFunc(self,input) :
      self.cosmeticId = input.readVarUhShort()
      if(self.cosmeticId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.cosmeticId) + ") on element of CharacterRemodelingInformation.cosmeticId.")

   def resume(self):
      super().resume()
      print("name :",self.name)
      print("breed :",self.breed)
      print("sex :",self.sex)
      print("cosmeticId :",self.cosmeticId)
      print("colors :",self.colors)
