from tmp.types.UpdatedStorageTabInformation import UpdatedStorageTabInformation
class GuildUpdateChestTabRequestMessage:
   def __init__(self,input):
      self.tab = UpdatedStorageTabInformation(input)