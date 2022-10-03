from tmp.types.Shortcut import Shortcut
class ShortcutSmiley(Shortcut):
   def __init__(self,input):
      super().__init__(input)
      self._smileyIdFunc(input)
   
   def _smileyIdFunc(self,input) :
      self.smileyId = input.readVarUhShort()
      if(self.smileyId < 0) :
         raise RuntimeError("Forbidden value (" + self.smileyId + ") on element of ShortcutSmiley.smileyId.")