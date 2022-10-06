class GuildSelectChestTabRequestMessage:
   def __init__(self,input):
      self._tabNumberFunc(input)
   
   def _tabNumberFunc(self,input) :
      self.tabNumber = input.readVarUhInt()
      if(self.tabNumber < 0) :
         raise RuntimeError("Forbidden value (" + str(self.tabNumber) + ") on element of GuildSelectChestTabRequestMessage.tabNumber.")

   def resume(self):
      print("tabNumber :",self.tabNumber)
