class GuildLogbookEntryBasicInformation:
   def __init__(self,input):
      self._idFunc(input)
      self._dateFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of GuildLogbookEntryBasicInformation.id.")
   
   def _dateFunc(self,input) :
      self.date = input.readDouble()
      if(self.date < 0 or self.date > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.date) + ") on element of GuildLogbookEntryBasicInformation.date.")

   def resume(self):
      print("id :",self.id)
      print("date :",self.date)
