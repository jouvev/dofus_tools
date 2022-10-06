import tmp.TypesFactory as pf
from tmp.types.TreasureHuntFlag import TreasureHuntFlag

class TreasureHuntMessage:
   def __init__(self,input):
      self.knownStepsList = []
      self.flags = []
      _id3 = 0
      _item3 = None
      _item8 = None
      self._questTypeFunc(input)
      self._startMapIdFunc(input)
      _knownStepsListLen = input.readUnsignedShort()
      for _i3 in range(0,_knownStepsListLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.knownStepsList.append(_item3)
      self._totalStepCountFunc(input)
      self._checkPointCurrentFunc(input)
      self._checkPointTotalFunc(input)
      self._availableRetryCountFunc(input)
      _flagsLen = input.readUnsignedShort()
      for _i8 in range(0,_flagsLen):
         _item8 = TreasureHuntFlag(input)
         self.flags.append(_item8)
   
   def _questTypeFunc(self,input) :
      self.questType = input.readByte()
      if(self.questType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.questType) + ") on element of TreasureHuntMessage.questType.")
   
   def _startMapIdFunc(self,input) :
      self.startMapId = input.readDouble()
      if(self.startMapId < 0 or self.startMapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.startMapId) + ") on element of TreasureHuntMessage.startMapId.")
   
   def _totalStepCountFunc(self,input) :
      self.totalStepCount = input.readByte()
      if(self.totalStepCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.totalStepCount) + ") on element of TreasureHuntMessage.totalStepCount.")
   
   def _checkPointCurrentFunc(self,input) :
      self.checkPointCurrent = input.readVarUhInt()
      if(self.checkPointCurrent < 0) :
         raise RuntimeError("Forbidden value (" + str(self.checkPointCurrent) + ") on element of TreasureHuntMessage.checkPointCurrent.")
   
   def _checkPointTotalFunc(self,input) :
      self.checkPointTotal = input.readVarUhInt()
      if(self.checkPointTotal < 0) :
         raise RuntimeError("Forbidden value (" + str(self.checkPointTotal) + ") on element of TreasureHuntMessage.checkPointTotal.")
   
   def _availableRetryCountFunc(self,input) :
      self.availableRetryCount = input.readInt()

   def resume(self):
      print("questType :",self.questType)
      print("startMapId :",self.startMapId)
      print("totalStepCount :",self.totalStepCount)
      print("checkPointCurrent :",self.checkPointCurrent)
      print("checkPointTotal :",self.checkPointTotal)
      print("availableRetryCount :",self.availableRetryCount)
      for e in self.knownStepsList:
         e.resume()
      for e in self.flags:
         e.resume()
