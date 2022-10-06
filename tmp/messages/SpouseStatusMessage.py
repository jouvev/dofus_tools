class SpouseStatusMessage:
   def __init__(self,input):
      self._hasSpouseFunc(input)
   
   def _hasSpouseFunc(self,input) :
      self.hasSpouse = input.readBoolean()

   def resume(self):
      print("hasSpouse :",self.hasSpouse)
