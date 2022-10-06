from tmp.messages.TaxCollectorDialogQuestionBasicMessage import TaxCollectorDialogQuestionBasicMessage

class TaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionBasicMessage):
   def __init__(self,input):
      super().__init__(input)
      self._maxPodsFunc(input)
      self._prospectingFunc(input)
      self._wisdomFunc(input)
      self._taxCollectorsCountFunc(input)
      self._taxCollectorAttackFunc(input)
      self._kamasFunc(input)
      self._experienceFunc(input)
      self._podsFunc(input)
      self._itemsValueFunc(input)
   
   def _maxPodsFunc(self,input) :
      self.maxPods = input.readVarUhShort()
      if(self.maxPods < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxPods) + ") on element of TaxCollectorDialogQuestionExtendedMessage.maxPods.")
   
   def _prospectingFunc(self,input) :
      self.prospecting = input.readVarUhShort()
      if(self.prospecting < 0) :
         raise RuntimeError("Forbidden value (" + str(self.prospecting) + ") on element of TaxCollectorDialogQuestionExtendedMessage.prospecting.")
   
   def _wisdomFunc(self,input) :
      self.wisdom = input.readVarUhShort()
      if(self.wisdom < 0) :
         raise RuntimeError("Forbidden value (" + str(self.wisdom) + ") on element of TaxCollectorDialogQuestionExtendedMessage.wisdom.")
   
   def _taxCollectorsCountFunc(self,input) :
      self.taxCollectorsCount = input.readByte()
      if(self.taxCollectorsCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.taxCollectorsCount) + ") on element of TaxCollectorDialogQuestionExtendedMessage.taxCollectorsCount.")
   
   def _taxCollectorAttackFunc(self,input) :
      self.taxCollectorAttack = input.readInt()
   
   def _kamasFunc(self,input) :
      self.kamas = input.readVarUhLong()
      if(self.kamas < 0 or self.kamas > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element of TaxCollectorDialogQuestionExtendedMessage.kamas.")
   
   def _experienceFunc(self,input) :
      self.experience = input.readVarUhLong()
      if(self.experience < 0 or self.experience > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element of TaxCollectorDialogQuestionExtendedMessage.experience.")
   
   def _podsFunc(self,input) :
      self.pods = input.readVarUhInt()
      if(self.pods < 0) :
         raise RuntimeError("Forbidden value (" + str(self.pods) + ") on element of TaxCollectorDialogQuestionExtendedMessage.pods.")
   
   def _itemsValueFunc(self,input) :
      self.itemsValue = input.readVarUhLong()
      if(self.itemsValue < 0 or self.itemsValue > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.itemsValue) + ") on element of TaxCollectorDialogQuestionExtendedMessage.itemsValue.")

   def resume(self):
      super().resume()
      print("maxPods :",self.maxPods)
      print("prospecting :",self.prospecting)
      print("wisdom :",self.wisdom)
      print("taxCollectorsCount :",self.taxCollectorsCount)
      print("taxCollectorAttack :",self.taxCollectorAttack)
      print("kamas :",self.kamas)
      print("experience :",self.experience)
      print("pods :",self.pods)
      print("itemsValue :",self.itemsValue)
