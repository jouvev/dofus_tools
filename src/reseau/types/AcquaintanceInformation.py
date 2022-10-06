from src.reseau.types.AbstractContactInformations import AbstractContactInformations

class AcquaintanceInformation(AbstractContactInformations):
   def __init__(self,input):
      super().__init__(input)
      self._playerStateFunc(input)
   
   def _playerStateFunc(self,input) :
      self.playerState = input.readByte()
      if(self.playerState < 0) :
         raise RuntimeError("Forbidden value (" + str(self.playerState) + ") on element of AcquaintanceInformation.playerState.")

   def resume(self):
      super().resume()
      print("playerState :",self.playerState)
