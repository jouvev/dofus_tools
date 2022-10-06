from src.reseau.types.PresetsContainerPreset import PresetsContainerPreset

class IconNamedPreset(PresetsContainerPreset):
   def __init__(self,input):
      super().__init__(input)
      self._iconIdFunc(input)
      self._nameFunc(input)
   
   def _iconIdFunc(self,input) :
      self.iconId = input.readShort()
      if(self.iconId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.iconId) + ") on element of IconNamedPreset.iconId.")
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()

   def resume(self):
      super().resume()
      print("iconId :",self.iconId)
      print("name :",self.name)
