class BreachInvitationRequestMessage:
   def __init__(self,input):
      self.guests = []
      _val1 = None
      _guestsLen = input.readUnsignedShort()
      for _i1 in range(0,_guestsLen):
         _val1 = input.readVarUhLong()
         if(_val1 < 0 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of guests.")
         self.guests.append(_val1)