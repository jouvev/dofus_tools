class CharacterCharacteristic:
   def __init__(self,input):
      self._characteristicIdFunc(input)
   
   def _characteristicIdFunc(self,input) :
      self.characteristicId = input.readShort()