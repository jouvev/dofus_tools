from tmp.types.PlayerStatus import PlayerStatus
class PlayerStatusExtended(PlayerStatus):
   def __init__(self,input):
      super().__init__(input)
      self._messageFunc(input)
   
   def _messageFunc(self,input) :
      self.message = input.readUTF()