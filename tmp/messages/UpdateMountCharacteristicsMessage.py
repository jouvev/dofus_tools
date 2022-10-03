import tmp.TypesFactory as pf
class UpdateMountCharacteristicsMessage:
   def __init__(self,input):
      self.boostToUpdateList = []
      _id2 = 0
      _item2 = None
      self._rideIdFunc(input)
      _boostToUpdateListLen = input.readUnsignedShort()
      for _i2 in range(0,_boostToUpdateListLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.boostToUpdateList.append(_item2)
   
   def _rideIdFunc(self,input) :
      self.rideId = input.readVarInt()