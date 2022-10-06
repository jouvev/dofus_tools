from src.reseau.types.CharacterCharacteristic import CharacterCharacteristic

class CharacterCharacteristicDetailed(CharacterCharacteristic):
   def __init__(self,input):
      super().__init__(input)
      self._baseFunc(input)
      self._additionalFunc(input)
      self._objectsAndMountBonusFunc(input)
      self._alignGiftBonusFunc(input)
      self._contextModifFunc(input)
   
   def _baseFunc(self,input) :
      self.base = input.readVarInt()
   
   def _additionalFunc(self,input) :
      self.additional = input.readVarInt()
   
   def _objectsAndMountBonusFunc(self,input) :
      self.objectsAndMountBonus = input.readVarInt()
   
   def _alignGiftBonusFunc(self,input) :
      self.alignGiftBonus = input.readVarInt()
   
   def _contextModifFunc(self,input) :
      self.contextModif = input.readVarInt()

   def resume(self):
      super().resume()
      print("base :",self.base)
      print("additional :",self.additional)
      print("objectsAndMountBonus :",self.objectsAndMountBonus)
      print("alignGiftBonus :",self.alignGiftBonus)
      print("contextModif :",self.contextModif)
