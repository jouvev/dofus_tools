from src.reseau.types.AlignmentWarEffortInformation import AlignmentWarEffortInformation

class AlignmentWarEffortProgressionMessage:
   def __init__(self,input):
      self.effortProgressions = []
      _item1 = None
      _effortProgressionsLen = input.readUnsignedShort()
      for _i1 in range(0,_effortProgressionsLen):
         _item1 = AlignmentWarEffortInformation(input)
         self.effortProgressions.append(_item1)

   def resume(self):
      for e in self.effortProgressions:
         e.resume()
