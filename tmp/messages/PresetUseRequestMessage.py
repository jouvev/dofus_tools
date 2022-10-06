class PresetUseRequestMessage:
   def __init__(self,input):
      self._presetIdFunc(input)
   
   def _presetIdFunc(self,input) :
      self.presetId = input.readShort()

   def resume(self):
      print("presetId :",self.presetId)
