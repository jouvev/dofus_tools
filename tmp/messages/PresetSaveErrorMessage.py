class PresetSaveErrorMessage:
   def __init__(self,input):
      self._presetIdFunc(input)
      self._codeFunc(input)
   
   def _presetIdFunc(self,input) :
      self.presetId = input.readShort()
   
   def _codeFunc(self,input) :
      self.code = input.readByte()
      if(self.code < 0) :
         raise RuntimeError("Forbidden value (" + str(self.code) + ") on element of PresetSaveErrorMessage.code.")

   def resume(self):
      print("presetId :",self.presetId)
      print("code :",self.code)
