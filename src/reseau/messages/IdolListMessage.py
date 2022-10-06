import src.reseau.TypesFactory as pf

class IdolListMessage:
   def __init__(self,input):
      self.chosenIdols = []
      self.partyChosenIdols = []
      self.partyIdols = []
      _val1 = 0
      _val2 = 0
      _id3 = 0
      _item3 = None
      _chosenIdolsLen = input.readUnsignedShort()
      for _i1 in range(0,_chosenIdolsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of chosenIdols.")
         self.chosenIdols.append(_val1)
      _partyChosenIdolsLen = input.readUnsignedShort()
      for _i2 in range(0,_partyChosenIdolsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of partyChosenIdols.")
         self.partyChosenIdols.append(_val2)
      _partyIdolsLen = input.readUnsignedShort()
      for _i3 in range(0,_partyIdolsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.partyIdols.append(_item3)

   def resume(self):
      print("chosenIdols :",self.chosenIdols)
      print("partyChosenIdols :",self.partyChosenIdols)
      for e in self.partyIdols:
         e.resume()
