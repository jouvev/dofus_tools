from tmp.types.Idol import Idol
class GameFightStartMessage:
   def __init__(self,input):
      self.idols = []
      _item1 = None
      _idolsLen = input.readUnsignedShort()
      for _i1 in range(0,_idolsLen):
         _item1 = Idol(input)
         self.idols.append(_item1)