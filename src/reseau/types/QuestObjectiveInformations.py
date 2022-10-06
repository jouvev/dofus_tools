class QuestObjectiveInformations:
   def __init__(self,input):
      self.dialogParams = []
      _val3 = None
      self._objectiveIdFunc(input)
      self._objectiveStatusFunc(input)
      _dialogParamsLen = input.readUnsignedShort()
      for _i3 in range(0,_dialogParamsLen):
         _val3 = input.readUTF()
         self.dialogParams.append(_val3)
   
   def _objectiveIdFunc(self,input) :
      self.objectiveId = input.readVarUhShort()
      if(self.objectiveId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectiveId) + ") on element of QuestObjectiveInformations.objectiveId.")
   
   def _objectiveStatusFunc(self,input) :
      self.objectiveStatus = input.readBoolean()

   def resume(self):
      print("objectiveId :",self.objectiveId)
      print("objectiveStatus :",self.objectiveStatus)
      print("dialogParams :",self.dialogParams)
