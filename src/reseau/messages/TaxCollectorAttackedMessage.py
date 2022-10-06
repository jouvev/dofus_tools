from src.reseau.types.BasicGuildInformations import BasicGuildInformations

class TaxCollectorAttackedMessage:
   def __init__(self,input):
      self._firstNameIdFunc(input)
      self._lastNameIdFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
      self.guild = BasicGuildInformations(input)
   
   def _firstNameIdFunc(self,input) :
      self.firstNameId = input.readVarUhShort()
      if(self.firstNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of TaxCollectorAttackedMessage.firstNameId.")
   
   def _lastNameIdFunc(self,input) :
      self.lastNameId = input.readVarUhShort()
      if(self.lastNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of TaxCollectorAttackedMessage.lastNameId.")
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of TaxCollectorAttackedMessage.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of TaxCollectorAttackedMessage.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of TaxCollectorAttackedMessage.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of TaxCollectorAttackedMessage.subAreaId.")

   def resume(self):
      print("firstNameId :",self.firstNameId)
      print("lastNameId :",self.lastNameId)
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("mapId :",self.mapId)
      print("subAreaId :",self.subAreaId)
      self.guild.resum()
