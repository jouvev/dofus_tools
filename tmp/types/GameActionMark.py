from tmp.types.GameActionMarkedCell import GameActionMarkedCell

class GameActionMark:
   def __init__(self,input):
      self.cells = []
      _item8 = None
      self._markAuthorIdFunc(input)
      self._markTeamIdFunc(input)
      self._markSpellIdFunc(input)
      self._markSpellLevelFunc(input)
      self._markIdFunc(input)
      self._markTypeFunc(input)
      self._markimpactCellFunc(input)
      _cellsLen = input.readUnsignedShort()
      for _i8 in range(0,_cellsLen):
         _item8 = GameActionMarkedCell(input)
         self.cells.append(_item8)
      self._activeFunc(input)
   
   def _markAuthorIdFunc(self,input) :
      self.markAuthorId = input.readDouble()
      if(self.markAuthorId < -9007199254740992 or self.markAuthorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.markAuthorId) + ") on element of GameActionMark.markAuthorId.")
   
   def _markTeamIdFunc(self,input) :
      self.markTeamId = input.readByte()
      if(self.markTeamId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.markTeamId) + ") on element of GameActionMark.markTeamId.")
   
   def _markSpellIdFunc(self,input) :
      self.markSpellId = input.readInt()
      if(self.markSpellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.markSpellId) + ") on element of GameActionMark.markSpellId.")
   
   def _markSpellLevelFunc(self,input) :
      self.markSpellLevel = input.readShort()
      if(self.markSpellLevel < 1 or self.markSpellLevel > 32767) :
         raise RuntimeError("Forbidden value (" + str(self.markSpellLevel) + ") on element of GameActionMark.markSpellLevel.")
   
   def _markIdFunc(self,input) :
      self.markId = input.readShort()
   
   def _markTypeFunc(self,input) :
      self.markType = input.readByte()
   
   def _markimpactCellFunc(self,input) :
      self.markimpactCell = input.readShort()
      if(self.markimpactCell < -1 or self.markimpactCell > 559) :
         raise RuntimeError("Forbidden value (" + str(self.markimpactCell) + ") on element of GameActionMark.markimpactCell.")
   
   def _activeFunc(self,input) :
      self.active = input.readBoolean()

   def resume(self):
      print("markAuthorId :",self.markAuthorId)
      print("markTeamId :",self.markTeamId)
      print("markSpellId :",self.markSpellId)
      print("markSpellLevel :",self.markSpellLevel)
      print("markId :",self.markId)
      print("markType :",self.markType)
      print("markimpactCell :",self.markimpactCell)
      print("active :",self.active)
      for e in self.cells:
         e.resume()
