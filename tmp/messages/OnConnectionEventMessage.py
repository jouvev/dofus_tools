class OnConnectionEventMessage:
   def __init__(self,input):
      self._eventTypeFunc(input)
   
   def _eventTypeFunc(self,input) :
      self.eventType = input.readByte()
      if(self.eventType < 0) :
         raise RuntimeError("Forbidden value (" + self.eventType + ") on element of OnConnectionEventMessage.eventType.")