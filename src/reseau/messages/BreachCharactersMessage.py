class BreachCharactersMessage:
   def __init__(self,input):
      self.characters = []
      _val1 = None
      _charactersLen = input.readUnsignedShort()
      for _i1 in range(0,_charactersLen):
         _val1 = input.readVarUhLong()
         if(_val1 < 0 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of characters.")
         self.characters.append(_val1)

   def resume(self):
      print("characters :",self.characters)
