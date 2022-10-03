class GameRolePlayArenaRegisterMessage:
   def __init__(self,input):
      self._battleModeFunc(input)
   
   def _battleModeFunc(self,input) :
      self.battleMode = input.readInt()
      if(self.battleMode < 0) :
         raise RuntimeError("Forbidden value (" + self.battleMode + ") on element of GameRolePlayArenaRegisterMessage.battleMode.")