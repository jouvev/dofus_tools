from src.reseau.types.ItemForPreset import ItemForPreset

class ItemForPresetUpdateMessage:
   def __init__(self,input):
      self._presetIdFunc(input)
      self.presetItem = ItemForPreset(input)
   
   def _presetIdFunc(self,input) :
      self.presetId = input.readShort()

   def resume(self):
      print("presetId :",self.presetId)
      self.presetItem.resume()
