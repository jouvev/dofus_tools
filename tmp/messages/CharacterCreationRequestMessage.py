class CharacterCreationRequestMessage:
   def __init__(self,input):
      self._nameFunc(input)
      self._breedFunc(input)
      self._sexFunc(input)
      for _i4 in range(0,5):
         self.colors[_i4] = input.readInt()
      self._cosmeticIdFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
      if(self.breed < 1 or self.breed > 18) :
         raise RuntimeError("Forbidden value (" + str(self.breed) + ") on element of CharacterCreationRequestMessage.breed.")
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()
   
   def _cosmeticIdFunc(self,input) :
      self.cosmeticId = input.readVarUhShort()
      if(self.cosmeticId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.cosmeticId) + ") on element of CharacterCreationRequestMessage.cosmeticId.")

   def resume(self):
      print("name :",self.name)
      print("breed :",self.breed)
      print("sex :",self.sex)
      print("cosmeticId :",self.cosmeticId)
