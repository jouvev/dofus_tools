class GameRolePlayArenaRegistrationWarningMessage:
   def __init__(self,input):
      self._battleModeFunc(input)
   
   def _battleModeFunc(self,input) :
      self.battleMode = input.readInt()
      if(self.battleMode < 0) :
         raise RuntimeError("Forbidden value (" + str(self.battleMode) + ") on element of GameRolePlayArenaRegistrationWarningMessage.battleMode.")

   def resume(self):
      print("battleMode :",self.battleMode)
