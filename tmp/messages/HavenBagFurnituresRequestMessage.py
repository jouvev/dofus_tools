class HavenBagFurnituresRequestMessage:
   def __init__(self,input):
      self.cellIds = []
      self.funitureIds = []
      self.orientations = []
      _val1 = 0
      _val2 = 0
      _val3 = 0
      _cellIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_cellIdsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of cellIds.")
         self.cellIds.append(_val1)
      _funitureIdsLen = input.readUnsignedShort()
      for _i2 in range(0,_funitureIdsLen):
         _val2 = input.readInt()
         self.funitureIds.append(_val2)
      _orientationsLen = input.readUnsignedShort()
      for _i3 in range(0,_orientationsLen):
         _val3 = input.readByte()
         if(_val3 < 0) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of orientations.")
         self.orientations.append(_val3)

   def resume(self):
      print("cellIds :",self.cellIds)
      print("funitureIds :",self.funitureIds)
      print("orientations :",self.orientations)
