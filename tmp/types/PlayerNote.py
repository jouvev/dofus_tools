class PlayerNote:
   def __init__(self,input):
      self._contentFunc(input)
      self._lastEditDateFunc(input)
   
   def _contentFunc(self,input) :
      self.content = input.readUTF()
   
   def _lastEditDateFunc(self,input) :
      self.lastEditDate = input.readDouble()
      if(self.lastEditDate < -9007199254740992 or self.lastEditDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.lastEditDate) + ") on element of PlayerNote.lastEditDate.")

   def resume(self):
      print("content :",self.content)
      print("lastEditDate :",self.lastEditDate)
