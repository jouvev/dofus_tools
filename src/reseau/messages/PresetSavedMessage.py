import src.reseau.TypesFactory as pf

class PresetSavedMessage:
   def __init__(self,input):
      self._presetIdFunc(input)
      _id2 = input.readUnsignedShort()
      self.preset = pf.TypesFactory.get_instance_id(_id2,input)
   
   def _presetIdFunc(self,input) :
      self.presetId = input.readShort()

   def resume(self):
      print("presetId :",self.presetId)
