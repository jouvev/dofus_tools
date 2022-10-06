class GameRolePlayArenaPlayerBehavioursMessage:
   def __init__(self,input):
      self.flags = []
      self.sanctions = []
      _val1 = None
      _val2 = None
      _flagsLen = input.readUnsignedShort()
      for _i1 in range(0,_flagsLen):
         _val1 = input.readUTF()
         self.flags.append(_val1)
      _sanctionsLen = input.readUnsignedShort()
      for _i2 in range(0,_sanctionsLen):
         _val2 = input.readUTF()
         self.sanctions.append(_val2)
      self._banDurationFunc(input)
   
   def _banDurationFunc(self,input) :
      self.banDuration = input.readInt()
      if(self.banDuration < 0) :
         raise RuntimeError("Forbidden value (" + str(self.banDuration) + ") on element of GameRolePlayArenaPlayerBehavioursMessage.banDuration.")

   def resume(self):
      print("banDuration :",self.banDuration)
      print("flags :",self.flags)
      print("sanctions :",self.sanctions)
