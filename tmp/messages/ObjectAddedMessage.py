from tmp.types.ObjectItem import ObjectItem
class ObjectAddedMessage:
   def __init__(self,input):
      self.object = ObjectItem(input)
      self._originFunc(input)
   
   def _originFunc(self,input) :
      self.origin = input.readByte()
      if(self.origin < 0) :
         raise RuntimeError("Forbidden value (" + self.origin + ") on element of ObjectAddedMessage.origin.")