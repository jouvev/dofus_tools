class InteractiveUsedMessage:
   def __init__(self,input):
      self._entityIdFunc(input)
      self._elemIdFunc(input)
      self._skillIdFunc(input)
      self._durationFunc(input)
      self._canMoveFunc(input)
   
   def _entityIdFunc(self,input) :
      self.entityId = input.readVarUhLong()
      if(self.entityId < 0 or self.entityId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.entityId) + ") on element of InteractiveUsedMessage.entityId.")
   
   def _elemIdFunc(self,input) :
      self.elemId = input.readVarUhInt()
      if(self.elemId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.elemId) + ") on element of InteractiveUsedMessage.elemId.")
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhShort()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of InteractiveUsedMessage.skillId.")
   
   def _durationFunc(self,input) :
      self.duration = input.readVarUhShort()
      if(self.duration < 0) :
         raise RuntimeError("Forbidden value (" + str(self.duration) + ") on element of InteractiveUsedMessage.duration.")
   
   def _canMoveFunc(self,input) :
      self.canMove = input.readBoolean()

   def resume(self):
      print("entityId :",self.entityId)
      print("elemId :",self.elemId)
      print("skillId :",self.skillId)
      print("duration :",self.duration)
      print("canMove :",self.canMove)
