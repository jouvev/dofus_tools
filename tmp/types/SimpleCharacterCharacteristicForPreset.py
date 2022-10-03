class SimpleCharacterCharacteristicForPreset:
   def __init__(self,input):
      self._keywordFunc(input)
      self._baseFunc(input)
      self._additionnalFunc(input)
   
   def _keywordFunc(self,input) :
      self.keyword = input.readUTF()
   
   def _baseFunc(self,input) :
      self.base = input.readVarInt()
   
   def _additionnalFunc(self,input) :
      self.additionnal = input.readVarInt()