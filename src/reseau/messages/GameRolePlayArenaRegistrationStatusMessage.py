class GameRolePlayArenaRegistrationStatusMessage:
   def __init__(self,input):
      self._registeredFunc(input)
      self._stepFunc(input)
      self._battleModeFunc(input)
   
   def _registeredFunc(self,input) :
      self.registered = input.readBoolean()
   
   def _stepFunc(self,input) :
      self.step = input.readByte()
      if(self.step < 0) :
         raise RuntimeError("Forbidden value (" + str(self.step) + ") on element of GameRolePlayArenaRegistrationStatusMessage.step.")
   
   def _battleModeFunc(self,input) :
      self.battleMode = input.readInt()
      if(self.battleMode < 0) :
         raise RuntimeError("Forbidden value (" + str(self.battleMode) + ") on element of GameRolePlayArenaRegistrationStatusMessage.battleMode.")

   def resume(self):
      print("registered :",self.registered)
      print("step :",self.step)
      print("battleMode :",self.battleMode)
