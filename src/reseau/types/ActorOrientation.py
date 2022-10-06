class ActorOrientation:
   def __init__(self,input):
      self._idFunc(input)
      self._directionFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readDouble()
      if(self.id < -9007199254740992 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of ActorOrientation.id.")
   
   def _directionFunc(self,input) :
      self.direction = input.readByte()
      if(self.direction < 0) :
         raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of ActorOrientation.direction.")

   def resume(self):
      print("id :",self.id)
      print("direction :",self.direction)
