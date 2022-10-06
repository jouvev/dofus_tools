import src.reseau.TypesFactory as pf

class GameContextActorPositionInformations:
   def __init__(self,input):
      self._contextualIdFunc(input)
      _id2 = input.readUnsignedShort()
      self.disposition = pf.TypesFactory.get_instance_id(_id2,input)
   
   def _contextualIdFunc(self,input) :
      self.contextualId = input.readDouble()
      if(self.contextualId < -9007199254740992 or self.contextualId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.contextualId) + ") on element of GameContextActorPositionInformations.contextualId.")

   def resume(self):
      print("contextualId :",self.contextualId)
