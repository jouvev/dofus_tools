from src.reseau.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation

class GuildUnlockNewTabActivity(GuildLogbookEntryBasicInformation):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
