from src.reseau.messages.SymbioticObjectAssociateRequestMessage import SymbioticObjectAssociateRequestMessage

class MimicryObjectFeedAndAssociateRequestMessage(SymbioticObjectAssociateRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._foodUIDFunc(input)
      self._foodPosFunc(input)
      self._previewFunc(input)
   
   def _foodUIDFunc(self,input) :
      self.foodUID = input.readVarUhInt()
      if(self.foodUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.foodUID) + ") on element of MimicryObjectFeedAndAssociateRequestMessage.foodUID.")
   
   def _foodPosFunc(self,input) :
      self.foodPos = input.readUnsignedByte()
      if(self.foodPos < 0 or self.foodPos > 255) :
         raise RuntimeError("Forbidden value (" + str(self.foodPos) + ") on element of MimicryObjectFeedAndAssociateRequestMessage.foodPos.")
   
   def _previewFunc(self,input) :
      self.preview = input.readBoolean()

   def resume(self):
      super().resume()
      print("foodUID :",self.foodUID)
      print("foodPos :",self.foodPos)
      print("preview :",self.preview)
