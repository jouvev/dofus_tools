from tmp.types.EntityLook import EntityLook
class GameContextRefreshEntityLookMessage:
   def __init__(self,input):
      self._idFunc(input)
      self.look = EntityLook(input)
   
   def _idFunc(self,input) :
      self.id = input.readDouble()
      if(self.id < -9007199254740992 or self.id > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of GameContextRefreshEntityLookMessage.id.")