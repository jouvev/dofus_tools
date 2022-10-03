class HaapiConfirmationRequestMessage:
   def __init__(self,input):
      self._kamasFunc(input)
      self._ogrinesFunc(input)
      self._rateFunc(input)
      self._actionFunc(input)
   
   def _kamasFunc(self,input) :
      self.kamas = input.readVarUhLong()
      if(self.kamas < 0 or self.kamas > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.kamas + ") on element of HaapiConfirmationRequestMessage.kamas.")
   
   def _ogrinesFunc(self,input) :
      self.ogrines = input.readVarUhLong()
      if(self.ogrines < 0 or self.ogrines > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.ogrines + ") on element of HaapiConfirmationRequestMessage.ogrines.")
   
   def _rateFunc(self,input) :
      self.rate = input.readVarUhShort()
      if(self.rate < 0) :
         raise RuntimeError("Forbidden value (" + self.rate + ") on element of HaapiConfirmationRequestMessage.rate.")
   
   def _actionFunc(self,input) :
      self.action = input.readByte()
      if(self.action < 0) :
         raise RuntimeError("Forbidden value (" + self.action + ") on element of HaapiConfirmationRequestMessage.action.")