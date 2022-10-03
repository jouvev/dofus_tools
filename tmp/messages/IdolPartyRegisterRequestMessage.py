class IdolPartyRegisterRequestMessage:
   def __init__(self,input):
      self._registerFunc(input)
   
   def _registerFunc(self,input) :
      self.register = input.readBoolean()