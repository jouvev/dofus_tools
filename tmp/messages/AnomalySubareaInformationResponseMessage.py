from tmp.types.AnomalySubareaInformation import AnomalySubareaInformation

class AnomalySubareaInformationResponseMessage:
   def __init__(self,input):
      self.subareas = []
      _item1 = None
      _subareasLen = input.readUnsignedShort()
      for _i1 in range(0,_subareasLen):
         _item1 = AnomalySubareaInformation(input)
         self.subareas.append(_item1)

   def resume(self):
      for e in self.subareas:
         e.resume()
