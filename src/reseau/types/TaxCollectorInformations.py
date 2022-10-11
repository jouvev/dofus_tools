import src.reseau.TypesFactory as pf
from src.reseau.types.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
from src.reseau.types.EntityLook import EntityLook

class TaxCollectorInformations:
   def __init__(self,input):
      self.complements = []
      _id10 = 0
      _item10 = None
      self._uniqueIdFunc(input)
      self._firtNameIdFunc(input)
      self._lastNameIdFunc(input)
      self.additionalInfos = AdditionalTaxCollectorInformations(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._subAreaIdFunc(input)
      self._stateFunc(input)
      self.look = EntityLook(input)
      _complementsLen = input.readUnsignedShort()
      for _i10 in range(0,_complementsLen):
         _id10 = input.readUnsignedShort()
         _item10 = pf.TypesFactory.get_instance_id(_id10,input)
         self.complements.append(_item10)
   
   def _uniqueIdFunc(self,input) :
      self.uniqueId = input.readDouble()
      if(self.uniqueId < 0 or self.uniqueId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.uniqueId) + ") on element of TaxCollectorInformations.uniqueId.")
   
   def _firtNameIdFunc(self,input) :
      self.firtNameId = input.readVarUhShort()
      if(self.firtNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.firtNameId) + ") on element of TaxCollectorInformations.firtNameId.")
   
   def _lastNameIdFunc(self,input) :
      self.lastNameId = input.readVarUhShort()
      if(self.lastNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of TaxCollectorInformations.lastNameId.")
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of TaxCollectorInformations.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of TaxCollectorInformations.worldY.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of TaxCollectorInformations.subAreaId.")
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of TaxCollectorInformations.state.")

   def resume(self):
      print("uniqueId :",self.uniqueId)
      print("firtNameId :",self.firtNameId)
      print("lastNameId :",self.lastNameId)
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("subAreaId :",self.subAreaId)
      print("state :",self.state)
      self.additionalInfos.resume()
      self.look.resume()
      for e in self.complements:
         e.resume()
