from src.reseau.types.EntityLook import EntityLook

class PartyEntityBaseInformation:
   def __init__(self,input):
      self._indexIdFunc(input)
      self._entityModelIdFunc(input)
      self.entityLook = EntityLook(input)
   
   def _indexIdFunc(self,input) :
      self.indexId = input.readByte()
      if(self.indexId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.indexId) + ") on element of PartyEntityBaseInformation.indexId.")
   
   def _entityModelIdFunc(self,input) :
      self.entityModelId = input.readByte()
      if(self.entityModelId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.entityModelId) + ") on element of PartyEntityBaseInformation.entityModelId.")

   def resume(self):
      print("indexId :",self.indexId)
      print("entityModelId :",self.entityModelId)
      self.entityLook.resume()
