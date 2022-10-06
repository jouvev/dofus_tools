from src.reseau.types.AccountHouseInformations import AccountHouseInformations

class AccountHouseMessage:
   def __init__(self,input):
      self.houses = []
      _item1 = None
      _housesLen = input.readUnsignedShort()
      for _i1 in range(0,_housesLen):
         _item1 = AccountHouseInformations(input)
         self.houses.append(_item1)

   def resume(self):
      for e in self.houses:
         e.resume()
