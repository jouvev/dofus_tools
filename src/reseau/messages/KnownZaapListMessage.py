class KnownZaapListMessage:
   def __init__(self,input):
      self.destinations = []
      _val1 = None
      _destinationsLen = input.readUnsignedShort()
      for _i1 in range(0,_destinationsLen):
         _val1 = input.readDouble()
         if(_val1 < 0 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of destinations.")
         self.destinations.append(_val1)

   def resume(self):
      print("destinations :",self.destinations)
