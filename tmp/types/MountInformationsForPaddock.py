class MountInformationsForPaddock:
   def __init__(self,input):
      self._modelIdFunc(input)
      self._nameFunc(input)
      self._ownerNameFunc(input)
   
   def _modelIdFunc(self,input) :
      self.modelId = input.readVarUhShort()
      if(self.modelId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element of MountInformationsForPaddock.modelId.")
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _ownerNameFunc(self,input) :
      self.ownerName = input.readUTF()

   def resume(self):
      print("modelId :",self.modelId)
      print("name :",self.name)
      print("ownerName :",self.ownerName)
