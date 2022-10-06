import src.reseau.TypesFactory as pf
from src.reseau.types.SpellItem import SpellItem
from src.reseau.types.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations

class SlaveSwitchContextMessage:
   def __init__(self,input):
      self.slaveSpells = []
      self.shortcuts = []
      _item4 = None
      _id6 = 0
      _item6 = None
      self._masterIdFunc(input)
      self._slaveIdFunc(input)
      self._slaveTurnFunc(input)
      _slaveSpellsLen = input.readUnsignedShort()
      for _i4 in range(0,_slaveSpellsLen):
         _item4 = SpellItem(input)
         self.slaveSpells.append(_item4)
      self.slaveStats = CharacterCharacteristicsInformations(input)
      _shortcutsLen = input.readUnsignedShort()
      for _i6 in range(0,_shortcutsLen):
         _id6 = input.readUnsignedShort()
         _item6 = pf.TypesFactory.get_instance_id(_id6,input)
         self.shortcuts.append(_item6)
   
   def _masterIdFunc(self,input) :
      self.masterId = input.readDouble()
      if(self.masterId < -9007199254740992 or self.masterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element of SlaveSwitchContextMessage.masterId.")
   
   def _slaveIdFunc(self,input) :
      self.slaveId = input.readDouble()
      if(self.slaveId < -9007199254740992 or self.slaveId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.slaveId) + ") on element of SlaveSwitchContextMessage.slaveId.")
   
   def _slaveTurnFunc(self,input) :
      self.slaveTurn = input.readVarUhShort()
      if(self.slaveTurn < 0) :
         raise RuntimeError("Forbidden value (" + str(self.slaveTurn) + ") on element of SlaveSwitchContextMessage.slaveTurn.")

   def resume(self):
      print("masterId :",self.masterId)
      print("slaveId :",self.slaveId)
      print("slaveTurn :",self.slaveTurn)
      self.slaveStats.resum()
      for e in self.slaveSpells:
         e.resume()
      for e in self.shortcuts:
         e.resume()
