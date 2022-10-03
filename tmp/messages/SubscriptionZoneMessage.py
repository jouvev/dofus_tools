class SubscriptionZoneMessage:
   def __init__(self,input):
      self._activeFunc(input)
   
   def _activeFunc(self,input) :
      self.active = input.readBoolean()