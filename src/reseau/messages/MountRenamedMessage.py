class MountRenamedMessage:
   def __init__(self,input):
      self._mountIdFunc(input)
      self._nameFunc(input)
   
   def _mountIdFunc(self,input) :
      self.mountId = input.readVarInt()
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()

   def resume(self):
      print("mountId :",self.mountId)
      print("name :",self.name)
