class GameActionAcknowledgementMessage:
   def __init__(self,input):
      self._validFunc(input)
      self._actionIdFunc(input)
   
   def _validFunc(self,input) :
      self.valid = input.readBoolean()
   
   def _actionIdFunc(self,input) :
      self.actionId = input.readByte()