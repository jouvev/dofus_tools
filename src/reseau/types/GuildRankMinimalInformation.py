class GuildRankMinimalInformation:
   def __init__(self,input):
      self._idFunc(input)
      self._nameFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of GuildRankMinimalInformation.id.")
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()

   def resume(self):
      print("id :",self.id)
      print("name :",self.name)
