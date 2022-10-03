class MountRenameRequestMessage:
   def __init__(self,input):
      self._nameFunc(input)
      self._mountIdFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _mountIdFunc(self,input) :
      self.mountId = input.readVarInt()