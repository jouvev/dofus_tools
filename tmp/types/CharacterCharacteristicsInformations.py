import tmp.TypesFactory as pf
from tmp.types.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
from tmp.types.CharacterSpellModification import CharacterSpellModification
class CharacterCharacteristicsInformations:
   def __init__(self,input):
      self.characteristics = []
      self.spellModifications = []
      _id8 = 0
      _item8 = None
      _item9 = None
      self._experienceFunc(input)
      self._experienceLevelFloorFunc(input)
      self._experienceNextLevelFloorFunc(input)
      self._experienceBonusLimitFunc(input)
      self._kamasFunc(input)
      self.alignmentInfos = ActorExtendedAlignmentInformations(input)
      self._criticalHitWeaponFunc(input)
      _characteristicsLen = input.readUnsignedShort()
      for _i8 in range(0,_characteristicsLen):
         _id8 = input.readUnsignedShort()
         _item8 = pf.TypesFactory.get_instance_id(_id8,input)
         self.characteristics.append(_item8)
      _spellModificationsLen = input.readUnsignedShort()
      for _i9 in range(0,_spellModificationsLen):
         _item9 = CharacterSpellModification(input)
         self.spellModifications.append(_item9)
      self._probationTimeFunc(input)
   
   def _experienceFunc(self,input) :
      self.experience = input.readVarUhLong()
      if(self.experience < 0 or self.experience > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experience + ") on element of CharacterCharacteristicsInformations.experience.")
   
   def _experienceLevelFloorFunc(self,input) :
      self.experienceLevelFloor = input.readVarUhLong()
      if(self.experienceLevelFloor < 0 or self.experienceLevelFloor > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experienceLevelFloor + ") on element of CharacterCharacteristicsInformations.experienceLevelFloor.")
   
   def _experienceNextLevelFloorFunc(self,input) :
      self.experienceNextLevelFloor = input.readVarUhLong()
      if(self.experienceNextLevelFloor < 0 or self.experienceNextLevelFloor > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experienceNextLevelFloor + ") on element of CharacterCharacteristicsInformations.experienceNextLevelFloor.")
   
   def _experienceBonusLimitFunc(self,input) :
      self.experienceBonusLimit = input.readVarUhLong()
      if(self.experienceBonusLimit < 0 or self.experienceBonusLimit > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experienceBonusLimit + ") on element of CharacterCharacteristicsInformations.experienceBonusLimit.")
   
   def _kamasFunc(self,input) :
      self.kamas = input.readVarUhLong()
      if(self.kamas < 0 or self.kamas > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.kamas + ") on element of CharacterCharacteristicsInformations.kamas.")
   
   def _criticalHitWeaponFunc(self,input) :
      self.criticalHitWeapon = input.readVarUhShort()
      if(self.criticalHitWeapon < 0) :
         raise RuntimeError("Forbidden value (" + self.criticalHitWeapon + ") on element of CharacterCharacteristicsInformations.criticalHitWeapon.")
   
   def _probationTimeFunc(self,input) :
      self.probationTime = input.readInt()
      if(self.probationTime < 0) :
         raise RuntimeError("Forbidden value (" + self.probationTime + ") on element of CharacterCharacteristicsInformations.probationTime.")