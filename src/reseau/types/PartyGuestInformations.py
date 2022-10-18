import src.reseau.TypesFactory as pf
from src.reseau.types.EntityLook import EntityLook
from src.reseau.types.PartyEntityBaseInformation import PartyEntityBaseInformation

class PartyGuestInformations:
   def __init__(self,input):
      self.entities = []
      _item8 = None
      self._guestIdFunc(input)
      self._hostIdFunc(input)
      self._nameFunc(input)
      self.guestLook = EntityLook(input)
      self._breedFunc(input)
      self._sexFunc(input)
      _id7 = input.readUnsignedShort()
      self.status = pf.TypesFactory.get_instance_id(_id7,input)
      _entitiesLen = input.readUnsignedShort()
      for _i8 in range(0,_entitiesLen):
         _item8 = PartyEntityBaseInformation(input)
         self.entities.append(_item8)
   
   def _guestIdFunc(self,input) :
      self.guestId = input.readVarUhLong()
      if(self.guestId < 0 or self.guestId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.guestId) + ") on element of PartyGuestInformations.guestId.")
   
   def _hostIdFunc(self,input) :
      self.hostId = input.readVarUhLong()
      if(self.hostId < 0 or self.hostId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.hostId) + ") on element of PartyGuestInformations.hostId.")
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()

   def resume(self):
      print("guestId :",self.guestId)
      print("hostId :",self.hostId)
      print("name :",self.name)
      print("breed :",self.breed)
      print("sex :",self.sex)
      self.guestLook.resume()
      self.status.resume()
      for e in self.entities:
         e.resume()
