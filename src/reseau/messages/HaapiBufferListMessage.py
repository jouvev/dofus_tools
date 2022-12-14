from src.reseau.types.BufferInformation import BufferInformation

class HaapiBufferListMessage:
   def __init__(self,input):
      self.buffers = []
      _item1 = None
      _buffersLen = input.readUnsignedShort()
      for _i1 in range(0,_buffersLen):
         _item1 = BufferInformation(input)
         self.buffers.append(_item1)

   def resume(self):
      for e in self.buffers:
         e.resume()
