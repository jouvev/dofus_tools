from src.reseau.messages.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage

class AllianceSummaryRequestMessage(PaginationRequestAbstractMessage):
   def __init__(self,input):
      super().__init__(input)
      self._nameFilterFunc(input)
      self._tagFilterFunc(input)
      self._playerNameFilterFunc(input)
      self._sortTypeFunc(input)
      self._sortDescendingFunc(input)
   
   def _nameFilterFunc(self,input) :
      self.nameFilter = input.readUTF()
   
   def _tagFilterFunc(self,input) :
      self.tagFilter = input.readUTF()
   
   def _playerNameFilterFunc(self,input) :
      self.playerNameFilter = input.readUTF()
   
   def _sortTypeFunc(self,input) :
      self.sortType = input.readByte()
      if(self.sortType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.sortType) + ") on element of AllianceSummaryRequestMessage.sortType.")
   
   def _sortDescendingFunc(self,input) :
      self.sortDescending = input.readBoolean()

   def resume(self):
      super().resume()
      print("nameFilter :",self.nameFilter)
      print("tagFilter :",self.tagFilter)
      print("playerNameFilter :",self.playerNameFilter)
      print("sortType :",self.sortType)
      print("sortDescending :",self.sortDescending)
