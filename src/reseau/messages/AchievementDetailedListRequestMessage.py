class AchievementDetailedListRequestMessage:
   def __init__(self,input):
      self._categoryIdFunc(input)
   
   def _categoryIdFunc(self,input) :
      self.categoryId = input.readVarUhShort()
      if(self.categoryId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.categoryId) + ") on element of AchievementDetailedListRequestMessage.categoryId.")

   def resume(self):
      print("categoryId :",self.categoryId)
