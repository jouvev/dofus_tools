from tmp.messages.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage

class IconNamedPresetSaveRequestMessage(IconPresetSaveRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._nameFunc(input)
      self._typeFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of IconNamedPresetSaveRequestMessage.type.")

   def resume(self):
      super().resume()
      print("name :",self.name)
      print("type :",self.type)
