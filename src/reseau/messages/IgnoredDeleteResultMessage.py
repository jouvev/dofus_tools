from src.reseau.types.AccountTagInformation import AccountTagInformation

class IgnoredDeleteResultMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self.tag = AccountTagInformation(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.success = bool(bin(_box0)[2:].zfill(8)[0])
      self.session = bool(bin(_box0)[2:].zfill(8)[1])

   def resume(self):
      self.tag.resum()
