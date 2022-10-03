class DungeonKeyRingMessage:
   def __init__(self,input):
      self.availables = []
      self.unavailables = []
      _val1 = 0
      _val2 = 0
      _availablesLen = input.readUnsignedShort()
      for _i1 in range(0,_availablesLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of availables.")
         self.availables.append(_val1)
      _unavailablesLen = input.readUnsignedShort()
      for _i2 in range(0,_unavailablesLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of unavailables.")
         self.unavailables.append(_val2)