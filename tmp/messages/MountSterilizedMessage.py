class MountSterilizedMessage:
   def __init__(self,input):
      self._mountIdFunc(input)
   
   def _mountIdFunc(self,input) :
      self.mountId = input.readVarInt()