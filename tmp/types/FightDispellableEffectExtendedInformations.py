import tmp.TypesFactory as pf
class FightDispellableEffectExtendedInformations:
   def __init__(self,input):
      self._actionIdFunc(input)
      self._sourceIdFunc(input)
      _id3 = input.readUnsignedShort()
      self.effect = pf.TypesFactory.get_instance_id(_id3,input)
   
   def _actionIdFunc(self,input) :
      self.actionId = input.readVarUhShort()
      if(self.actionId < 0) :
         raise RuntimeError("Forbidden value (" + self.actionId + ") on element of FightDispellableEffectExtendedInformations.actionId.")
   
   def _sourceIdFunc(self,input) :
      self.sourceId = input.readDouble()
      if(self.sourceId < -9007199254740992 or self.sourceId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.sourceId + ") on element of FightDispellableEffectExtendedInformations.sourceId.")