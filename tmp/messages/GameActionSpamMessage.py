class GameActionSpamMessage:
   def __init__(self,input):
      self.cells = []
      _val1 = 0
      _cellsLen = input.readUnsignedShort()
      for _i1 in range(0,_cellsLen):
         _val1 = input.readShort()
         self.cells.append(_val1)