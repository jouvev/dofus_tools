from src.reseau.types.Shortcut import Shortcut

class ShortcutEmote(Shortcut):
   def __init__(self,input):
      super().__init__(input)
      self._emoteIdFunc(input)
   
   def _emoteIdFunc(self,input) :
      self.emoteId = input.readUnsignedShort()
      if(self.emoteId < 0 or self.emoteId > 65535) :
         raise RuntimeError("Forbidden value (" + str(self.emoteId) + ") on element of ShortcutEmote.emoteId.")

   def resume(self):
      super().resume()
      print("emoteId :",self.emoteId)
