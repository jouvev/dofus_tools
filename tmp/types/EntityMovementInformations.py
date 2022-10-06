class EntityMovementInformations:
   def __init__(self,input):
      self.steps = []
      _val2 = 0
      self._idFunc(input)
      _stepsLen = input.readUnsignedShort()
      for _i2 in range(0,_stepsLen):
         _val2 = input.readByte()
         self.steps.append(_val2)
   
   def _idFunc(self,input) :
      self.id = input.readInt()

   def resume(self):
      print("id :",self.id)
      print("steps :",self.steps)
