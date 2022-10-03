class IconPresetSaveRequestMessage:
   def __init__(self,input):
      self._presetIdFunc(input)
      self._symbolIdFunc(input)
      self._updateDataFunc(input)
   
   def _presetIdFunc(self,input) :
      self.presetId = input.readShort()
   
   def _symbolIdFunc(self,input) :
      self.symbolId = input.readByte()
      if(self.symbolId < 0) :
         raise RuntimeError("Forbidden value (" + self.symbolId + ") on element of IconPresetSaveRequestMessage.symbolId.")
   
   def _updateDataFunc(self,input) :
      self.updateData = input.readBoolean()