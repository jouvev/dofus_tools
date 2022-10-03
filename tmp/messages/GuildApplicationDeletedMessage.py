class GuildApplicationDeletedMessage:
   def __init__(self,input):
      self._deletedFunc(input)
   
   def _deletedFunc(self,input) :
      self.deleted = input.readBoolean()